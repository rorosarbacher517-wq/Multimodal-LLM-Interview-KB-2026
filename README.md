# Multimodal-LLM-Interview-KB-2026

> 面向 2026 秋招 / 社招的 **多模态大模型算法面试知识库**  
> 技术快照：**截至 2026-08**  
> 目标：**讲得清楚、答得准确、能继续追问、能落到代码和系统。**

## 这套知识库解决什么问题

很多面试资料的问题是：题目很多，但彼此没有知识链；答案要么只有一句结论，要么像论文综述，难以口述。

本仓库按真实算法面试的思路组织：

**原理 → 输入输出维度 → 为什么这样设计 → 怎么训练 → 怎么推理 → 如何优化 → 如何评测 → 如何落到业务。**

每个问题的答案尽量控制在 1–3 分钟可以讲清，同时保留继续追问所需的公式、shape、工程细节和常见误区。

## 完整目录

| 模块 | 重点 | 题量 |
|---|---|---:|
| [00 Roadmap](./00_Roadmap/README.md) | 学习顺序与知识地图 | — |
| [01 Transformer & LLM Fundamentals](./01_Transformer_LLM_Fundamentals/README.md) | Attention、RoPE、GQA、MoE、KV Cache | 18 |
| [02 Vision Fundamentals](./02_Vision_Fundamentals/README.md) | CNN、ViT、CLIP、SigLIP、DINO、视觉 token | 16 |
| [02B Detection / Segmentation / Grounding](./02B_Detection_Segmentation_Grounding/README.md) | YOLOv8–11/26、DETR、RT-DETR、SAM2、GroundingDINO、Grounded SAM | 22 |
| [03 Multimodal Core Architecture](./03_Multimodal_Core_Architecture/README.md) | Projector、Q-Former、Resampler、动态分辨率、融合 | 18 |
| [04 Representative Models 2026](./04_Representative_Models_2026/README.md) | Qwen3/3.5、InternVL、GLM、Seed、Kimi、MiniCPM、Omni | 20 |
| [05 Multimodal Data Engineering](./05_Multimodal_Data_Engineering/README.md) | 数据获取、清洗、去重、配比、合成、污染 | 16 |
| [06 Pretraining / SFT / PEFT](./06_Pretraining_SFT_PEFT/README.md) | 对齐、预训练、SFT、LoRA、冻结/解冻 | 18 |
| [07 Post-training / RL / Reasoning](./07_PostTraining_RL_Reasoning/README.md) | DPO、RLHF、GRPO、RLVR、视觉推理 | 20 |
| [08 Video / Audio / Omni](./08_Video_Audio_Omni/README.md) | 长视频、时间建模、音频、全双工 | 14 |
| [09 RAG / Tools / Agents / GUI / VLA](./09_RAG_Tools_Agents_GUI_VLA/README.md) | Function Call、MCP、GUI Agent、VLA | 18 |
| [10 Distributed Training](./10_Distributed_Training/README.md) | DDP、FSDP2、TP、PP、EP、ZeRO、Checkpoint | 18 |
| [11 Inference & Serving](./11_Inference_Serving_Optimization/README.md) | Prefill/Decode、vLLM、SGLang、量化、FlashAttention | 20 |
| [12 Evaluation & Diagnostics](./12_Evaluation_Diagnostics/README.md) | MMMU、MathVista、OCR、视频、Agent、幻觉诊断 | 16 |
| [13 Code Handwriting](./13_Code_Handwriting/README.md) | Attention、RoPE、LoRA、Projector、loss、KV 估算 | 15 |
| [14 System Design](./14_System_Design/README.md) | 多模态搜索、文档 QA、视频 QA、GUI Agent 等 | 15 |
| [15 Project Interview](./15_Project_Interview/README.md) | 项目介绍、消融、数据闭环、故障排查 | 12 |
| [16 高频题索引](./16_High_Frequency_Interview/README.md) | 面试前快速抽题 | 100+ |
| [17 2026-08 技术快照](./17_2026_Snapshot/README.md) | 最新模型与技术趋势 | — |
| [18 Primary References](./18_References/README.md) | 原论文 / 官方 GitHub / 官方文档 | — |
| [19 30-Day Review Plan](./19_30_Day_Review_Plan/README.md) | 30 天冲刺复习计划 | — |

## 面试万能回答框架

### 模型结构题

1. **输入是什么？** 例如 `[B, 3, H, W]`、视频 `[B,T,3,H,W]`。
2. **怎么变 token / feature map？** ViT 常是 `[B,N,D]`；detector 常保留 P3/P4/P5 多尺度 feature maps。
3. **任务头是什么？** LLM projector、detection head、object queries、mask decoder 还是 tool interface。
4. **在哪里做跨模态交互？** 拼接 self-attention、cross-attention、region-text alignment 或 language-guided queries。
5. **怎么训练？** 预训练、SFT、matching、box/mask loss、偏好优化/RL，各阶段哪些参数冻结。
6. **怎么算成本？** 视觉 token、feature-map resolution、prefill、KV cache、NMS、MoE active params、并行通信。

### 数据题

**目标能力 → 数据寻源 → 解析 → 清洗 → 去重 → 质量打分 → 配比 → 合成/伪标签 → 训练反馈 → 再迭代。**

### 系统题

**SLO → 模型/数据规模 → 显存预算 → 并行方式 → batch/scheduling → kernel/cache → 视觉工具链 → 监控 → 降级。**

## 可信度规则

- 最新模型只采用 **论文、官方 GitHub、官方技术报告、官方文档** 可确认的信息。
- 对 GPT / Gemini / Claude 等闭源模型，**公开能力不等于公开内部架构**；官方未披露的 vision encoder、projector、训练数据和 loss 不猜。
- YOLO 的版本号不等于同一团队的线性 lineage；先核对论文/官方实现来源。
- benchmark 数字会随评测设置变化；仓库重点解释机制，不靠排行榜背诵。

## 推荐使用方式

- **第一遍**：00 → 01 → 02 → **02B** → 03，先打通 LLM + Vision + Detection/Segmentation/Grounding 底层。
- **第二遍**：04 → 05 → 06 → 07，掌握 2026 多模态主线。
- **第三遍**：08 → 09 → 10 → 11，补 Agent 与工程。
- **第四遍**：13 手写 + 14 系统设计 + 15 项目面试。
- **面试前**：16 高频题 + 17 技术快照。

## Status

**Final 2026-08 interview edition.** 已补齐 YOLO、DETR、SAM、GroundingDINO 等视觉感知基础；后续只补新增的重要模型、论文和真实面试问题。