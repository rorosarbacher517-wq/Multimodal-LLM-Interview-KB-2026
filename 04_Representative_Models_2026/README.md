# 04 · Representative Multimodal Models — 2026-08-19

> 本节不背排行榜，只抓每个模型**真正值得面试的结构、训练和系统思想**。
>
> 规则：只写论文、官方 GitHub、官方 model card 能确认的内容；未公开的 vision encoder / projector / loss 明确写“未公开”。

---

## Q1. Flamingo → BLIP-2 → LLaVA 的架构演进主线？
- Flamingo：Resampler + gated cross-attention。
- BLIP-2：Q-Former 在冻结视觉塔与冻结 LLM 之间做信息瓶颈。
- LLaVA：强 vision encoder + 简单 projector + LLM，强调 instruction data。

核心趋势不是 adaptor 越来越复杂，而是**backbone/data 变强后 connector 可以更简单，视觉 token 与分辨率成为新瓶颈**。

## Q2. Qwen2.5-VL 为什么仍值得掌握？
重点是动态分辨率、空间/时间位置编码，以及 OCR、grounding、video、agent 任务的统一训练。它是理解 Qwen3-VL 的直接前置。

Primary: https://arxiv.org/abs/2502.13923

## Q3. Qwen3-VL 最核心的公开升级？
公开技术报告强调：
1. **Interleaved-MRoPE**；
2. **DeepStack** 多层视觉特征；
3. text-based timestamp alignment；
4. dense/MoE 与长 interleaved multimodal context。

Primary: https://arxiv.org/abs/2511.21631

## Q4. DeepStack 为什么有意义？
最后一层 ViT 更偏抽象语义，中间层通常保留更多局部/空间细节。多层特征能改善 OCR、grounding、fine-grained perception，但增加 feature bandwidth 和融合复杂度。

## Q5. Qwen3.5 为什么是一个重要转折？
Qwen 官方把 Qwen3.5 描述为 **Unified Vision-Language Foundation**，强调 early fusion 的大规模多模态训练，并公开：
- Gated Delta Networks + sparse MoE hybrid architecture；
- scalable RL；
- multimodal/agent capability 统一。

Primary: https://github.com/QwenLM/Qwen3.8

## Q6. Qwen3.6 应该怎么准确回答？
官方说明 Qwen3.6 建立在 Qwen3.5 的基础上，重点强化 **agentic coding、thinking preservation 和实际稳定性**。

不要把“继承 Qwen3.5 foundation”进一步推断成每个 Qwen3.6 checkpoint 都公开了新的视觉塔结构；具体模态支持与内部细节要看对应 model card。

Primary: https://github.com/QwenLM/Qwen3.8

## Q7. 截至 2026-08-19，Qwen3.8 的定位是什么？
Qwen3.8 是 Qwen3.5 open-model series 当前最新公开线路。官方仓库说明它**built on the architectural foundation of Qwen3.5**，重点提升 coding、professional work、research、long-horizon agentic tasks 与 agent execution。

2026-08-12 发布 Qwen3.8-2.4T-A95B，2026-08-14 发布 Qwen3.8-27B。面试时不应凭“3.8”名称自行补写新的 vision encoder/projector；模态与实现按具体 model card 核对。

Primary: https://github.com/QwenLM/Qwen3.8

## Q8. InternVL 系列的经典结构思路？
- 强视觉 backbone；
- dynamic tiling / high resolution；
- MLP/projector 接入 LLM；
- OCR、document、multi-image、video 共同训练。

特点是一直重视**高分辨率感知与 LLM token/compute 的平衡**。

## Q9. InternVL3.5 的三个面试重点？
1. Cascade RL；
2. Visual Resolution Router (ViR)；
3. Decoupled Vision-Language Deployment (DvD)。

说明现代 MLLM 创新已经同时覆盖 model、post-training 和 serving。

Primary: https://arxiv.org/abs/2508.18265

## Q10. ViR 为什么不是普通 Resize？
它要做的是 adaptive compute：根据视觉输入/任务动态分配 resolution/token budget，而不是固定规则把所有图缩成同样大小。

