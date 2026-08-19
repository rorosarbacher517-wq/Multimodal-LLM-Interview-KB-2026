# 01_Flamingo为什么重要

## 面试一句话

Flamingo 代表了“冻结视觉编码器 + 冻结语言模型 + 中间插入跨模态模块”的经典路线。

## 核心回答

- 它用 Perceiver Resampler 把视觉特征压缩成固定数量 token。
- 在语言模型层间插入 gated cross-attention，让文本 token 读取视觉信息。
- 优点是参数高效、少样本能力强；缺点是架构较重，视觉-语言交互依赖额外 cross-attention。

## 参考

- https://arxiv.org/abs/2204.14198
