# Multimodal-LLM-Interview-KB-2026

> 面向 2026 秋招 / 社招的 **多模态大模型算法面试知识库**  
> 审核基线：**2026-08-19**  
> 目标：**从数学与工程底层一路讲到 MLLM / Generation / Agent / VLA，并且每个知识点都能解释输入、shape、训练、推理和 trade-off。**

## 这套知识库的知识依赖

```text
AI Math
  ↓
Machine Learning + Deep Learning + PyTorch/CUDA
  ↓
Transformer / LLM
  ↓
Vision Backbones + Detection/Segmentation/Grounding
OCR/Document + Pose/Tracking + Depth/3D + Speech/Audio
  ↓
Multimodal Core Architecture
  ├─ Understanding / Reasoning
  └─ Generation / World Models
  ↓
Data → Pretraining/SFT → RL/Post-training → Safety
  ↓
Retrieval / RAG
  ↓
Agent Core: Loop / Tool / Planning / Memory / MCP / A2A
  ↓
Web / GUI / Coding Agent / VLA / Omni
  ↓
Distributed Training → Serving
  ↓
Evaluation → Code → System Design → Project Interview
```

这比“背最新模型名称”更重要：**新模型可以变，知识依赖和问题拆解方式更稳定。**

---

# 1. Foundation Layer

| 模块 | 核心内容 |
|---|---|
| [00 Roadmap](./00_Roadmap/README.md) | 全仓库学习顺序与能力地图 |
| [00A Math Fundamentals for AI](./00A_Math_Fundamentals_for_AI/README.md) | 线代、微积分、概率统计、信息论、优化、数值稳定 |
| [00B Deep Learning Fundamentals](./00B_Deep_Learning_Fundamentals/README.md) | Tensor、反向传播、Loss、Optimizer、Norm、Residual、Mixed Precision |
| [00C Machine Learning Fundamentals](./00C_Machine_Learning_Fundamentals/README.md) | Linear/Logistic、SVM、RF/XGBoost、聚类、指标、泛化、Calibration |
| [00D PyTorch & CUDA Engineering](./00D_PyTorch_CUDA_Engineering/README.md) | Autograd、DataLoader、Memory Layout、CUDA、Profiler、OOM |
| [01 Transformer & LLM Fundamentals](./01_Transformer_LLM_Fundamentals/README.md) | Tokenizer、Attention、RoPE、GQA、KV、MoE、Training/Decoding |

# 2. Visual / Audio Perception Layer

| 模块 | 核心内容 |
|---|---|
| [02 Vision Fundamentals](./02_Vision_Fundamentals/README.md) | CNN、ViT、CLIP/SigLIP、DINO、visual tokens |
| [02A Vision Backbones & Pretraining](./02A_Vision_Backbones_Pretraining/README.md) | ResNet、ConvNeXt、Swin、MAE、CLIP/DINO/SigLIP2、Augmentation |
| [02B Detection / Segmentation / Grounding](./02B_Detection_Segmentation_Grounding/README.md) | YOLO、DETR、U-Net、Mask R-CNN/Mask2Former、SAM2、GroundingDINO |
| [02C OCR / Document AI](./02C_OCR_Document_AI/README.md) | OCR、Layout、Table/Formula、PaddleOCR-VL、MinerU、Document RAG |
| [02D Pose / Tracking / Motion](./02D_Pose_Tracking/README.md) | ViTPose、RTMPose、MOT/SOT、RAFT、ByteTrack、CoTracker |
| [02E Depth / 3D Perception](./02E_Depth_3D_Perception/README.md) | Depth、Camera Geometry、SLAM、Point/BEV、NeRF/3DGS、DUSt3R/VGGT |
| [08A Speech & Audio Fundamentals](./08A_Speech_Audio_Fundamentals/README.md) | ASR、CTC、Whisper、wav2vec2、VAD、Diarization、Codec、TTS |

# 3. Multimodal Model Layer

| 模块 | 核心内容 |
|---|---|
| [03 Multimodal Core Architecture](./03_Multimodal_Core_Architecture/README.md) | Vision Encoder、Projector、Q-Former、Resampler、Fusion、Dynamic Resolution |
| [03B Generation & World Models](./03B_Multimodal_Generation_World_Models/README.md) | VAE/VQ、Diffusion、DiT、Flow Matching、Unified Generation、World Model |
| [04 Representative Models — 2026](./04_Representative_Models_2026/README.md) | Qwen3-VL/3.5/3.8、InternVL3.5/U、GLM-V、Seed、Kimi、Omni 等 |

# 4. Data / Training / Reasoning / Safety

| 模块 | 核心内容 |
|---|---|
| [05 Multimodal Data Engineering](./05_Multimodal_Data_Engineering/README.md) | 数据寻源、清洗、去重、质量、配比、合成、数据闭环 |
| [05 Advanced Data Infrastructure](./05_Multimodal_Data_Engineering/ADVANCED.md) | Sharding/Streaming、MinHash/LSH、Active Learning、Lineage、PII |
| [06 Pretraining / SFT / PEFT](./06_Pretraining_SFT_PEFT/README.md) | Alignment、Pretrain、SFT、LoRA/QLoRA、Freeze/Unfreeze |
| [06 Advanced Training Engineering](./06_Pretraining_SFT_PEFT/ADVANCED.md) | Token Budget、Packing、Long Context、Checkpoint/Resume、Reproducibility |
| [07 RL / Reasoning](./07_PostTraining_RL_Reasoning/README.md) | DPO、RLHF、GRPO、RLVR、Visual Reasoning、Active Perception |
| [07 Advanced RL](./07_PostTraining_RL_Reasoning/ADVANCED.md) | Policy Gradient、GAE、PPO Clip、KL、Rollout Infra、Verifier |
| [07B Safety & Reliability](./07B_Multimodal_Safety_Reliability/README.md) | Prompt Injection、Tool Permission、Sandbox、PII、Red Team、Audit |

