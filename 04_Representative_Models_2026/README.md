# 04 · Representative Multimodal Models — 2026-08

> 本节不背排行榜，只抓每个模型**真正值得面试的结构/训练思想**。对未公开细节明确写“未公开”。

## Q1. 从 Flamingo、BLIP-2 到 LLaVA，架构演进主线是什么？

- Flamingo：视觉 Resampler + 插入 LLM 的 gated cross-attention。
- BLIP-2：Q-Former 作为冻结 vision encoder 与冻结 LLM 的信息瓶颈。
- LLaVA：强 vision encoder + 简单 MLP projector + LLM，突出数据规模和指令微调。

演进并不是“模块越来越复杂”，而是**视觉 backbone 变强、数据变大后，连接器可以更简单，同时 token/分辨率问题变成新瓶颈。**

## Q2. Qwen2.5-VL 为什么值得掌握？

重点不是参数量，而是三件事：

- 动态分辨率，让不同尺寸图像保留更多原始信息；
- 多模态位置编码，处理图像和视频的空间/时间位置；
- OCR、grounding、文档、视频、视觉 agent 等能力一起进入统一 VLM。

它是理解 Qwen3-VL 后续升级的直接基础。

## Q3. Qwen3-VL 最核心的架构升级是什么？

公开技术报告强调：

1. **Interleaved-MRoPE**：更强的空间-时间位置建模；
2. **DeepStack**：利用 ViT 多层视觉特征，而不是只用最后一层；
3. **Text-based timestamp alignment**：用显式文本时间对齐强化视频 temporal grounding；
4. Dense 与 MoE 多种规模，原生支持长的 interleaved multimodal context。

来源：[Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)

## Q4. DeepStack 为什么能改善视觉能力？

ViT 最后一层更抽象，中间层保留更细的局部和空间信息。DeepStack 把多层视觉表征更直接地送入语言侧，使模型在 OCR、空间定位、图表、细粒度识别时不完全依赖高度抽象的最后一层特征。

面试要点：**多层特征融合提高信息保真度，但也增加特征传输和融合设计复杂度。**

## Q5. Qwen3.5 为什么是一个重要转折？

Qwen 官方把 Qwen3.5 描述为 **Unified Vision-Language Foundation**：不再只是“文本 LLM + 外挂 VLM”，而是在大规模多模态 token 上做更早、更统一的 multimodal training。

公开特点还包括：

- Gated Delta Networks + sparse MoE 的 hybrid architecture；
- 大规模 agent/RL training；
- 视觉、推理、coding、agent 一体化。

