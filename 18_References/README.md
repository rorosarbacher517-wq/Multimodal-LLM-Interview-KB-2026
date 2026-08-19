# 18 · Primary References

> 原则：优先原论文、官方 GitHub、官方 framework docs。二手博客只用于发现线索，不用于确认模型内部结构。

## A. Transformer / LLM Foundations

- Attention Is All You Need — https://arxiv.org/abs/1706.03762
- RoFormer / RoPE — https://arxiv.org/abs/2104.09864
- GQA — https://arxiv.org/abs/2305.13245
- LoRA — https://arxiv.org/abs/2106.09685
- QLoRA — https://arxiv.org/abs/2305.14314
- Switch Transformer / MoE — https://arxiv.org/abs/2101.03961

## B. Vision Foundations

- ViT — https://arxiv.org/abs/2010.11929
- CLIP — https://arxiv.org/abs/2103.00020
- SigLIP — https://arxiv.org/abs/2303.15343
- DINOv2 — https://arxiv.org/abs/2304.07193
- SAM — https://arxiv.org/abs/2304.02643

## C. Classic Multimodal Architectures

- Flamingo — https://arxiv.org/abs/2204.14198
- BLIP-2 — https://arxiv.org/abs/2301.12597
- LLaVA — https://arxiv.org/abs/2304.08485
- Qwen-VL — https://arxiv.org/abs/2308.12966

## D. 2025–2026 Representative VLM / MLLM

- Qwen2.5-VL — https://arxiv.org/abs/2502.13923
- Qwen3-VL — https://arxiv.org/abs/2511.21631
- Qwen3-VL official — https://github.com/QwenLM/Qwen3-VL
- Qwen3.5 / Qwen3.6 official — https://github.com/QwenLM/Qwen3.6
- Qwen3-Omni — https://github.com/QwenLM/Qwen3-Omni
- InternVL3.5 — https://arxiv.org/abs/2508.18265
- GLM-V official — https://github.com/zai-org/GLM-V
- GLM-5V-Turbo — https://arxiv.org/abs/2604.26752
- Seed1.5-VL — https://arxiv.org/abs/2505.07062
- Seed1.5-VL official — https://github.com/ByteDance-Seed/Seed1.5-VL
- Kimi-VL — https://arxiv.org/abs/2504.07491
- MiniCPM-V / MiniCPM-o — https://github.com/OpenBMB/MiniCPM-V
- Gemma 3 — https://arxiv.org/abs/2503.19786
- Janus-Pro — https://arxiv.org/abs/2501.17811
- STEP3-VL-10B — https://arxiv.org/abs/2601.09668
- Llama 4 official — https://ai.meta.com/blog/llama-4-multimodal-intelligence/

## E. Multimodal Retrieval

- Qwen3-VL-Embedding & Reranker — https://arxiv.org/abs/2601.04720

## F. Training / Alignment / Reasoning

- DPO — https://arxiv.org/abs/2305.18290
- PPO — https://arxiv.org/abs/1707.06347
- DeepSeekMath / GRPO context — https://arxiv.org/abs/2402.03300
- InternVL3.5 Cascade RL — https://arxiv.org/abs/2508.18265
- GLM-V scalable RL — https://arxiv.org/abs/2507.01006

## G. Distributed Training

- PyTorch DDP — https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html
- PyTorch FSDP2 `fully_shard` — https://docs.pytorch.org/docs/main/distributed.fsdp.fully_shard.html
- DeepSpeed ZeRO — https://www.deepspeed.ai/tutorials/zero/
- Megatron-LM — https://github.com/NVIDIA/Megatron-LM

## H. Inference / Serving

- vLLM — https://github.com/vllm-project/vllm
- vLLM multimodal docs — https://docs.vllm.ai/en/latest/features/multimodal_inputs/
- SGLang — https://github.com/sgl-project/sglang
- FlashAttention — https://arxiv.org/abs/2205.14135
- FlashAttention-3 — https://arxiv.org/abs/2407.08608
- FlashAttention-4 — https://arxiv.org/abs/2603.05451

## I. Evaluation

- MMMU — https://arxiv.org/abs/2311.16502
- MathVista — https://arxiv.org/abs/2310.02255
- LongVideoBench — https://arxiv.org/abs/2407.15754
- OSWorld — https://arxiv.org/abs/2404.07972

---

### 使用参考文献的面试原则

你不需要背 DOI 或 benchmark 小数点。需要知道：

- 这篇工作解决什么问题；
- 输入输出是什么；
- 架构改在哪里；
- 训练改在哪里；
- 成本如何变化；
- 它与上一代相比为什么合理。

真正遇到“某模型到底用了哪一层/多少参数”的细节问题，回官方实现核对，不凭印象回答。