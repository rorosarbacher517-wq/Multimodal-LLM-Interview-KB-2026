# RT-DETR 为什么能把 DETR 做到实时？

## 面试一句话

RT-DETR 通过更高效的 multi-scale encoder 和更好的 query initialization，保留 DETR 的端到端 NMS-free 优势，同时显著降低实时检测成本。

## 核心设计

- **Efficient Hybrid Encoder**：把 intra-scale interaction 和 cross-scale fusion 解耦。
- **Uncertainty-minimal Query Selection**：从 encoder features 中选择质量更高的初始 queries。
- Decoder layer 数可以在推理时调整，用于速度/精度 trade-off。
- RT-DETRv2 进一步优化 deformable sampling、数据增强和部署友好性。

## 与 YOLO 的区别

YOLO 传统上是 dense convolutional detection；RT-DETR 是 query-based set prediction。现在两条路线都在追求实时和 NMS-free。

## Primary sources

- https://arxiv.org/abs/2304.08069
- https://arxiv.org/abs/2407.17140
