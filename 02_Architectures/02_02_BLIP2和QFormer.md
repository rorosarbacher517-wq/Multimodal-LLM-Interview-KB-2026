# 02_BLIP2和QFormer

## 面试一句话

BLIP-2 的核心是 Q-Former：用少量 learnable queries 从冻结视觉编码器中抽取和语言相关的视觉信息。

## 核心回答

- 第一阶段做 image-text representation learning，第二阶段把 Q-Former 输出接到冻结 LLM。
- 固定 query 数能把大量视觉 patch 压成较短序列。
- 面试重点：Q-Former 不是简单 MLP，而是带 self-attention/cross-attention 的可学习信息瓶颈。

## 参考

- https://arxiv.org/abs/2301.12597
