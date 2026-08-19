# Open-Vocabulary Segmentation 是什么？

Closed-set segmentation 只能预测训练时固定类别；open-vocabulary segmentation 希望根据 text prompt 或开放语义 embedding 分割新概念。

常见思路：
```text
image dense features
+ text embeddings / grounding boxes
→ class-aware masks
```

GroundingDINO + SAM 是模块化路线：text → box → mask；其他模型则把语言条件直接融入 segmentation network。
