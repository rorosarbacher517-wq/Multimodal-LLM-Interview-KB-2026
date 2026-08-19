# Sparse Conv / Point Transformer v3

## Sparse Convolution

只在非空 voxel 上计算卷积，避免 3D dense grid 的巨大浪费。

## Point Transformer

直接在点/局部邻域上做 attention，更自然地处理不规则点集。

## PTv3 的核心理解

Point Transformer V3 重点不是“把普通 Transformer 原样搬到点云”，而是通过序列化/邻域组织提高可扩展性，使点云 attention 能处理更大的场景。

## 面试对比

- Sparse Conv：规则 voxel + 高效局部算子；
- Point Transformer：point-centric + attention；
- 真实系统经常根据场景规模和硬件折中。

## Reference

- Pointcept/PTv3: https://github.com/Pointcept/Pointcept