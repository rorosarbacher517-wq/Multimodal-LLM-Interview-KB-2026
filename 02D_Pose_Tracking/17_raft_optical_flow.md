# RAFT / Optical Flow 基础

Optical flow 为几乎每个像素估计从 frame t 到 t+1 的二维位移：
```text
flow: [B,2,H,W]
```

RAFT 的经典思想是：
1. 提取两帧 feature；
2. 构造 all-pairs correlation；
3. 用 recurrent update block 迭代细化 flow。

它和 object tracking 不同：flow 是 dense motion field，不直接维护 object identity。
