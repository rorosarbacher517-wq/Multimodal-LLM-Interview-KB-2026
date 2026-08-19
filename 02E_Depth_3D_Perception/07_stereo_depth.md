# Stereo：Disparity 如何变成 Depth

## 面试一句话

双目深度通过左右图中同一三维点的视差恢复距离：视差越大，物体越近。

## Rectified Stereo

校正后对应点主要沿同一水平线搜索。

`Z = fB/d`

## 典型 Pipeline

```text
left/right images
→ feature extraction
→ correlation / cost volume
→ disparity estimation
→ depth
```

## 为什么远处更难

远处 `d` 很小，1 pixel 的视差误差会导致很大的 depth error。

## 单目 vs 双目

双目有真实几何尺度来源；单目更多依赖 learned priors。