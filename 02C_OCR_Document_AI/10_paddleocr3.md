# PaddleOCR 3.x：PP-OCRv6 / PP-StructureV3

## 面试一句话

PaddleOCR 3.x 同时保留高效 OCR pipeline 和 VLM document parsing 两条路线，适合解释“专用模型 + 大模型”如何组合落地。

## PP-OCR 系列

典型 pipeline：

```text
orientation → text detection → text recognition → structured text
```

截至 2026，官方文档列出 PP-OCRv6，覆盖多语言和 edge/server 不同模型规模。

## PP-StructureV3

面向复杂文档解析，负责 layout、table、formula、reading order 等结构恢复，并可输出 Markdown/JSON。

## 面试重点

不要认为 VLM 一定替代传统 OCR。对于高吞吐、固定版式和边缘部署，专用 detector/recognizer 仍有明显效率优势。

## Reference

- https://github.com/PaddlePaddle/PaddleOCR