# YOLOv9 的 PGI 和 GELAN 是什么？

## 面试一句话

YOLOv9 的核心不是简单换一个 backbone，而是用 **GELAN** 改善特征/梯度路径，并用 **PGI** 在训练中提供更可靠的梯度信息。

## 核心回答

- **GELAN** = Generalized Efficient Layer Aggregation Network，强调高效的层聚合和参数利用。
- **PGI** = Programmable Gradient Information，目标是缓解深层网络信息损失对训练信号的影响。
- PGI 中部分辅助结构服务于训练，不意味着推理路径必须同样复杂。
- YOLOv9 来自 WongKinYiu 团队，不要把 YOLOv8→v9→v10→11 当成同一个官方代码线连续升级。

## Primary sources

- https://arxiv.org/abs/2402.13616
- https://github.com/WongKinYiu/yolov9
