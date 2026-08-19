# VGGT-Ω：2026 的动态场景与高效 3D Foundation

## 面试一句话

VGGT-Ω 是 2026 对 VGGT 的扩展：更大规模数据、更低训练内存、支持动态场景，并把 scene information 压入 registers。

## 公开的关键改动

- 单一 dense prediction head + multi-task supervision；
- 去掉昂贵的高分辨率卷积层；
- registers 聚合 scene information；
- register attention 限制跨帧信息交换；
- 大量 unlabeled video self-supervision。

## 为什么值得关注

这说明 3D foundation model 也在面对与 LLM 相似的问题：**scaling、memory、token interaction、self-supervised data**。

论文还展示了这些 scene registers 对 vision-language-action 表示的潜在价值。

## Reference

- https://arxiv.org/abs/2605.15195