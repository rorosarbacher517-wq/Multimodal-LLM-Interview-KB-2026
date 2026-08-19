# 截至 2026-08，YOLO26 最值得掌握什么？

## 面试一句话

YOLO26 把 Ultralytics 路线推进到**默认端到端 NMS-free + DFL-free regression**，同时继续统一多任务与边缘部署。

## 核心回答

- 默认 end-to-end one-to-one detection head，推理无需 NMS。
- 官方配置 `reg_max=1`，即移除传统 DFL 分布回归路径。
- 训练配方公开包含 **Progressive Loss、STAL、MuSGD**。
- 支持 detect / instance segment / semantic segment / depth / classify / pose / OBB。
- **YOLOE-26** 将同一高效路线扩展到 open-vocabulary detection/segmentation。

## 为什么值得面试准备？

因为它把传统 CV 中的“实时 detector”与 2026 的三个趋势连接起来：**end-to-end、open-vocabulary、unified deployment**。

## Primary sources

- https://docs.ultralytics.com/models/yolo26
- https://arxiv.org/abs/2606.03748
