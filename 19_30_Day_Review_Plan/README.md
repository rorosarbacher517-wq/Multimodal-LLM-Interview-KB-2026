# 19 · 30-Day Interview Review Plan

> 默认每天 2–4 小时。时间更充足时，把“口述 + 手写 + 小实验”加倍，而不是一天刷更多新概念。

## Week 1：把底层补齐

### Day 1
- Transformer 总体结构
- Q/K/V
- scaled attention
- 手写 attention

### Day 2
- Multi-Head
- mask
- Pre-Norm / RMSNorm
- SwiGLU

### Day 3
- RoPE
- GQA/MQA
- KV Cache
- 手算 KV 显存

### Day 4
- MoE
- router
- active params
- Expert Parallel 基础

### Day 5
- CNN vs ViT
- patchify
- position embedding
- 手算视觉 token

### Day 6
- CLIP / SigLIP / DINO
- OCR / grounding
- dynamic resolution

### Day 7
- 闭卷画：Vision Encoder → Projector → LLM
- 随机抽 20 题复盘

## Week 2：多模态模型 + 数据 + 训练

### Day 8
- LLaVA / Flamingo / BLIP-2
- MLP / Q-Former / Resampler

### Day 9
- Qwen2.5-VL → Qwen3-VL
- MRoPE / DeepStack / timestamp

### Day 10
- Qwen3.5 / InternVL3.5
- native multimodal / ViR / DvD

### Day 11
- GLM-V / Seed1.5-VL / Kimi-VL

### Day 12
- MiniCPM-V/O / Qwen3-Omni
- 端侧 + full duplex

### Day 13
- 数据清洗、去重、质量打分、配比

### Day 14
- Alignment → Pretraining → SFT
- LoRA / QLoRA
- 手写 LoRA

## Week 3：RL + Agent + 系统

### Day 15
- DPO / RM / PPO / GRPO / RLVR

### Day 16
- visual reasoning
- grounding reward
- active perception
- test-time scaling

### Day 17
- video tokenization
- long video retrieval
- temporal grounding

### Day 18
- Function Calling / MCP / RAG

### Day 19
- GUI Agent / VLA
- action space / verifier

### Day 20
- DDP / ZeRO / FSDP2

### Day 21
- TP / PP / EP / Sequence Parallel
- 画 8-GPU / 64-GPU 训练方案

## Week 4：Serving + 面试化

### Day 22
- Prefill / Decode
- KV / PagedAttention
- Continuous Batching

### Day 23
- FlashAttention
- quantization
- prefix cache
- speculative decoding

### Day 24
- vLLM / SGLang
- multimodal serving
- OOM diagnosis

### Day 25
- MMMU / MathVista / OCR / grounding
- perception vs reasoning diagnostics

### Day 26
- System Design：PDF QA
- System Design：长视频 QA

### Day 27
- System Design：GUI Agent
- System Design：多租户 MLLM serving

### Day 28
- 项目介绍 90 秒 / 3 分钟 / 10 分钟三个版本
- 准备 3 个 bug / failure case

### Day 29
- 高频题 1–63，闭卷口述
- 手写 5 题

### Day 30
- 高频题 64–126
- 完整模拟面试：基础 20 min + 项目 20 min + 系统设计 20 min

## 每天打卡模板

```text
[ ] 今日新知识点
[ ] 5 道闭卷口述
[ ] 1 道手写 / shape 推导
[ ] 1 个真实模型源码/官方文档核对
[ ] 记录 3 个不会的问题
[ ] 第二天优先复盘不会的问题
```

## 通过标准

不是“看完仓库”，而是：

- 80% 高频题能在 2 分钟内说清；
- 能不看资料画出典型 MLLM；
- 能计算 attention / visual token / KV / LoRA 参数量；
- 能解释至少 6 个 2026 代表模型的核心差异；
- 能设计一个端到端多模态系统；
- 项目追问 3 层后仍然能说到真实代码、数据和实验。