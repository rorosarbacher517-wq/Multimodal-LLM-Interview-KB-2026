# YOLOv10 为什么能做端到端 NMS-free？

## 面试一句话

YOLOv10 用 **consistent dual assignments** 同时训练 one-to-many 和 one-to-one 分支：前者保证密集监督，后者服务最终端到端推理。

## 核心回答

- One-to-many 分支让每个 GT 获得多个正样本，优化更稳定。
- One-to-one 分支直接对应最终 NMS-free prediction。
- 两条 assignment 保持一致，减少训练目标冲突。
- 推理时只保留 one-to-one 分支，因此不需要传统 NMS。
- 论文还从 efficiency / accuracy 两方面重新设计多个组件，所以 YOLOv10 不只是“YOLO 去掉 NMS”。

## Primary source

- https://arxiv.org/abs/2405.14458
