# 07_Llama4为什么是natively_multimodal

## 面试一句话

Llama 4 的公开信息显示其从预训练阶段就做多模态联合建模，并首次在 Llama 系列中引入 MoE。

## 核心回答

- Scout 和 Maverick 都是 multimodal MoE。
- MoE 用 routed experts + shared expert；每个 token 只激活部分专家。
- 其长上下文和多模态设计说明现代 MLLM 的核心矛盾已从“能不能看图”转向“容量、上下文、成本如何同时扩展”。
## 易错点

- 闭源/有限披露部分不要从第三方博客补全成“官方架构”。

## 参考

- https://ai.meta.com/blog/llama-4-multimodal-intelligence/
