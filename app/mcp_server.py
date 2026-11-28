"""第6回: 用語集と各回の要点を MCP サーバーとして公開する。

使い方:
    uv run python -m app.mcp_agent --list-tools     # このサーバーが公開するツールを一覧する（APIキー不要）
    uv run python -m app.mcp_server --http          # Streamable HTTP で起動する（http://127.0.0.1:8000/mcp）

引数なしで実行すると stdio（標準入出力）で待ち受ける。これは MCP クライアント（app.mcp_agent など）が
サブプロセスとして起動する使い方なので、手で実行すると入力待ちのまま止まって見える。

第3回では tools.py の関数を agent.py に直接登録した。MCP サーバーにすると、同じ関数を
エージェントのプログラム（app/mcp_agent.py）からも、MCP に対応したほかのソフトウェアからも、
共通の手順で使えるようになる。
"""

import argparse
import json
import random

from mcp.server.mcpserver import MCPServer

from app import tools
from scripts.make_sft_dataset import GLOSSARY

# サーバーの名前と説明。クライアントに表示される（設定ファイル側のキー "glossary" とは別物）
server = MCPServer(
    "aie2026-glossary",
    instructions="AIE2026（AIエンジニアリング実践講座）の用語集と各回の要点を提供する。",
)

# 第3回と同じ関数を、そのまま MCP のツールとして公開する。docstring と型ヒントが説明文になる
server.tool()(tools.search_glossary)

@server.tool()
def make_quiz(lecture: int, num_questions: int = 3) -> str:
    """指定された講義回の用語集データをもとに、理解度確認クイズの出題材料を作成します。

    Args:
        lecture: 対象の講義回（1以上の整数。例: 1, 2, 3）
        num_questions: 作成する問題数（1〜5の整数。デフォルトは3）
    """
    # ※既存の search_glossary と同じデータ変数（または読み込み関数）を参照してください
    entries = tools.load_glossary()

    # 1. データ内に実際に存在する講義回の一覧を取得
    valid_lectures = sorted({item["lecture"] for item in entries})

    # 2. 範囲外チェック（存在しない講義回）
    if lecture not in valid_lectures:
        lectures_str = ", ".join(map(str, valid_lectures))
        return (
            f"第{lecture}回のデータは存在しません。"
            f"指定できる講義回は [{lectures_str}] です。"
        )

    # 3. 範囲外チェック（問題数）
    if not (1 <= num_questions <= 5):
        return "問題数（num_questions）は 1〜5 の範囲で指定してください。"

    # 4. 指定された回の用語を抽出してランダムに選定
    targets = [item for item in entries if item["lecture"] == lecture]
    if not targets:
        return f"第{lecture}回に登録されている用語が見つかりませんでした。"

    selected = random.sample(targets, k=min(num_questions, len(targets)))
    lines = [
        f"以下の第{lecture}回の用語データをもとに、{len(selected)}問の4択クイズと解説を作成してください。"
    ]
    for i, item in enumerate(selected, start=1):
        lines.append(f"{i}. 用語: {item['term']} / 定義: {item['definition']}")

    return "\n".join(lines)


# TODO(宿題・基礎): get_lecture_summary も公開しよう
server.tool()(tools.get_lecture_summary)


def main() -> None:
    parser = argparse.ArgumentParser(description="用語集 MCP サーバー")
    parser.add_argument("--http", action="store_true", help="Streamable HTTP で起動する（既定は stdio）")
    args = parser.parse_args()
    if args.http:
        print("MCP サーバーを http://127.0.0.1:8000/mcp で起動します（Ctrl+C で停止）")
        server.run(transport="streamable-http")
    else:
        # stdio では標準出力がプロトコルの通信路になるので、print してはいけない
        server.run()


if __name__ == "__main__":
    main()
