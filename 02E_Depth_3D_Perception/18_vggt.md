# VGGT：Feed-forward 3D Geometry Foundation

## 面试一句话

VGGT 把多种传统 3D 几何任务统一成一个 feed-forward Transformer：输入一张或多张图，直接预测 camera、depth、point maps 和 3D tracks。

## 输入输出

```text
images [B,T,3,H,W]
→ shared visual tokens
→ global transformer
→ multiple geometry heads
   ├ camera intrinsics/extrinsics
   ├ depth maps
   ├ point maps
   └ 3D point tracks
```

## 为什么是重要变化

传统系统需要 feature matching、SfM、MVS 等多个模块；VGGT 尝试用统一 learned model 直接预测关键几何量。

## 注意

Feed-forward 不等于“完全不需要优化”。实际高精重建仍可以在输出后接 bundle adjustment/COLMAP refinement。

## Reference

- https://github.com/facebookresearch/vggt