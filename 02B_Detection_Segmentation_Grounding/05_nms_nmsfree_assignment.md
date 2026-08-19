# NMS、NMS-free 与 Label Assignment 怎么串起来理解？

## 面试一句话

传统 dense detector 会对同一 GT 产生多个高分预测，所以推理后需要 NMS；NMS-free detector 则通过 one-to-one supervision 让最终输出本身接近唯一匹配。

## 核心回答

- **NMS**：按 score 排序，高 IoU 的重复框被抑制。
- **One-to-many assignment**：一个 GT 分给多个正样本，训练信号密集，但容易产生重复框。
- **One-to-one assignment**：一个 GT 对应一个最终预测，天然更适合端到端检测。
- DETR 使用 Hungarian matching 做全局一一匹配。
- YOLOv10 使用 consistent dual assignments：训练保留 one-to-many + one-to-one，推理使用 one-to-one。
- YOLO26 默认采用 end-to-end NMS-free 路线。

## Primary sources

- https://arxiv.org/abs/2405.14458
- https://docs.ultralytics.com/models/yolo26
