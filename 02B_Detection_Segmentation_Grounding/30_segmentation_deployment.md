# Segmentation 部署怎么做取舍？

主要成本来自：
- input resolution；
- backbone；
- dense decoder；
- mask 数量；
- video temporal propagation。

## 常见优化
- resize / tile；
- lightweight backbone；
- prototype mask / low-resolution mask + upsample；
- detector 先找 ROI，再局部分割；
- video 中复用 memory/track，而不是每帧重新全图 heavy segmentation。

面试应同时谈 mask quality、latency、memory 和目标大小分布。
