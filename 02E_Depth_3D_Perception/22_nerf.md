# NeRF 是什么？

NeRF 用神经网络表示连续 3D radiance field：输入空间位置和视角，输出 density 与 color，再通过 volume rendering 合成新视角。

```text
(x,y,z, view_direction)
→ MLP / field
→ density + color
→ volume rendering
→ image
```

优势是新视角质量高；经典 NeRF 训练/渲染慢，也依赖较好的相机姿态。
