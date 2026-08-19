# LayoutLMv3：文本、版面和图像怎么融合

## 面试一句话

LayoutLMv3 是 Document AI 的经典预训练模型：同时建模 **OCR text、2-D bounding box 和 document image patches**。

## 输入

```text
words + 2D coordinates + image patches
```

模型通过统一的 text/image masking 和 word-patch alignment 学习跨模态文档表示。

## 适合任务

- form understanding
- receipt extraction
- document classification
- DocVQA
- layout analysis

## 与生成式 Document VLM 区别

LayoutLMv3 更像“文档 encoder”，常用于分类/抽取；现代 Document VLM 更倾向直接生成 Markdown、JSON 或回答问题。

## Reference

- https://arxiv.org/abs/2204.08387