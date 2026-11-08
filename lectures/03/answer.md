# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
```
  ・素のLLM (app.ask): 
  　AIE2026や講座全体の固有情報を直接参照できないため、確実な回答ではないという前提を示したうえで、
  　一般的なAI・プログラミング教育の文脈から答えを推測して回答した。また、正確な確認方法として
  　プラットフォームの案内文を読んだり、運営やメンター、同期の受講生へ質問する等の方法を提示した。

　・エージェント (app.agent): 
　　一方、エージェント側はツール等を通じて正確に「3レベル」の具体的な解説を返した。
```
- `--trace` で見えたツール呼び出し（ツール名と引数）：

```
　　ツール名：search_glossary
　　引数：{'query': 'LoRA'}　および　{'query': 'QLoRA'}
```

```
--- trace ---
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[usage] RunUsage(cost=Decimal('0.0008013'), details={'text_prompt_tokens': 1196}, input_text_tokens=1196, input_tokens=1196, output_tokens=177, requests=2, tool_calls=2)
```


- 1つの質問での LLM 呼び出し回数（`requests`）：　
```
    2回（requests=2）
```

- 追加したツールと、docstring に書いた説明：

　　追加したツール：
```
    make_quiz
```
　　docstring に書いた説明：
  
    指定した回の用語から1つを選び、確認問題と答えを返す。
    「第2回の確認問題を出して」のように、復習用の問題を求められたときに使う。
    

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
