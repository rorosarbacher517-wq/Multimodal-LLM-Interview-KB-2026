# 2025–2026 Point Cloud Foundation：Sonata / Concerto / Utonia

## 面试一句话

点云方向也在从“每个任务一个 backbone”走向通用 pretrained encoder。

## Pointcept 路线

截至 2026，官方 Pointcept 仓库持续维护：

- **Sonata**：2025 point cloud self-supervised foundation representation；
- **Concerto**：联合 2D–3D self-supervised learning；
- **Utonia**：2026 面向“one encoder for all point clouds”的统一 encoder 方向。

## 为什么 2D–3D 联合训练有价值

图像提供纹理/语义，点云提供真实几何；跨模态一致性可以增强 spatial representation。

## 面试意义

这是 3D perception 与 MLLM/VLA 接轨的重要桥梁：统一 3D encoder 比只训练单个 segmentation detector 更容易复用。

## Primary source

- https://github.com/Pointcept/Pointcept