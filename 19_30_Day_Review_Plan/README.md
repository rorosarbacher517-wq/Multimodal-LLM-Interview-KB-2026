# 19 · 30-Day Interview Review Plan

> 默认每天 3–6 小时。仓库已经足够大，不应该一天“看几十页”；每天必须包含：**理解 → 闭卷口述 → shape/公式 → 代码/源码 → 复盘**。

## Week 1 · Math / ML / DL / Transformer / PyTorch

### Day 1 — Linear Algebra + Information Theory
- vector/matrix/dot/cosine/norm
- rank/SVD/PCA
- entropy/CE/KL
- softmax stability
- 闭卷 10 题

### Day 2 — Calculus + Probability + Optimization
- gradient/chain rule/Jacobian/Hessian
- expectation/variance/Bayes/MLE
- SGD/Adam/AdamW
- warmup/cosine

### Day 3 — Classical ML
- Linear/Logistic/SVM
- Tree/RF/GBDT/XGBoost
- bias/variance/data leakage
- precision/recall/AUC/calibration
- 做一个 sklearn/XGBoost baseline

### Day 4 — Deep Learning + PyTorch
- autograd / computation graph
- norm/residual/activation
- FP16/BF16
- DataLoader/collate/contiguous
- CUDA memory hierarchy / OOM

### Day 5 — Transformer I
- tokenizer/embedding
- Q/K/V / multi-head / mask
- Pre-Norm/RMSNorm/SwiGLU
- 手写 Attention

### Day 6 — Transformer II
- RoPE
- MHA/MQA/GQA
- KV cache
- prefill/decode
- MoE
- 手算 KV memory

### Day 7 — 基础闭卷日
- 16A 抽题
- 手写 RMSNorm/SwiGLU/Attention/top-p
- 从零画 `text → tokenizer → model → logits → sampling`

## Week 2 · Complete Perception Stack

### Day 8 — Vision Backbone
ResNet / ViT / Swin / ConvNeXt / MAE / CLIP / DINO / SigLIP；手算 patch/token。

### Day 9 — Detection / Segmentation
YOLO / DETR / FPN / assignment / NMS；semantic-instance-panoptic；U-Net / Mask R-CNN / Mask2Former / SAM。

### Day 10 — Grounding / Document
GroundingDINO / Grounded SAM；OCR detection/recognition/CTC；layout/reading order；Document RAG。

### Day 11 — Pose / Tracking / Motion
ViTPose / ByteTrack / OC-SORT / SOT / RAFT / CoTracker；区分 detection error 与 association error。

### Day 12 — Depth / 3D Geometry
camera projection / stereo / SfM / SLAM；Point/Voxel/BEV；Depth Anything / DUSt3R / VGGT。

### Day 13 — Neural 3D + Audio
NeRF / 3DGS；ASR/Whisper/wav2vec2/VAD/diarization/codec/TTS。

### Day 14 — Perception 闭卷
16B 抽题；画 `image/video/audio/LiDAR → structured evidence → MLLM`。

## Week 3 · MLLM / Generation / Data / Training / RL

### Day 15 — MLLM Architecture
Vision Encoder → Projector/Q-Former/Resampler → LLM；dynamic resolution；multi-image/video position。

### Day 16 — Representative Models
Qwen3-VL → Qwen3.5/3.8；InternVL3.5/U；Seed/GLM/Kimi/MiniCPM。重点讲“方法差异”，不背排行榜。

### Day 17 — Generation
VAE/VQ → Diffusion/DDIM/CFG → Latent Diffusion → DiT → Flow Matching → Unified Generation / World Model。

### Day 18 — Data Engineering
sampling/dedup/quality/mixture；sharding/streaming；lineage/licensing/PII；hard-negative/active learning。

### Day 19 — Pretraining / SFT
alignment/pretrain/SFT；LoRA/QLoRA；packing/token budget；long-context；checkpoint/resume。

### Day 20 — RL / Reasoning
DPO/PPO/GRPO/RLVR；advantage/KL；rollout/verifier；active perception；reward hacking。

### Day 21 — Safety
indirect prompt injection；RAG poisoning；tool permissions；confirmation/sandbox；red team；agent audit log。

## Week 4 · Retrieval / Agent / Distributed / Serving / Interview

### Day 22 — Retrieval / RAG
BM25 + dense embedding；HNSW/IVF-PQ；hybrid recall；reranker；retrieval vs generation diagnostics。

### Day 23 — Agent Core / Tool / Memory / Protocol
重点学习 [09B Agent Fundamentals & Engineering](../09B_Agent_Fundamentals_Engineering/README.md)：
- Chatbot vs Workflow vs Agent；
- Agent Loop / stop condition；
- function call / tool schema / routing；
- timeout / retry / idempotency；
- ReAct / plan-execute / planner-executor-verifier；
- working/episodic/semantic memory；
- context compaction / externalized state；
- Function Calling vs MCP vs A2A。

当天闭卷完成 [16C Agent 高频题](../16C_Agent_High_Frequency/README.md) 的前 40 题。

### Day 24 — Web / GUI / Coding Agent / Omni
- DOM + screenshot；
- GUI grounding；
- Coding Agent：inspect → edit → test → repair → verify；
- sandbox / least privilege；
- checkpoint / resume / durable execution；
- Agent evaluation / OSWorld；
- long-video retrieval；
- full-duplex / interruption。

完成 16C 剩余题目，并从零画：

```text
Goal
→ Agent Harness
→ Planner / Model
→ Tools / Remote Agents
→ Environment
→ Observation
→ Verifier
→ Continue / Replan / Stop
```

### Day 25 — Distributed Training
DDP/FSDP/ZeRO；TP/PP/EP/SP/CP；1F1B；topology；communication overlap；straggler。

### Day 26 — Serving
vLLM/SGLang；PagedAttention；continuous batching；chunked prefill；disaggregation；quantization/cache/admission control。

### Day 27 — Evaluation
benchmark buckets；perception vs reasoning；bootstrap CI/paired test；calibration/OOD；cost-normalized eval；Agent task success / recovery / safety。

### Day 28 — Code + System Design
Attention/LoRA/IoU-NMS/Patchify；PDF QA/Video QA/GUI Agent/MLLM serving，至少做 2 道完整系统设计，其中至少一道 Agent 系统题必须包含 state、tool、verifier、sandbox、checkpoint。

### Day 29 — Project Interview
准备项目 90 秒/3 分钟/10 分钟；3 个 controlled ablation；3 个 bad cases；2 个真实 bug/OOM；个人贡献边界。

### Day 30 — Full Mock
- fundamentals 20 min；
- model/data/training 20 min；
- Agent / system 20 min；
- project 20 min；
- code 20 min；
- 当天只复盘暴露出的短板。

---

## 每日打卡
```text
[ ] 5–10 道闭卷口述
[ ] 1 个公式/shape 手推
[ ] 1 道代码或一个真实源码模块
[ ] 记录 3 个不会的问题
[ ] 复盘前一天错误
```

## 通过标准
- 80% 高频题能在 2 分钟内讲清；
- 能从 shape 推导模型，不靠背图；
- 能区分 confirmed fact 和未公开实现；
- 能从 data/model/training/system 四层定位 bad case；
- 能设计一个可部署、可评测、可安全回滚的端到端多模态系统；
- 能设计一个包含 **tool / state / memory / verifier / permission / sandbox / checkpoint** 的 production Agent。
