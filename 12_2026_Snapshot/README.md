# 12 · 2026-08 技术快照

本页只记录**截至 2026-08 可由官方文档/论文确认**、且面试价值较高的变化。

## 1. Qwen3-VL
- Dense + MoE、Instruct + Thinking。
- 公开架构更新包括 **Interleaved-MRoPE、DeepStack、Text–Timestamp Alignment**。
- 重点：高分辨率视觉、长视频、空间/时间理解、agent interaction。
- Source: https://github.com/QwenLM/Qwen3-VL

## 2. Qwen3-Omni
- 原生处理 text / image / audio / video，并可实时生成 speech。
- 公开采用 MoE-based **Thinker–Talker** 架构与多 codebook 语音设计。
- Source: https://github.com/QwenLM/Qwen3-Omni

## 3. InternVL3.5
- **Visual Resolution Router (ViR)**：动态控制视觉分辨率/token。
- **Cascade RL**：离线 RL + 在线 RL。
- **DvD**：视觉编码器与 LLM 解耦部署。
- Source: https://arxiv.org/abs/2508.18265

## 4. Llama 4
- Meta 首批 natively multimodal、MoE 的 Llama 系列。
- Scout / Maverick 都强调 active parameters 与 total parameters 的区别。
- Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/

## 5. Gemma 3
- SigLIP vision encoder。
- 长上下文通过更高 local:global attention 比例降低 KV-cache 压力。
- Source: https://arxiv.org/abs/2503.19786

## 6. Multimodal serving
- vLLM 已覆盖 text/image/video/audio 多模态输入，并持续扩展多模态缓存、LoRA 和 disaggregated serving。
- Source: https://docs.vllm.ai/en/latest/features/multimodal_inputs/

## 7. Training system
- PyTorch 推荐新项目使用 **FSDP2 / fully_shard** 路线。
- Source: https://docs.pytorch.org/docs/main/distributed.fsdp.fully_shard.html

## 8. Attention kernel
- FlashAttention-4（2026）面向 Blackwell 的异步 pipeline 与内存/softmax 协同设计。
- Source: https://arxiv.org/abs/2603.05451

## 9. 闭源模型
- 只记录官方公开的 modality、context、tool/API capability。
- **不把未披露的 vision encoder、projector、训练配方当成事实。**
- OpenAI official models page: https://developers.openai.com/api/docs/models
