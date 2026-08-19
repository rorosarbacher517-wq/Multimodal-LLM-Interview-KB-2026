# 19 · 30-Day Interview Review Plan

> 默认每天 2–4 小时。视觉感知内容新增后，不建议简单延长到 40 天；更好的做法是把 Week 1 做成“Transformer + 完整视觉底座”，后面再进入 MLLM。

## Week 1：Transformer + 完整视觉感知

### Day 1
- Transformer 总体结构
- Q/K/V / scaled attention
- 手写 attention

### Day 2
- Multi-Head / mask
- Pre-Norm / RMSNorm / SwiGLU
- RoPE / GQA

### Day 3
- KV Cache
- MoE / router / active params
- 手算 KV 显存

### Day 4
- CNN vs ViT
- patchify / position encoding
- CLIP / SigLIP / DINO
- 手算视觉 token

### Day 5
- YOLOv8–11/26
- DETR / RT-DETR
- SAM / SAM2
- GroundingDINO
- 手算 P3/P4/P5 尺寸

### Day 6
- OCR detection / recognition / CTC
- Layout / reading order
- PaddleOCR-VL-1.6
- MinerU2.5 / Pro
- Document RAG

### Day 7
- Pose：ViTPose / RTMPose
- Tracking：ByteTrack / OC-SORT / CoTracker
- Depth：Depth Anything V2
- 3D：Point Cloud / BEV / DUSt3R / VGGT
- 闭卷画完整 perception stack

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
- 准备 3 个 bug / failure case

### Day 29
- 高频题闭卷口述：Transformer / Vision / Perception
- 手写 IoU/NMS/Attention/LoRA

### Day 30
- 高频题闭卷口述：MLLM / Training / Agent / Systems
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
- 能画出 YOLO / SAM / OCR pipeline / tracker / depth-to-3D / 典型 MLLM；
- 能计算 attention / visual token / detector feature map / KV / LoRA 参数量；
- 能解释至少 6 个 2026 代表模型的核心差异；
- 能说明什么时候用专用 perception model，什么时候直接用 MLLM；
- 能设计一个端到端多模态系统；
- 项目追问 3 层后仍然能说到真实代码、数据和实验。
