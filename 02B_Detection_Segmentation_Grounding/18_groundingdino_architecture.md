# GroundingDINO 的底层结构和 Phrase → Box 怎么实现？

## 面试一句话

GroundingDINO = **DINO-style detector + text encoder + tight cross-modal fusion**。它不是固定 `num_classes` 分类头，而是让 object queries 与文本 tokens 对齐。

## 主流程

```text
Image
 → multi-scale visual features ─┐
                                ├→ Feature Enhancer
Text
 → text tokens [B,L,C] ─────────┘
            ↓
Language-guided Query Selection
queries [B,Q,C]
            ↓
Cross-Modality Decoder
     ├→ boxes [B,Q,4]
     └→ text alignment [B,Q,L]
```

## 三个核心模块

1. **Feature Enhancer**：增强视觉/文本特征并做跨模态交互。
2. **Language-guided Query Selection**：优先选择与文本相关的视觉 queries。
3. **Cross-Modality Decoder**：query 同时读取图像与文本信息。

因为输出保留 query-to-token/phrase alignment，所以输入可以是 category name，也可以是 referring expression。

## Primary sources

- https://arxiv.org/abs/2303.05499
- https://github.com/IDEA-Research/GroundingDINO
