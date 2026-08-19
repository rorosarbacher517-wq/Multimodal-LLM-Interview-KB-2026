# 00 · Roadmap：多模态算法岗知识地图

## 一张图
```text
00A Math
  ↓
00C Machine Learning ─┐
00B Deep Learning ────┼→ 00D PyTorch/CUDA
                      ↓
01 Transformer / LLM
                      ↓
02 Vision → 02A Backbone/Pretraining
   ├→ 02B Detection/Segmentation/Grounding
   ├→ 02C OCR/Document
   ├→ 02D Pose/Tracking/Motion
   └→ 02E Depth/3D/Geometry
08A Speech/Audio ──────┘
                      ↓
03 Multimodal Core Architecture
   ├→ Understanding / Reasoning
   └→ 03B Generation / World Models
                      ↓
05 Data → 06 Train → 07 RL → 07B Safety
                      ↓
08 Omni / 09 RAG-Agent-VLA / 09A Retrieval
                      ↓
10 Distributed → 11 Serving
                      ↓
12 Evaluation → 13 Code → 14 System → 15 Project
```

## Phase 1：底层必须能推导
学习：[00A](../00A_Math_Fundamentals_for_AI/README.md) → [00B](../00B_Deep_Learning_Fundamentals/README.md) → [00C](../00C_Machine_Learning_Fundamentals/README.md) → [00D](../00D_PyTorch_CUDA_Engineering/README.md) → [01](../01_Transformer_LLM_Fundamentals/README.md)

通过标准：
- 能解释 dot product / CE / KL / gradient / AdamW；
- 能写出 `[B,L,D]` 矩阵乘；
- 能画 forward→loss→backward→optimizer；
- 能手算 attention 与 KV cache；
- 能解释 Tensor contiguous、autograd、GPU memory hierarchy。

## Phase 2：视觉/音频感知必须完整
学习：[02](../02_Vision_Fundamentals/README.md) → [02A](../02A_Vision_Backbones_Pretraining/README.md) → 02B/02C/02D/02E + [08A](../08A_Speech_Audio_Fundamentals/README.md)

通过标准：
- 能画 ResNet/ViT 的 feature 变化；
- 能解释 YOLO/DETR/SAM/GroundingDINO；
- 能区分 semantic/instance/panoptic；
- 能解释 OCR→layout→Document RAG；
- 能区分 box tracking / point tracking / optical flow；
- 能从 camera geometry 讲到 SLAM/BEV/NeRF/VGGT；
- 能解释 ASR/codec/TTS 的基本链路。

## Phase 3：MLLM 不只要会画三块
学习：[03](../03_Multimodal_Core_Architecture/README.md) + [03B](../03B_Multimodal_Generation_World_Models/README.md) + [04](../04_Representative_Models_2026/README.md)

必须能回答：
1. Vision Encoder 输出什么？
2. `Dv → Dl` 怎么做？
3. `N → N'` 怎么压？
4. fusion 在哪里？
5. position/time 怎么编码？
6. understanding 与 generation 为什么表示需求不同？
7. dynamic resolution 影响什么成本？
8. 新模型哪些细节是 confirmed，哪些 unknown？

## Phase 4：训练是 Data + Optimization + RL
学习 05 → 06 → 07 → 07B。

不要把“会调 LoRA”当成训练全部内容。需要会：
- data mixture / lineage；
- token-based batching / packing；
- checkpoint/resume；
- DPO/PPO/GRPO/RLVR；
- rollout/verifier；
- multimodal prompt injection 与 tool safety。

## Phase 5：Agent / RAG / Omni
学习 08/08A → 09/09A。

能画：
```text
perceive → retrieve/tool → reason → policy check → act → observe → verify
```
并解释 BM25/HNSW/reranker、GUI grounding、VLA action representation、full-duplex streaming。

## Phase 6：大规模工程
学习 10 → 11。

至少会：
- 参数/activation/KV 显存估算；
- DP/TP/PP/EP/SP/CP；
- FSDP/ZeRO；
- topology / collective；
- prefill/decode；
- continuous batching / paged KV；
- chunked prefill / disaggregation；
- quantization / cache / admission control。

## Phase 7：面试化
12 Evaluation → 13 Code → 14 System Design → 15 Project → 16/16A/16B。

## 判断自己是否真的掌握
对任何新模型，优先回答九个问题：
1. 输入是什么？
2. 表示/shape 如何变化？
3. 核心计算是什么？
4. 为什么这样设计？
5. loss/reward 怎么来？
6. train 与 inference 有何不同？
7. memory/compute/latency 花在哪里？
8. bad case 如何定位？
9. 哪些细节是官方确认、哪些没有公开？
