# Donut：为什么可以 OCR-free

## 面试一句话

Donut 不把外部 OCR 结果作为输入，而是直接从文档图像生成结构化文本，因此避免了 OCR 错误向下游传播。

## 结构

```text
Document image
→ vision encoder
→ autoregressive text decoder
→ JSON / text sequence
```

## 优点

- pipeline 更简单；
- 不依赖 OCR box/token；
- 可以针对票据、表单等任务直接生成结构化结果。

## 局限

- 高分辨率细字仍然是 perception bottleneck；
- 很长页面会受到视觉 token 和输出 token 成本限制；
- 若只生成答案，可能丢失可验证的空间结构。

## Reference

- Donut: https://arxiv.org/abs/2111.15664