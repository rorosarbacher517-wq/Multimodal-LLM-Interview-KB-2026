# 00 · Roadmap：多模态算法岗知识地图

## 一张图理解整个知识链

```text
数学直觉 / PyTorch Tensor
    ↓
Deep Learning Fundamentals
Forward / Backward / Loss / Optimizer / Norm / Residual / Mixed Precision
    ↓
Transformer / LLM
Tokenizer / Embedding / Attention / RoPE / GQA / KV Cache / MoE
    ↓
Vision Fundamentals
CNN / ViT / CLIP / SigLIP / DINO
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
Multimodal Pretrain → SFT → Preference/RL
    ↓
Reasoning / RAG / Agent / GUI / VLA / Omni
    ↓
FSDP / TP / PP / EP → vLLM / SGLang
    ↓
Evaluation / System Design / Project Interview
```

## 第零层：Deep Learning 基础必须先补齐

在进入 Transformer 之前，至少要能解释：

- Tensor shape 和 matrix multiplication；
- broadcasting；
- forward / backward / computational graph；
- chain rule 和 gradient；
- MSE / Cross Entropy / KL；
- ReLU / GELU / SiLU；
- SGD / Momentum / Adam / AdamW；
- warmup / cosine / weight decay；
- BatchNorm / LayerNorm / RMSNorm；
- residual connection；
- gradient accumulation / clipping；
- FP16 / BF16 / mixed precision；
- parameter / gradient / optimizer / activation 显存。

对应模块： [00B Deep Learning Fundamentals](../00B_Deep_Learning_Fundamentals/README.md)

如果这些不熟，后面的 Pre-Norm、SwiGLU、LoRA、FSDP、FlashAttention 很容易只剩名词。

## 第一层：Transformer / LLM 必须能从零画出来

至少能闭卷画：

```text
Text
↓ Tokenizer
Token IDs [B,L]
↓ Embedding
[B,L,D]
↓ Transformer Blocks
[B,L,D]
↓ LM Head
[B,L,V]
↓ Sampling
Next Token
```

并解释：

- BPE / SentencePiece 为什么需要；
- Q/K/V 的 shape；
- `QK^T` 为什么得到 `[B,H,L,L]`；
- 为什么除以 `sqrt(d_k)`；
- causal mask / padding mask；
- residual / RMSNorm / FFN / SwiGLU；
- RoPE；
- MHA / MQA / GQA；
- KV Cache；
- teacher forcing / next-token loss；
- prefill / decode；
- top-k / top-p / temperature；
- dense / sliding-window / linear-recurrent attention；
- MoE routing / active parameters。

对应模块： [01 Transformer & LLM Fundamentals](../01_Transformer_LLM_Fundamentals/README.md)

## 第二层：视觉感知底座必须完整

### Vision Fundamentals

- CNN / receptive field；
- ViT / patchify；
- CLIP / SigLIP；
- DINO / self-supervised visual representation；
- image → visual token 的 shape。

### Detection / Segmentation / Grounding

- YOLO 的 P3/P4/P5；
- DETR / Hungarian matching；
- SAM / prompt encoder；
- GroundingDINO / text phrase → box。

### OCR / Document AI

- text detection vs recognition；
- CTC / autoregressive recognition；
- layout / reading order；
- PaddleOCR-VL / MinerU coarse-to-fine；
- Document RAG metadata。

### Pose / Tracking

- top-down / bottom-up pose；
- heatmap / SimCC；
- ByteTrack / Kalman / Hungarian / ReID；
- object tracking / point tracking / optical flow。

### Depth / 3D Perception

- relative vs metric depth；
- `Z=fB/d`；
- intrinsics / extrinsics；
- point / voxel / pillar / BEV；
- DUSt3R / MASt3R / VGGT；
- 3D geometry → VLA / world model。

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
[B, L_total, Dl]
     ↓
LLM
     ↓
Text / Coordinates / Tool Call / Action
```

你必须能解释：

- `N` 从哪里来；
- 为什么 `N'` 可能更小；
- 为什么 `Dv → Dl`；
- image/video 的 position 怎么编码；
- visual token 增加后为什么 prefill 和 KV cache 变贵；
- 什么时候调用 YOLO/SAM/OCR/depth/tracker，而不是只靠 VLM 内部感知。

## 第四层：2026 必须掌握的变化

- native / dynamic resolution；
- visual-token compression / routing；
- Qwen3-VL 的 DeepStack、Interleaved-MRoPE、timestamp alignment；
- InternVL3.5 的 ViR / DvD；
- multimodal reasoning + RLVR；
- long-video active perception；
- GUI / computer-use agent；
- full-duplex Omni；
- PaddleOCR-VL / MinerU 的 Document AI；
- VGGT-Ω / point-cloud foundation model；
- hybrid attention / recurrent architectures；
- efficient serving / multimodal caching。

## 第五层：算法工程必须落地

至少会算：

- Linear 参数量；
- Attention QKV shape；
- KV cache；
- Adam 训练显存；
- activation memory；
- visual token 数；
- YOLO feature-map 尺寸；
- point-cloud / voxel / BEV tensor；
- LoRA 参数量；
- FSDP/TP/PP/EP 各切什么。

至少会排查：

- loss 不下降；
- NaN / Inf；
- gradient 为 0；
- train/val gap；
- OOM；
- long-sequence prefill；
- tracker association error；
- document OCR/layout/reading-order error；
- 3D coordinate-frame error。

## 最推荐的复习顺序

### Phase 1：真正的底层

**00B Deep Learning → 01 Transformer/LLM**

### Phase 2：视觉感知

**02 Vision → 02B Detection → 02C OCR → 02D Pose/Tracking → 02E Depth/3D**

### Phase 3：多模态模型

**03 Architecture → 04 Models → 05 Data → 06 Pretrain/SFT → 07 RL**

### Phase 4：Agent 与工程

**08 Video/Omni → 09 Agent → 10 Distributed → 11 Serving**

### Phase 5：面试化

**12 Evaluation → 13 Handwriting → 14 System Design → 15 Project → 16/16A/16B 高频题**

## 一个判断标准

对任何一个新模型，不要先背模型名。优先回答：

1. 输入是什么？
2. tensor / token / feature shape 怎么变？
3. 核心计算是什么？
4. 为什么需要这个结构？
5. loss 怎么定义？
6. 参数怎么更新？
7. 推理是否需要 cache / post-processing / memory / geometry？
8. 主要计算和显存花在哪里？
9. 它在完整系统中接在什么位置？
