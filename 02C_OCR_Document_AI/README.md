# 02C · OCR / Document AI

> 这一模块放在 Detection/Segmentation/Grounding 之后、MLLM Core Architecture 之前。
>
> 核心链路：**文字检测 → 文字识别 → OCR spotting → layout → table/formula/chart → document parsing → Document VLM → Document RAG**。

## 推荐学习顺序

**OCR 基础 → Detection/Recognition → Layout → OCR-free / VLM → 2026 Document AI → 数据与评测 → RAG**

## 问题目录

1. [OCR、Text Spotting、Document Parsing 有什么区别](./01_ocr_spotting_document_parsing.md)
2. [Text Detection：DBNet 为什么常用](./02_text_detection_dbnet.md)
3. [CRNN + CTC：经典文字识别链路](./03_crnn_ctc.md)
4. [TrOCR / PARSeq：Transformer OCR 怎么做](./04_transformer_ocr.md)
5. [Layout Analysis 与 Reading Order](./05_layout_reading_order.md)
6. [LayoutLMv3：文本、版面和图像怎么融合](./06_layoutlmv3.md)
7. [Donut：为什么可以 OCR-free](./07_donut_ocr_free.md)
8. [表格、公式、图表为什么不能只做普通 OCR](./08_table_formula_chart.md)
9. [GOT-OCR2.0：Unified OCR 模型](./09_got_ocr2.md)
10. [PaddleOCR 3.x：PP-OCRv6 / PP-StructureV3](./10_paddleocr3.md)
11. [PaddleOCR-VL-1.6：2026 文档解析路线](./11_paddleocr_vl_16.md)
12. [MinerU2.5 / MinerU2.5-Pro：Coarse-to-Fine Document Parsing](./12_mineru25_pro.md)
13. [OCR / Document 数据怎么生产和清洗](./13_document_data_engineering.md)
14. [Document AI 怎么评测和诊断错误](./14_document_evaluation.md)
15. [Document Parsing 如何接 Multimodal RAG](./15_document_rag.md)

## 一张图理解 Document AI

```text
PDF / Document Image
        ↓
Orientation / Dewarp / Layout Detection
        ↓
┌─────────────┬──────────────┬──────────────┐
│ Text Region │ Table/Chart  │ Formula/Image│
└─────────────┴──────────────┴──────────────┘
        ↓
OCR / VLM Recognition
        ↓
Reading Order + Structure Recovery
        ↓
Markdown / HTML / JSON
        ↓
Chunking + Metadata + Embedding
        ↓
Document RAG / Agent
```

## 2026 要特别掌握

- PaddleOCR-VL-1.6：layout analysis + VLM recognition；
- MinerU2.5 / Pro：coarse-to-fine high-resolution parsing、data engine；
- OCR 已经从“字符识别”扩展到 **结构恢复 + 多模态内容解析 + LLM-ready output**。

## Primary sources

- PaddleOCR: https://github.com/PaddlePaddle/PaddleOCR
- PaddleOCR-VL: https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md
- MinerU: https://github.com/opendatalab/MinerU
- MinerU2.5: https://arxiv.org/abs/2509.22186
- GOT-OCR2.0: https://github.com/Ucas-HaoranWei/GOT-OCR2.0
- LayoutLMv3: https://arxiv.org/abs/2204.08387
