# 17 · 2026-08 Multimodal AI Snapshot

> 截止 2026-08，只记录有官方仓库/论文支撑、且对算法面试真正有价值的变化。

## 1. 从“外挂视觉塔”走向 Native Multimodal Foundation

Qwen3.5 官方明确强调 **Unified Vision-Language Foundation** 和早期融合的大规模多模态训练。多模态正在从“在文本 LLM 外加一个 vision adapter”走向 foundation-model 级统一训练。

- Official: https://github.com/QwenLM/Qwen3.6

**面试关键词：** early/native multimodal training、hybrid architecture、agent RL。

## 2. Qwen3-VL：高分辨率 + 多层视觉特征 + 时间对齐

公开技术报告的三个重要升级：

- Interleaved-MRoPE；
- DeepStack；
- text-based timestamp alignment。

同时提供 dense/MoE 多种规模和长 interleaved multimodal context。

- Paper: https://arxiv.org/abs/2511.21631
- Repo: https://github.com/QwenLM/Qwen3-VL

## 3. Qwen3-Omni：从 VLM 走向实时 Omni

Qwen3-Omni 公开采用 MoE-based Thinker–Talker，处理 text/image/audio/video，并支持实时 text/speech 输出。

- Official: https://github.com/QwenLM/Qwen3-Omni

**面试关键词：** streaming、speech codec、多 codebook、turn-taking、modal synchronization。

## 4. InternVL3.5：模型设计开始直接面向 Serving

InternVL3.5 同时提出：

- Cascade RL；
- Visual Resolution Router；
- Decoupled Vision-Language Deployment。

这意味着“视觉分辨率”已经同时是**能力、训练和系统负载**问题。

- Paper: https://arxiv.org/abs/2508.18265

## 5. GLM-4.6V → GLM-5V-Turbo：Native Multimodal Agent

GLM-4.6V 公开强调 native multimodal function calling；GLM-5V-Turbo 进一步把视觉感知直接放入 reasoning、planning、tool use、execution。

- Repo: https://github.com/zai-org/GLM-V
- GLM-5V-Turbo: https://arxiv.org/abs/2604.26752

**面试关键词：** perceive → reason → act → verify。

## 6. MiniCPM-V 4.6：视觉 Token Compression 进入端侧核心

官方公开：SigLIP2-400M + Qwen3.5-0.8B，约 1.3B 级，并使用 mixed 4x/16x visual-token compression，面向手机等本地部署。

- Official: https://github.com/OpenBMB/MiniCPM-V

**趋势：** VLM 轻量化已经不只是 LLM 量化，还包括视觉 token 数和 vision compute。

## 7. MiniCPM-o 4.5：Full-Duplex Real-time Omni

输入音频/视频与输出语音/文本可以同时流动，模型需要边听、边看、边说并处理打断。

- Official: https://github.com/OpenBMB/MiniCPM-V

**面试关键词：** full duplex、streaming cache、interruption、real-time factor。

## 8. Seed1.5-VL：Data / Model / Agent 一体化

公开报告包含 532M vision encoder + 20B active MoE LLM，并覆盖 grounding、3D、video、GUI/game agent。

- Repo: https://github.com/ByteDance-Seed/Seed1.5-VL
- Paper: https://arxiv.org/abs/2505.07062

**面试价值：** 非常适合数据策略、VLM data engineering、agent data 的系统复习。

## 9. Kimi-VL：小 Active Params + Native Resolution + Long Thinking

Kimi-VL-A3B 语言 decoder 激活约 2.8B 参数，MoonViT 面向原生高分辨率；Thinking 版本通过 long-CoT SFT + RL 强化视觉推理。

- Paper: https://arxiv.org/abs/2504.07491
- Repo: https://github.com/MoonshotAI/Kimi-VL

## 10. STEP3-VL-10B：Post-training + Test-time Scaling

报告强调 fully-unfrozen multimodal pretraining、规模化 RL、以及 Parallel Coordinated Reasoning（PaCoRe）扩展 test-time perceptual reasoning。

- Paper: https://arxiv.org/abs/2601.09668

**趋势：** 能力扩展不再只靠参数，开始同时扩展 training compute、RL environment 和 inference-time compute。

## 11. Qwen3-VL Embedding / Reranker：多模态检索成为独立基础能力

2026 的 Qwen3-VL-Embedding / Reranker 把 text、image、document image、video 统一到多模态 retrieval/ranking pipeline。

- Paper: https://arxiv.org/abs/2601.04720

**面试关键词：** bi-encoder recall、cross-encoder rerank、multimodal RAG。

## 12. FlashAttention-4：模型和硬件共同设计

2026 FlashAttention-4 针对 Blackwell GPU 进一步重构 attention pipeline 和数据搬运。

- Paper: https://arxiv.org/abs/2603.05451

**趋势：** 算法工程面试越来越会问 kernel / memory hierarchy，而不只问 Transformer 公式。

## 13. 当前最重要的 8 条技术主线

1. Native multimodal pretraining；
2. Dynamic/native resolution；
3. Visual-token routing/compression；
4. Multimodal reasoning + RLVR；
5. Active perception / visual lookback；
6. Long-video retrieval + temporal grounding；
7. GUI/tool/agent integration；
8. Omni streaming + efficient serving。

## 14. 哪些内容不要编？

对闭源模型：

- vision encoder；
- hidden size；
- projector；
- MoE routing；
- pretraining data composition；
- loss；

如果官方未披露，就明确“unknown / not publicly disclosed”。

**截至 2026，可信地说清楚公开事实，比背一份看似完整但混有猜测的架构表更重要。**