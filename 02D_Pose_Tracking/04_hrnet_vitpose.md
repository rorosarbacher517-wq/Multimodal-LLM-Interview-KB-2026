# HRNet / ViTPose：为什么能做强 Pose Backbone

## HRNet

一直保留高分辨率分支，并与低分辨率语义分支反复交换信息，因此适合关键点这类精细定位任务。

## ViTPose

用标准 ViT 做强视觉 backbone，再接简单 pose decoder。它说明大量预训练 + 大 ViT 本身就可以提供很强的姿态表示。

## 面试对比

- HRNet：强调 multi-resolution parallel representation。
- ViTPose：强调 scalable ViT backbone 和预训练。

## Reference

- ViTPose: https://arxiv.org/abs/2204.12484