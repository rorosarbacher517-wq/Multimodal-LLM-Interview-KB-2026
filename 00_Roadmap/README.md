# 00 · Roadmap：多模态算法岗知识地图

## 一张图理解整个知识链

```text
数学 / PyTorch
    ↓
Transformer / LLM
    ↓
ViT / CLIP /视觉编码
    ↓
Vision Encoder → Connector → LLM
    ↓
动态分辨率 / 视频 / 音频 / MoE
    ↓
Multimodal Pretrain → SFT → Preference/RL
    ↓
Reasoning / Grounding / OCR / Agent
    ↓
FSDP / TP / PP / EP → vLLM / SGLang
    ↓
Evaluation / System Design / Project Interview
```

## 第一层：必须能从零解释

- Self-Attention 为什么能建模长距离依赖？
- `Q/K/V` 的 shape 怎么变化？
- Multi-Head Attention 为什么要多头？
- RoPE、GQA、KV Cache、MoE 各解决什么问题？
- 图像怎么从 `[3,H,W]` 变成视觉 token？
- Vision Encoder 和 LLM hidden size 不一样怎么办？

如果这些说不清，多模态模型结构题很容易变成背模型名。

## 第二层：必须能画出一个 MLLM

```text
Image / Video
     ↓
Vision Encoder
[B, N, Dv]
     ↓
Projector / Resampler
[B, N', Dl]
     ↓
Visual Tokens + Text Tokens
[B, L, Dl]
     ↓
LLM
     ↓
Text / Coordinates / Tool Call / Action
```

你必须能够解释：

- `N` 从哪里来；
- 为什么 `N'` 可能比 `N` 小；
- 为什么 `Dv` 要变成 `Dl`；
- image/video 的位置编码怎么做；
- 最终 loss 到底监督谁。

## 第三层：2026 必须掌握的变化

2024 的面试常问“LLaVA 是什么”；2026 更容易继续追问：

- 为什么模型开始做 **native / dynamic resolution**？
- 为什么视觉 token 压缩越来越重要？
- Qwen3-VL 的 **DeepStack、Interleaved-MRoPE、timestamp alignment** 分别解决什么？
- Qwen3.5 为什么从独立 VLM 走向 **native multimodal foundation model**？
- InternVL3.5 的 ViR 为什么既是模型问题也是系统问题？
- MoE 的 total params 和 active params 有什么区别？
- 如何通过 RL 提升视觉 reasoning，而不是只让回答变长？
- GUI Agent 如何从 screenshot 走到 click/action？
- 全双工 Omni 模型为什么比 ASR→LLM→TTS 串联更难？

## 第四层：算法工程必须能落地

至少会算：

- 参数显存；
- Adam 优化器显存；
- KV cache；
- visual token 数；
- attention 复杂度；
- LoRA 参数量；
- FSDP/TP/PP/EP 各切什么。

至少会解释：

- OOM 从哪里排查；
- 多模态 batch 为什么比文本 batch 更难做；
- 长视频为什么容易把 prefill 打爆；
- vLLM / SGLang 如何管理多模态请求；
- 为什么线上不能只追求 benchmark accuracy。

## 最推荐的复习顺序

### Week 1：底层
01 Transformer → 02 Vision → 03 Multimodal architecture

### Week 2：模型与训练
04 Representative models → 05 Data → 06 Pretrain/SFT → 07 RL

### Week 3：能力与工程
08 Video/Omni → 09 Agent → 10 Distributed → 11 Serving

### Week 4：面试化
12 Evaluation → 13 Handwriting → 14 System Design → 15 Project → 16 高频题

## 一个判断标准

对任何一个新模型，不需要背全部参数。只要能回答下面 8 个问题，就基本理解了：

1. Vision encoder 是什么？
2. 图像/视频如何 token 化？
3. Connector 是什么？有没有压 token？
4. 视觉 token 在哪里进入 LLM？
5. 位置和时间如何编码？
6. 训练分几阶段？
7. 后训练如何增强 reasoning/agent？
8. 推理成本主要在哪里？