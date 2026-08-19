# YOLO-World、YOLOE、GroundingDINO 都是开放词汇，它们有什么区别？

## 面试一句话

它们都把语言引入检测，但 YOLO-World / YOLOE 更强调实时 YOLO 路线；GroundingDINO 更强调 phrase-level grounding 和 Transformer detector 的跨模态融合。

## YOLO-World

- 核心模块是 **RepVL-PAN**。
- 使用 region-text contrastive learning。
- 目标是把开放词汇能力放进实时 YOLO detector。

## YOLOE

- 支持 **text prompt / visual prompt / prompt-free**。
- 文本路线有 RepRTA，视觉 prompt 有 SAVPE，prompt-free 有 LRPC。
- 同时覆盖 detection + segmentation。
- YOLOE-26 进一步继承 YOLO26 的 NMS-free 路线。

## GroundingDINO

- 更强调 natural-language phrase → object query → box 的精确对齐。
- 对复杂 referring expression / auto-labeling 很有价值。

## Primary sources

- https://arxiv.org/abs/2401.17270
- https://arxiv.org/abs/2503.07465
- https://arxiv.org/abs/2303.05499
