# GOT-OCR2.0：Unified OCR 模型

## 面试一句话

GOT-OCR2.0 代表“把 OCR 统一成一个生成式视觉语言模型”的路线，覆盖普通文字、数学公式、表格等多种 OCR 输出。

## 核心理解

传统 OCR：

```text
detector → crop → recognizer → task-specific postprocess
```

GOT 风格：

```text
image / region prompt → unified visual encoder + language decoder → text / formula / structured output
```

## 为什么值得面试掌握

它体现 OCR 从多个专用模块向统一生成模型迁移，但真实系统仍可能保留 layout detector 和 crop pipeline，以降低高分辨率成本。

## Reference

- Official: https://github.com/Ucas-HaoranWei/GOT-OCR2.0
- Paper: https://arxiv.org/abs/2409.01704