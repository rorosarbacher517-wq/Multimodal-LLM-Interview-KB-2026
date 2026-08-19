# Video Depth Anything / Prompt Depth Anything

## Video Depth Anything

单帧 depth 容易在视频中闪烁。Video Depth Anything 重点解决 **temporal consistency**，让长视频深度在时间上更稳定。

## Prompt Depth Anything

用低分辨率 sparse/metric depth（例如 LiDAR）作为 prompt，引导高分辨率图像得到 metric depth。

```text
RGB high-res + sparse/low-res metric depth
→ prompted depth model
→ high-res metric depth
```

## 面试价值

它展示了 foundation model 的两种扩展：

- 单帧 → temporal；
- purely learned prior → sensor-guided metric geometry。

## Reference

- https://github.com/DepthAnything/Depth-Anything-V2