# 5. Retrieval / Agent / Omni

| 模块 | 核心内容 |
|---|---|
| [09A Retrieval & Vector Search](./09A_Retrieval_Vector_Search/README.md) | BM25、Embedding、HNSW、IVF/PQ、Hybrid Retrieval、Reranker |
| [09 RAG / Tools / GUI / VLA](./09_RAG_Tools_Agents_GUI_VLA/README.md) | Multimodal RAG、Function Call、GUI grounding、VLA 应用层 |
| [09B Agent Fundamentals & Engineering](./09B_Agent_Fundamentals_Engineering/README.md) | Agent Loop、Tool、Planning、Memory、Multi-Agent、MCP/A2A、Sandbox、Checkpoint、Eval |
| [08 Video / Audio / Omni](./08_Video_Audio_Omni/README.md) | Long Video、Temporal Alignment、Streaming、Full Duplex |

# 6. Large-scale Systems

| 模块 | 核心内容 |
|---|---|
| [10 Distributed Training](./10_Distributed_Training/README.md) | DDP、FSDP2、ZeRO、TP/PP/EP/SP |
| [10 Advanced Distributed](./10_Distributed_Training/ADVANCED.md) | CP、1F1B、Topology、Communication Overlap、Offload、Straggler |
| [11 Inference & Serving](./11_Inference_Serving_Optimization/README.md) | Prefill/Decode、PagedAttention、vLLM/SGLang、Quantization、Caching |
| [11 Advanced Serving](./11_Inference_Serving_Optimization/ADVANCED.md) | Chunked Prefill、Disaggregation、Multi-LoRA、FP8、Admission/Scheduling |

# 7. Interview Conversion Layer

| 模块 | 核心内容 |
|---|---|
| [12 Evaluation & Diagnostics](./12_Evaluation_Diagnostics/README.md) | MMMU/Math、OCR、Grounding、Video、Hallucination、Agent Eval |
| [12 Advanced Evaluation](./12_Evaluation_Diagnostics/ADVANCED.md) | Bootstrap CI、Paired Test、Calibration、OOD、Cost-normalized Eval |
| [13 Code Handwriting](./13_Code_Handwriting/README.md) | Attention、Projector、LoRA、SFT Loss、KV、MoE |
| [13 Advanced Code Drills](./13_Code_Handwriting/ADVANCED.md) | RMSNorm、SwiGLU、Top-p、Patchify、GQA、Dice、Debug |
| [14 System Design](./14_System_Design/README.md) | PDF QA、Video QA、GUI Agent、Data Platform、Serving |
| [15 Project Interview](./15_Project_Interview/README.md) | 项目介绍、Ablation、Bug/OOM、Bad Case、个人贡献 |
| [16 高频题索引](./16_High_Frequency_Interview/README.md) | 通用 MLLM 高频题 |
| [16A Math/DL/Transformer 高频题](./16A_Deep_Learning_Transformer_High_Frequency/README.md) | 基础闭卷 |
| [16B Visual Perception 高频题](./16B_Visual_Perception_High_Frequency/README.md) | 视觉专项闭卷 |
| [16C Agent 高频题](./16C_Agent_High_Frequency/README.md) | Agent / Tool / Memory / Protocol / GUI / Coding / Safety 专项闭卷 |
| [17 2026-08 技术快照](./17_2026_Snapshot/README.md) | 只保留有 primary source 的快速变化 |
| [18 Primary References](./18_References/README.md) | 论文 / 官方 GitHub / 官方文档 |
| [19 30-Day Plan](./19_30_Day_Review_Plan/README.md) | 面试冲刺路线 |

---

# 面试回答统一框架

## 模型题
1. 输入是什么？
2. shape/token/feature 如何变化？
3. 核心模块解决什么问题？
4. loss / matching / reward 怎么定义？
5. train 与 inference 有什么区别？
6. compute / memory / latency 花在哪里？
7. 和上一代方法相比改变了什么假设？

## Agent 题
1. Goal / environment / action space 是什么？
2. Agent Loop 如何闭环？
3. Tool schema 和 state 如何组织？
4. Planning / memory / verifier 放在哪里？
5. failure 如何 retry / replan / resume？
6. permission / sandbox / prompt injection 如何处理？
7. task success、latency、cost 如何评估？

## 数据题
**能力目标 → 错误定义 → 寻源 → 解析 → 清洗 → 去重 → 质量 → 配比 → 训练反馈 → 再迭代。**

## 系统题
**SLO → workload → model/data flow → memory/compute → parallel/scheduler/cache → failure handling → evaluation/safety。**

---

# 可信度与维护

- 新模型只采用论文、官方 GitHub、官方 model card/文档可确认的信息。
- 闭源模型公开 capability 不等于公开 internal architecture。
- 对具体版本不确定时写 **unknown / not publicly disclosed**，不补猜测。
- 每次 push/PR 自动运行 [`scripts/audit_repo.py`](./scripts/audit_repo.py) 检查 broken links 和结构问题。
- 详细更新原则见 [Audit & Update Policy](./AUDIT_AND_UPDATE_POLICY.md)。

**目标不是“问题最多”，而是形成一张能持续维护、能真正用于算法面试的知识依赖图。**
