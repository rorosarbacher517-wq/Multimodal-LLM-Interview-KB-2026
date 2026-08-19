# Audit & Update Policy

这个仓库不是按“模型越新越往里塞”的方式维护，而按**知识稳定性 + 面试价值 + 可核实性**维护。

## 1. 三类内容分开

### Stable fundamentals
数学、机器学习、深度学习、Transformer、CV 基础、概率、优化、经典算法。只在发现错误、表达不清或重要知识缺口时更新。

### Fast-moving implementation
PyTorch、CUDA、FSDP、vLLM/SGLang、量化、serving。必须优先引用官方文档，并区分稳定概念与可能随版本变化的具体 API。

### Fast-moving models
2025–2026 模型卡、技术报告和 release。只写论文、官方 GitHub、官方 model card 可确认的内容；未披露的 vision encoder、hidden size、训练数据、loss 不猜。

## 2. 新模型是否值得加入？
至少满足一项：
- 提出了值得面试的新结构或训练思想；
- 代表重要能力方向，如 native multimodal、Omni、GUI/VLA、generation；
- 官方开源且能从源码理解；
- 对训练、serving 或 data engineering 有明确方法价值。

只有排行榜更新、没有新增方法价值的版本，不必单独占大量篇幅。

## 3. 每个知识点推荐回答模板

```text
一句话
→ 输入/输出
→ 核心计算或结构
→ 为什么需要
→ shape / loss / complexity（适用时）
→ 常见追问
→ 易错点
→ primary source（新模型/具体实现）
```

## 4. 事实等级
- **Confirmed**：原论文、官方仓库、官方文档直接支持。
- **Implementation inference**：可从公开源码合理推导，必须说明是实现层解释。
- **Unknown**：官方未公开，不补全、不猜。

## 5. 自动审计
每次 push/PR 运行：

```bash
python scripts/audit_repo.py
```

Hard failure：
- broken relative links；
- 编号模块缺 README。

Warnings：
- duplicate question titles；
- 未完成的占位符标记。

重复题名不自动视为错误。数学定义与训练应用、模型原理与 serving 预算等跨层知识可以保留，但应确保两处回答视角不同，避免原文复制。

## 6. 内容边界
这个仓库目标是**多模态/大模型算法求职知识库**，不是所有 CS 课程的百科全书。

应覆盖：AI 数学、ML/DL、PyTorch/CUDA、Transformer、Vision/Audio/3D、MLLM、generation、data/training/RL、Agent/VLA、安全、分布式、serving、evaluation、code/system design。

LeetCode、操作系统、数据库、网络的完整课程不在此仓库展开，可作为独立求职仓库维护。
