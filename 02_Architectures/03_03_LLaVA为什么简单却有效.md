# 03_LLaVA为什么简单却有效

## 面试一句话

LLaVA 证明了强视觉编码器 + 简单 projector + 指令数据，就能把 LLM 快速变成视觉对话模型。

## 核心回答

- 视觉编码器提取 patch features。
- 线性层或 MLP 把视觉 hidden size 映射到 LLM hidden size。
- 视觉 token 与文本 token 拼接后做自回归训练。
- 它的重要意义是把多模态对齐问题简化成了可规模化的数据与指令微调问题。

## 参考

- https://arxiv.org/abs/2304.08485
