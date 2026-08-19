# 00 · Roadmap：多模态算法岗知识地图

## 一张图理解整个知识链

```text
数学 / PyTorch
    ↓
Transformer / LLM
    ↓
CNN / ViT / CLIP / SigLIP / DINOv2
    ↓
Detection / Segmentation / Grounding
YOLO / DETR / RT-DETR / SAM / GroundingDINO
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
- RoPE、GQA、KV Cache、MoE 各解决什么问题？
- 图像怎么从 `[3,H,W]` 变成视觉 token？
- YOLO 为什么要 P3/P4/P5 多尺度检测？
- NMS、one-to-many、one-to-one matching 有什么关系？
- SAM 为什么可以用 point / box / mask 做 prompt？
- GroundingDINO 为什么能把自然语言短语映射到 box？
- Vision Encoder 和 LLM hidden size 不一样怎么办？

如果这些说不清，多模态模型结构题很容易变成背模型名。

## 第二层：必须能画出两类视觉链路

### A. MLLM

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

### B. Grounded Perception

```text
Image → detector / grounding model → boxes
Text ────────────────────────────────↑
                         ↓
                      SAM / SAM2
                         ↓
                     pixel masks
```

你必须能够解释：

- `N` 从哪里来；
- 为什么 `N'` 可能比 `N` 小；
- 为什么 detector 更喜欢保留多尺度 feature map；
- 640 输入为什么常得到 80×80 / 40×40 / 20×20；
- object queries 如何与 GT 匹配；
- prompt / box / mask 如何在 SAM 中交互；
- 最终 loss 到底监督谁。

## 第三层：2026 必须掌握的变化

- Dynamic / native resolution 与 visual-token compression。
- Qwen3-VL 的 DeepStack、Interleaved-MRoPE、timestamp alignment。
- InternVL3.5 ViR 与 vision-language decoupled serving。
- YOLO26 的 end-to-end NMS-free、DFL-free 路线。
- YOLOE-26 / GroundingDINO / DINO-X 的 open-vocabulary perception。
- SAM 2 的 streaming memory 与视频对象传播。
- Grounded SAM 2 的 text → box → mask → tracking 工具链。
- RL 如何提升视觉 reasoning，而不是只让回答变长。
- GUI Agent 如何从 screenshot 走到 grounding / click / action。

## 第四层：算法工程必须能落地

至少会算：

- 参数显存；
- Adam 优化器显存；
- KV cache；
- visual token 数；
- attention 复杂度；
- LoRA 参数量；
- detector feature-map 尺寸；
- IoU / NMS；
- FSDP/TP/PP/EP 各切什么。

至少会解释：

- OOM 从哪里排查；
- 高分辨率输入如何影响 token/feature map；
- 自动标注如何用 GroundingDINO + SAM 产生伪标签；
- 为什么线上可用轻量 YOLO student，而 teacher 用更强 open-world model；
- vLLM / SGLang 如何管理多模态请求。

## 最推荐的复习顺序

### Week 1：底层视觉 + Transformer
01 Transformer → 02 Vision → **02B Detection/Segmentation/Grounding** → 03 Multimodal architecture

### Week 2：模型与训练
04 Representative models → 05 Data → 06 Pretrain/SFT → 07 RL

### Week 3：能力与工程
08 Video/Omni → 09 Agent → 10 Distributed → 11 Serving

### Week 4：面试化
12 Evaluation → 13 Handwriting → 14 System Design → 15 Project → 16 高频题

## 一个判断标准

对任何一个新视觉/多模态模型，不需要背全部参数。优先回答：

1. 输入是什么？
2. Backbone / Vision Encoder 是什么？
3. 空间分辨率和 token/feature-map 如何变化？
4. Head / Connector / Query / Prompt 是什么？
5. 训练时如何 assignment / matching / loss？
6. 是否 closed-set / open-vocabulary / promptable？
7. 推理是否需要 NMS、memory、tool call？
8. 成本主要在哪里？