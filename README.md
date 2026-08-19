# Multimodal-LLM-Interview-KB-2026

> 面向 2026 秋招 / 社招的 **多模态大模型算法面试知识库**  
> 更新基线：**2026-08**  
> 目标：**简单、清楚、能讲出来，但不省略关键原理。**

本项目参考 `DeepLearing-Interview-Awesome-2024` 的“专题化知识库 + 面试题入口”思路，但做了三项调整：

1. **每个问题对应独立答案文件**，不再让几十个问题全部跳到一个超长 `Reference.md`。
2. 从“传统深度学习题库”升级为 **MLLM / VLM / Omni / Agent / Reasoning / Systems** 主线。
3. 对 2025–2026 模型只采用**论文、官方 GitHub、官方文档**可确认的信息；闭源架构不猜。

## 模块

| 模块 | 问题数 |
|---|---:|
| [01 Fundamentals](./01_Fundamentals/README.md) | 9 |
| [02 Architectures](./02_Architectures/README.md) | 11 |
| [03 Data](./03_Data/README.md) | 7 |
| [04 Training](./04_Training/README.md) | 8 |
| [05 Reasoning](./05_Reasoning/README.md) | 6 |
| [06 Video Audio Omni](./06_Video_Audio_Omni/README.md) | 5 |
| [07 Agents](./07_Agents/README.md) | 5 |
| [08 Training Inference Systems](./08_Training_Inference_Systems/README.md) | 8 |
| [09 Evaluation](./09_Evaluation/README.md) | 6 |
| [10 Code Handwriting](./10_Code_Handwriting/README.md) | 5 |
| [11 高频面试题](./11_High_Frequency_Interview/README.md) | 20 |
| [12 2026-08 技术快照](./12_2026_Snapshot/README.md) | 持续更新 |
| [13 参考资料](./13_References/README.md) | Primary sources |

## 推荐面试回答模板

遇到任何模型结构题，优先按下面 5 步回答：

**1. 输入是什么？**  
图像 / 视频 / 音频 / 文本，原始 shape 是什么。

**2. 怎么变成 token？**  
Vision/audio encoder 后是 `[B, N, D_v]` 还是其他形式。

**3. 怎么接 LLM？**  
MLP / Q-Former / Resampler / early fusion / cross-attention。

**4. loss 怎么训练？**  
自回归 CE、masked SFT、grounding loss、DPO/RL/RLVR。

**5. 推理为什么快/慢？**  
视觉 token、prefill、KV cache、MoE、量化、并行与 serving。

## 2026 面试重点

- Native / dynamic resolution
- Visual-token compression & routing
- MRoPE / temporal alignment
- Deep visual feature fusion
- MoE + Expert Parallelism
- Multimodal reasoning + RLVR/GRPO
- Long-video active navigation
- Omni-modal real-time speech
- GUI / Computer-use agents
- Multimodal RAG
- FSDP2 / vLLM multimodal serving
- FlashAttention-4 / Blackwell
- 闭源模型：**公开能力 ≠ 公开架构**

## 使用方式

- 第一遍：按 Roadmap 顺序阅读。
- 第二遍：只看“面试一句话”，强迫自己口述。
- 第三遍：从高频题索引随机抽题。
- 第四遍：手写 `10_Code_Handwriting`。
- 面试前：复习 `12_2026_Snapshot`。

## 可信度原则

- 不写“据说某闭源模型内部用了某模块”。
- 数字、模型能力、架构更新优先回到原论文/官方文档。
- 论文没有公开的训练数据量、hidden size、loss，不自行补全。
- 代码示例用于解释核心机制，不等价于官方实现。

## License

建议使用 MIT License；正式推到 GitHub 后可再补充 LICENSE 文件。
