# Object Tracking、Point Tracking、Optical Flow 区别

## Object Tracking

输出 object box/mask + identity：

`[T,N,box/mask,id]`

## Point Tracking

给定一组 query points，输出每个点跨帧坐标：

`[B,T,N,2] + visibility`

## Optical Flow

预测相邻帧大范围像素位移场：

`[B,2,H,W]`

## 关系

- MOT 更关注语义对象和 identity；
- point tracking 更关注长期几何对应；
- flow 更偏局部 dense motion。

3D reconstruction、robotics、video editing 往往更需要 point tracks。