来源：[Qwen3.6 / Qwen3.5 official repository](https://github.com/QwenLM/Qwen3.6)

## Q6. Qwen3.6 截至 2026-08 应该怎么回答？

官方把 Qwen3.6 定位为 Qwen3.5 基础上的稳定性和实际 agentic coding 升级，公开强调 agentic coding、thinking preservation 等能力。

**不要**因为它继承 Qwen3.5 就自己补写未公开的视觉内部层数、projector 或视觉 loss。面试时可以说：

> “官方确认它延续 native multimodal foundation 路线，但具体视觉内部设计应以公开 model card / code 为准，未披露部分不能推测。”

来源：[Qwen3.6 official repository](https://github.com/QwenLM/Qwen3.6)

## Q7. InternVL 系列的经典结构思路是什么？

InternVL 长期强调：

- 强视觉 backbone；
- 动态切图/高分辨率输入；
- 通过 MLP/projector 接入 LLM；
- 多图、视频、OCR、文档能力共同训练。

其特点是非常重视**高分辨率感知能力与大模型推理能力之间的工程折中。**

## Q8. InternVL3.5 的三项面试重点？

1. **Cascade RL**：offline RL → online RL，分阶段增强 reasoning；
2. **Visual Resolution Router (ViR)**：按输入动态调整视觉分辨率/token；
3. **Decoupled Vision-Language Deployment (DvD)**：视觉 encoder 与 LLM 分到不同 GPU，改善负载平衡。

这说明现代 MLLM 的“架构创新”已经同时覆盖模型、RL 和 serving。

来源：[InternVL3.5](https://arxiv.org/abs/2508.18265)

## Q9. ViR 为什么不是简单 resize？

固定 resize 不考虑任务信息需求。Resolution Router 试图根据输入决定视觉计算预算：简单图像少 token，复杂文档/高细节图像多 token。

本质是 **adaptive compute**：让模型在准确率、视觉 token 数、prefill latency 之间动态取舍。

## Q10. GLM-4.5V / GLM-4.6V 的重点是什么？

GLM-V 路线强调 multimodal reasoning + RL + agent：

- GLM-4.5V 延续 reasoning-centric VLM training；
- GLM-4.6V 扩展到 128K context，并公开强调 **native multimodal function calling**；
- 视觉输入/输出可以直接进入工具调用链，而不是先全部转文字。

来源：[GLM-V official repository](https://github.com/zai-org/GLM-V)

## Q11. GLM-5V-Turbo 为什么值得 2026 面试关注？

它明确把目标从“VLM 能看懂图”推进到 **native multimodal agent foundation model**：视觉感知直接参与 reasoning、planning、tool use 和 execution。

面试价值：理解未来多模态模型的评价标准不只是 VQA，而是完整的 **perceive → reason → act → verify**。

来源：[GLM-5V-Turbo Technical Report](https://arxiv.org/abs/2604.26752)

## Q12. Seed1.5-VL 的结构和定位？

公开报告：

- 532M vision encoder；
- MoE LLM，20B active parameters；
- 覆盖 OCR、diagram、grounding、3D spatial understanding、video、GUI/game agent；
- 强调从 model design、data construction 到多阶段 training 的完整经验。

对数据策略/模型数据工程岗位尤其值得读。

来源：[ByteDance Seed1.5-VL](https://github.com/ByteDance-Seed/Seed1.5-VL)

## Q13. Kimi-VL 的核心亮点？

Kimi-VL 是高效 MoE VLM：

- language decoder 只激活约 2.8B parameters；
- MoonViT 强调 native-resolution visual encoding；
- 128K long context；
- Kimi-VL-Thinking 通过 long-CoT SFT + RL 强化视觉推理。

它适合回答“**小 active parameter 如何同时做高分辨率、长上下文和 reasoning**”。

来源：[Kimi-VL Technical Report](https://arxiv.org/abs/2504.07491)

## Q14. MiniCPM-V 4.6 为什么代表端侧路线？

截至 2026-08，官方公开的 MiniCPM-V 4.6：

- 基于 SigLIP2-400M + Qwen3.5-0.8B；
- 约 1.3B 级别；
- 引入 **mixed 4x/16x visual-token compression**；
- 明确面向 iOS / Android / HarmonyOS 等端侧部署。

面试重点：**token compression 不只是省 LLM FLOPs，还能直接影响端侧内存和延迟。**

来源：[MiniCPM-V official repository](https://github.com/OpenBMB/MiniCPM-V)

## Q15. MiniCPM-o 4.5 的 full-duplex 是什么？

全双工意味着：输入视频/音频流与输出文本/语音流可以同时进行，用户不必“说完一句→模型再开始说”。

系统要同时解决：

- streaming encoder；
- turn-taking / interruption；
- 音视频同步；
- 低延迟 speech generation；
- 状态持续更新。

来源：[MiniCPM-V / MiniCPM-o official repository](https://github.com/OpenBMB/MiniCPM-V)

## Q16. Qwen3-Omni 的 Thinker–Talker 怎么理解？

公开架构用 MoE-based **Thinker–Talker**：

- Thinker：多模态理解、语义推理；
- Talker：面向流式语音生成；
- multi-codebook 设计用于高效语音生成；
- 支持 text/image/audio/video 输入和实时 text/speech 输出。

来源：[Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni)

## Q17. Llama 4 的多模态 + MoE 面试怎么讲？

Meta 公开将 Llama 4 Scout/Maverick 描述为 natively multimodal MoE 系列。回答重点：

- 多模态从训练中原生加入，而不是推理时外挂；
- MoE 要区分 total / active params；
- 超长上下文和多模态 token 使 capacity 与 serving efficiency 同时成为核心问题。

来源：[Meta Llama 4 official announcement](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

## Q18. Gemma 3 代表什么设计取向？

Gemma 3 是“轻量开放 VLM + 长上下文效率”路线：

- SigLIP vision encoder；
- 视觉能力覆盖多种尺寸；
- 通过 local/global attention 配比降低长 context 的 KV/cache 成本；
- 适合讨论单卡/边缘场景的质量-效率折中。

来源：[Gemma 3 Technical Report](https://arxiv.org/abs/2503.19786)

## Q19. Janus-Pro 为什么把理解和生成视觉编码解耦？

视觉理解需要语义判别表征；图像生成需要适合重建/生成的视觉表示。强行共享同一编码器可能产生目标冲突。

Janus 路线的启示：**统一模型不等于所有任务必须共享完全相同的视觉表征。**

来源：[Janus-Pro](https://arxiv.org/abs/2501.17811)

## Q20. STEP3-VL-10B 带来的 2026 新趋势是什么？

其报告强调：

- fully unfrozen multimodal pretraining；
- 大规模 RL post-training；
- Parallel Coordinated Reasoning（PaCoRe）用于 test-time compute scaling。

这代表趋势从“训练一个更大 VLM”进一步走向 **训练阶段 + RL + test-time perceptual reasoning 共同扩展能力**。

来源：[STEP3-VL-10B](https://arxiv.org/abs/2601.09668)

---

### 闭源模型统一回答原则

GPT、Gemini、Claude 等如果官方没公开 vision encoder / projector / loss：

> 可以说公开的输入输出模态、context、工具和产品能力；内部结构明确标注“官方未披露”。

这比编一个“可能用了 CLIP/SigLIP”专业得多。