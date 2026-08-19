# 19 · 30-Day Interview Review Plan

> 默认每天 2–4 小时。现在基础层已经扩展为 **Deep Learning → Transformer → Vision/Perception → MLLM**，所以 Week 1 不再从 Q/K/V 直接开始。

## Week 1：Deep Learning + Transformer + 视觉底座

### Day 1 · Tensor / Autograd / Loss
- Tensor shape / matmul / broadcasting
- Forward / computational graph
- Gradient / chain rule / backward
- MSE / MAE / Cross Entropy / BCE / KL
- PyTorch `requires_grad / grad / zero_grad`
- 闭卷手推一个两层 MLP 的 shape

### Day 2 · Optimization / Stability / Memory
- ReLU / GELU / SiLU
- SGD / Momentum / Adam / AdamW
- warmup / cosine / weight decay
- LayerNorm / RMSNorm / BatchNorm
- residual connection
- FP16 / BF16 / mixed precision
- gradient accumulation / clipping
- activation checkpointing
- 粗算 parameter / gradient / optimizer / activation memory

### Day 3 · Tokenizer → Attention
- BPE / SentencePiece
- vocabulary / BOS / EOS / PAD
- embedding `[B,L] → [B,L,D]`
- hidden state / logits / probability
- Q/K/V
- scaled dot-product attention
- Multi-Head reshape
- causal mask / padding mask
- 手写 attention

### Day 4 · Transformer Block → LLM Inference
- Pre-Norm / RMSNorm / residual
- FFN / SwiGLU
- RoPE
- MHA / MQA / GQA
- KV Cache
- teacher forcing / next-token loss
- prefill / decode
- top-k / top-p / temperature
- MoE / router / active params
- 手算 KV cache

### Day 5 · Vision + Detection / Segmentation / Grounding
- CNN vs ViT
- patchify / visual token
- CLIP / SigLIP / DINO
- YOLO / DETR / RT-DETR
- SAM / SAM2
- GroundingDINO
- 手算 P3/P4/P5 和 ViT token 数

### Day 6 · OCR / Document + Pose / Tracking
- OCR detection / recognition / CTC
- Layout / reading order
- PaddleOCR-VL / MinerU
- ViTPose / RTMPose
- ByteTrack / OC-SORT / CoTracker
- Document RAG

### Day 7 · Depth / 3D + 全基础闭卷
- relative / metric depth
- Depth Anything
- camera intrinsics / extrinsics
- point / voxel / pillar / BEV
- DUSt3R / MASt3R / VGGT
- 闭卷画：`Deep Learning training loop → Transformer → Perception → MLLM`
- 抽 30 道 16A/16B 高频题

## Week 2：MLLM 模型 + 数据 + 训练

### Day 8
- Vision Encoder → Projector → LLM
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
- OCR / detection / 3D pseudo-label data engine

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
- object/point tracking 与 video memory

### Day 18
- Function Calling / MCP / Multimodal RAG
- OCR / detector / depth 作为 perception tools

### Day 19
- GUI Agent / VLA
- action space / verifier
- 2D/3D coordinate frame

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
- perception model + MLLM multi-service design
- OOM diagnosis

### Day 25
- MMMU / MathVista
- OCR / grounding / tracking / depth metrics
- perception vs reasoning diagnostics

### Day 26
- System Design：PDF QA / Document RAG
- System Design：Grounded auto-labeling pipeline

### Day 27
- System Design：长视频 QA + tracking
- System Design：GUI/VLA + 3D perception

### Day 28
- 项目介绍 90 秒 / 3 分钟 / 10 分钟三个版本
- 准备 3 个真实 bug / failure case

### Day 29
- 16A：Deep Learning / Transformer 高频题闭卷
- 16B：Visual Perception 高频题闭卷
- 手写 Attention / IoU-NMS / LoRA

### Day 30
- 通用 MLLM / Training / Agent / Systems 高频题
- 完整模拟：基础 20 min + 项目 20 min + 系统设计 20 min

## 每天打卡模板

```text
[ ] 今日新知识点
[ ] 5 道闭卷口述
[ ] 1 道手写 / shape 推导
[ ] 1 个真实源码/原论文核对
[ ] 记录 3 个不会的问题
[ ] 第二天优先复盘不会的问题
```

## 通过标准

不是“看完仓库”，而是：

- Deep Learning / Transformer 基础不依赖背稿也能解释；
- 80% 高频题能在 2 分钟内说清；
- 能推导 Linear / Conv / Attention / KV Cache 的 shape；
- 能解释 forward → loss → backward → optimizer 的完整训练链；
- 能画出 YOLO / SAM / OCR pipeline / tracker / depth-to-3D / 典型 MLLM；
- 能计算 attention / visual token / detector feature map / KV / LoRA 参数量；
- 能设计一个端到端多模态系统；
- 项目追问 3 层后仍然能说到真实代码、数据和实验。
