# 00 · 学习路线

这套知识库按“先底层原理，再模型结构，再训练/推理，再系统与业务”组织。

建议顺序：

1. **基础原理**：Transformer、视觉 token、对齐、融合。
2. **经典架构**：Flamingo → BLIP-2 → LLaVA → Qwen-VL / InternVL。
3. **2025–2026 架构演进**：动态分辨率、MLP/Resampler、MoE、DeepStack、MRoPE、Omni。
4. **数据与训练**：预训练、SFT、偏好优化、RL、合成数据。
5. **视觉推理**：perception bottleneck、CoT、RLVR、test-time scaling。
6. **视频/音频**：时间建模、长视频、实时语音。
7. **Agent**：工具调用、GUI、RAG、具身/VLA。
8. **训练与部署**：FSDP2、TP/PP/EP、KV cache、vLLM、量化。
9. **评测与面试**：benchmark、错误诊断、系统设计。

> 原则：能说清“输入是什么 → 中间维度如何变化 → loss 怎么算 → 推理怎么跑 → 为什么这么设计”，基本就能覆盖多数多模态算法面试。
