# Depth Anything V2：Foundation Depth

## 面试一句话

Depth Anything V2 的核心价值是用大规模数据与强视觉 encoder 构建更通用的 monocular depth foundation model，并提高细节、鲁棒性和推理效率。

## 结构理解

```text
RGB image
→ DINOv2-style visual encoder
→ multi-scale intermediate features
→ DPT-like depth decoder
→ depth map
```

## 为什么中间层有用

深层 token 偏语义，浅/中层保留局部几何细节；dense prediction 需要两者结合。

## Relative vs Metric

官方同时提供 relative depth 和基于 V2 backbone 的 metric depth 模型，面试时要区分。

## Reference

- https://github.com/DepthAnything/Depth-Anything-V2