## Q11. InternVL-U 为什么需要加入 2026 知识图？
InternVL-U 是公开的 unified multimodal 方向：约 4B 参数，覆盖**understanding、reasoning、image generation、image editing**，把 MLLM 与 MMDiT-style generation head 放入同一系统。

它代表 MLLM 从“只理解多模态”继续走向“理解 + 生成统一”。

Primary: https://arxiv.org/abs/2603.09877

## Q12. GLM-4.5V / GLM-4.6V 的重点？
GLM-V 路线强调 multimodal reasoning + RL + agent。公开线路进一步支持长 context 与 multimodal function calling。

具体 checkpoint 的内部 vision 结构按官方 repo/model card，不从产品能力反推未公开架构。

Primary: https://github.com/zai-org/GLM-V

## Q13. GLM-5V-Turbo 为什么值得关注？
公开技术报告把目标推进到 **native multimodal agent**：视觉感知直接参与 reasoning、planning、tool use、execution。

面试框架：`perceive → reason → act → verify`。

Primary: https://arxiv.org/abs/2604.26752

## Q14. Seed1.5-VL 的公开结构与定位？
公开报告给出 532M vision encoder + MoE LLM（20B active parameters），覆盖 OCR、diagram、grounding、3D spatial understanding、video、GUI/game agent，并系统讨论 data/model/training。

Primary: https://arxiv.org/abs/2505.07062

## Q15. Kimi-VL 的核心亮点？
- 高效 MoE language decoder，约 2.8B active；
- MoonViT 面向 native-resolution visual encoding；
- long context；
- Thinking 版本结合 long-CoT SFT + RL。

Primary: https://arxiv.org/abs/2504.07491

## Q16. MiniCPM-V 4.6 为什么代表端侧路线？
官方公开版本采用 SigLIP2-400M + Qwen3.5-0.8B，约 1.3B，并强调 mixed `4×/16×` visual-token compression 与端侧部署。

面试重点：**压 visual tokens 同时降低 LLM prefill、内存和端侧延迟**。

Primary: https://github.com/OpenBMB/MiniCPM-V

## Q17. MiniCPM-o 4.5 的 Full-Duplex 是什么？
输入 audio/video 与输出 speech/text 可以持续并行流动，需要处理 turn-taking、interruption、streaming cache 和模态同步。

Primary: https://github.com/OpenBMB/MiniCPM-V

## Q18. Qwen3-Omni 的 Thinker–Talker 怎么理解？
公开架构采用 MoE-based Thinker–Talker：
- Thinker：multimodal understanding/reasoning；
- Talker：streaming speech generation；
- multi-codebook 用于 speech representation/generation。

Primary: https://github.com/QwenLM/Qwen3-Omni

## Q19. Llama 4 多模态 + MoE 怎么讲？
Meta 公开把 Scout/Maverick 描述为 natively multimodal MoE。面试重点：
- native multimodal training；
- total vs active parameters；
- long-context multimodal serving 的 capacity/efficiency trade-off。

Primary: https://ai.meta.com/blog/llama-4-multimodal-intelligence/

## Q20. Gemma 3 代表什么设计取向？
轻量开放 VLM + 长 context efficiency：SigLIP vision encoder，并通过 local/global attention 等设计控制长上下文成本。

Primary: https://arxiv.org/abs/2503.19786

## Q21. Janus-Pro 为什么解耦 Understanding / Generation 表示？
理解需要判别性语义表示；生成需要高保真可重建表示。Janus 路线说明：**统一 Transformer 不等于所有任务必须共享完全相同的视觉 encoder**。

Primary: https://arxiv.org/abs/2501.17811

## Q22. STEP3-VL-10B 代表什么趋势？
报告强调 fully-unfrozen multimodal pretraining、大规模 RL 与 PaCoRe test-time perceptual reasoning。

趋势：能力扩展同时来自 **pretraining + post-training + inference-time compute**。

Primary: https://arxiv.org/abs/2601.09668

---

## 闭源模型统一回答原则
GPT / Gemini / Claude 等，如果官方没公开 vision encoder、projector、loss、training mixture：

> 可以讨论官方公开的输入输出模态、context、工具和产品能力；内部结构明确标注“not publicly disclosed”。

这比用开源 VLM 架构去猜闭源模型专业得多。
