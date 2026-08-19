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
09A Retrieval → 09 RAG/GUI/VLA
                      ↓
09B Agent Core: Loop/Tool/Planning/Memory/MCP/A2A
                      ↓
Web / GUI / Coding Agent / VLA / 08 Omni
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

## Phase 5：Retrieval → Agent → GUI / VLA / Omni
推荐顺序：

[09A Retrieval](../09A_Retrieval_Vector_Search/README.md)
→ [09 RAG / GUI / VLA](../09_RAG_Tools_Agents_GUI_VLA/README.md)
→ [09B Agent Fundamentals & Engineering](../09B_Agent_Fundamentals_Engineering/README.md)
→ [08 Video / Audio / Omni](../08_Video_Audio_Omni/README.md)

必须能画：

```text
Goal
→ Observe
→ Retrieve / Tool
→ Plan
→ Policy / Permission Check
→ Act
→ Environment Changes
→ Observe Again
→ Verify
→ Continue / Replan / Stop
```

通过标准：
- 能区分 Chatbot / Workflow / Agent；
- 能解释 Function Calling / MCP / A2A 的层次关系；
- 能解释 planner / executor / verifier；
- 能设计 working/episodic/semantic memory 与 externalized state；
- 能说明 timeout / retry / idempotency / checkpoint / resume；
- 能设计 Web / GUI / Coding Agent；
- 能解释 prompt injection、least privilege、sandbox；
- 能从 task success / latency / cost / safety 四层评测 Agent；
- 能解释 GUI grounding、VLA action representation、full-duplex streaming。

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
12 Evaluation → 13 Code → 14 System Design → 15 Project → 16/16A/16B/[16C Agent 高频题](../16C_Agent_High_Frequency/README.md)。

## 判断自己是否真的掌握
对任何新模型或 Agent 系统，优先回答九个问题：
1. 输入/Goal 是什么？
2. 表示/shape 或 state 如何变化？
3. 核心计算/decision loop 是什么？
4. 为什么这样设计？
5. loss/reward/verifier 怎么来？
6. train 与 inference/execution 有何不同？
7. memory/compute/latency/cost 花在哪里？
8. bad case 如何定位、恢复和验证？
9. 哪些细节是官方确认、哪些没有公开？
