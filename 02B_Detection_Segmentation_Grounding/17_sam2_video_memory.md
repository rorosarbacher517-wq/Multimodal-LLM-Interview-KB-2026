# SAM 2 / SAM 2.1 为什么能处理视频？

## 面试一句话

SAM 2 在 promptable segmentation 上加入 **streaming memory**：当前帧视觉特征可以读取过去帧的对象状态，所以一次提示能传播到后续视频帧。

## 结构逻辑

```text
Current frame
  ↓ image encoder
current visual features
  ↓ memory attention ← past memories / object pointers
prompt + current object state
  ↓ SAM-style mask decoder
mask
  ↓ memory encoder
new memory → next frame
```

## 关键点

- Memory Attention 让当前帧读取历史对象信息。
- Memory Encoder 把过去预测 mask 与视觉特征写入 memory。
- 官方实现默认维护有限数量 mask memory，避免无限增长。
- SAM 2.1 是官方 improved checkpoints / developer suite 更新，并开放训练/微调代码。
- 后续 predictor 进一步支持更灵活的多对象视频推理。

## Primary sources

- https://github.com/facebookresearch/sam2
- https://arxiv.org/abs/2408.00714
