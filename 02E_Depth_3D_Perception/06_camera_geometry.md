# Camera Intrinsics / Extrinsics / Projection

## 面试一句话

Intrinsics 描述相机内部成像；extrinsics 描述世界坐标到相机坐标的位姿变换。

## Projection

```text
X_world [X,Y,Z,1]
→ [R|t]
→ X_camera
→ K
→ homogeneous pixel [u,v,w]
→ divide by w
→ pixel [u/w,v/w]
```

常写成：

`p ~ K [R|t] P`

## Intrinsics K

包含 `fx, fy, cx, cy`，以及在更完整模型中的 skew/distortion 参数。

## Unprojection

已知 pixel `(u,v)`、depth `Z` 和 K：

`X_camera = Z * K^{-1} [u,v,1]^T`

这是把 depth map 转成 point cloud 的核心。