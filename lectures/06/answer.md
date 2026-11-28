# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：
  - `app.agent`：`search_materials`
  - `app.mcp_agent`：`glossary_search_glossary`
- STEP 2 の [tool call]：
　- `glossary_search_glossary({'query': '3レベル'})`
- STEP 3 の [tool call]：
  -`fetch_fetch({'url': 'https://modelcontextprotocol.io/'})` 
- STEP 4 の [tool call]：
  -`aws_aws___search_documentation({'search_phrase': 'Amazon S3 versioning overview'})` 
- 気づき・疑問：
エージェント側のPythonコードを一切変更せず、設定ファイル（mcp_servers.json）に数行追記するだけで、①自分で作った用語集サーバーから②公開されているfetchサーバー、③外部で動くAWSサーバーまで同じ仕組みで追加できることに驚いた。一方で、サーバー数が増えるとすべてのツールの説明文が毎回モデルに送られるためトークン消費の増加や、外部サーバーを利用する際のセキュリティ面について疑問を持った。
## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
