# Document Parsing 如何接 Multimodal RAG

## 面试一句话

Document RAG 的第一步不是 embedding，而是先把 PDF 解析成“可检索但不丢结构”的中间表示。

## 推荐 Pipeline

```text
PDF
→ document parser
→ blocks: text/table/figure/formula
→ keep page + bbox + hierarchy
→ semantic chunking
→ text/image embeddings
→ retrieval
→ rerank
→ send original page/crop + text evidence to MLLM
```

## 为什么保留 bbox/page_id

检索到文本后，可以回到原始页 crop 做视觉验证，减少 OCR 错误和上下文缺失。

## 表格怎么办

同时保存：

- HTML/Markdown structure；
- cell-level text；
- page image crop；
- table caption/metadata。

## 关键评测

要拆开 **retrieval recall** 和 **answer correctness**，否则无法知道是没召回还是模型没答对。