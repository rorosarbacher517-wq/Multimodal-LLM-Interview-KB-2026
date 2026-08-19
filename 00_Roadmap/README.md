# 00 · Roadmap：多模态算法岗知识地图

## 一张图理解整个知识链

```text
数学 / PyTorch
    ↓
Transformer / LLM
    ↓
Vision Fundamentals
    ↓
Detection / Segmentation / Grounding
    ↓
OCR / Document AI
    ↓
Pose / Tracking
    ↓
Depth / 3D Perception
    ↓
Vision Encoder → Connector → LLM
    ↓
动态分辨率 / 视频 / 音频 / MoE
    ↓
Multimodal Pretrain → SFT → Preference/RL
    ↓
Reasoning / RAG / Agent / GUI / VLA
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
- CNN / ViT / CLIP / DINO 分别解决什么？

## 第二层：视觉感知底座必须完整

### Detection / Segmentation / Grounding

要会解释：

- YOLO 的 P3/P4/P5 为什么是多尺度；
- DETR 为什么用 Hungarian matching；
- SAM 为什么需要 prompt encoder；
- GroundingDINO 如何把 text phrase 对齐到 box。

### OCR / Document AI

要会解释：

- text detection 和 recognition 为什么分开；
- CTC 为什么不需要字符级对齐；
- layout / reading order 为什么属于文档结构而不是 OCR；
- PaddleOCR-VL / MinerU 为什么采用 layout + crop + recognition 的 coarse-to-fine pipeline；
- Document RAG 为什么必须保留 page/bbox/layout metadata。

### Pose / Tracking

要会解释：

- top-down / bottom-up pose；
- heatmap / SimCC；
- ByteTrack 为什么使用低分 detection；
- Kalman / Hungarian / ReID 分别负责什么；
- object tracking、point tracking、optical flow 的区别；
- CoTracker / SAM2 tracking 适合什么场景。

### Depth / 3D Perception

要会解释：

- relative vs metric depth；
- `Z=fB/d`；
- intrinsics / extrinsics / unprojection；
- point / voxel / pillar / BEV；
- PointPillars / CenterPoint / BEVFormer / BEVFusion；
- DUSt3R / MASt3R / VGGT 为什么改变传统 SfM pipeline；
- 3D geometry 为什么对 VLA / world model 重要。

## 第三层：必须能画出一个 MLLM

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
- 最终 loss 到底监督谁；
- 什么时候应该调用 YOLO/SAM/OCR/depth/tracker，而不是只靠 VLM 内部感知。

## 第四层：2026 必须掌握的变化

- native / dynamic resolution；
- visual-token compression / routing；
- Qwen3-VL 的 DeepStack、Interleaved-MRoPE、timestamp alignment；
- InternVL3.5 的 ViR / DvD；
- multimodal reasoning + RLVR；
- long-video active navigation；
- GUI / computer-use agent；
- full-duplex Omni；
- PaddleOCR-VL-1.6 / MinerU2.5-Pro 的 Document AI；
- VGGT-Ω 的 dynamic-scene 3D foundation modeling；
- point-cloud foundation encoder 与 2D–3D joint pretraining。

## 第五层：算法工程必须能落地

至少会算：

- 参数显存；
- Adam 优化器显存；
- KV cache；
- visual token 数；
- YOLO feature-map 尺寸；
- point-cloud / voxel / BEV tensor 大小；
- attention 复杂度；
- LoRA 参数量；
- FSDP/TP/PP/EP 各切什么。

至少会解释：

- OOM 从哪里排查；
- 多模态 batch 为什么难做；
- 长视频为什么容易把 prefill 打爆；
- tracker 的错误来自 detector 还是 association；
- document parser 的错误来自 OCR、layout 还是 reading order；
- 3D perception 的 coordinate frame 如何统一；
- 为什么线上不能只追求 benchmark accuracy。

## 最推荐的复习顺序

### Week 1：底层 + 视觉感知

01 Transformer → 02 Vision → 02B Detection → 02C OCR → 02D Pose/Tracking → 02E Depth/3D

### Week 2：多模态模型与训练

03 Multimodal architecture → 04 Representative models → 05 Data → 06 Pretrain/SFT → 07 RL

### Week 3：能力与工程

08 Video/Omni → 09 Agent → 10 Distributed → 11 Serving

### Week 4：面试化

12 Evaluation → 13 Handwriting → 14 System Design → 15 Project → 16 高频题

## 一个判断标准

对任何一个新视觉/多模态模型，不需要背全部参数。至少能回答：

1. 输入是什么？
2. Backbone / encoder 是什么？
3. feature/token 的 shape 怎么变？
4. 中间是否保留多尺度/空间坐标？
5. 输出是什么：box/mask/keypoint/depth/text/action？
6. loss / matching 怎么做？
7. 是否需要后处理 / memory / geometry？
8. 推理成本主要在哪里？
9. 它与 MLLM/Agent/VLA 在系统中如何连接？
