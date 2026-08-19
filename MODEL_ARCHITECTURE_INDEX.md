# Model Architecture & Tensor-Dimension Index

> Purpose: add a **structure-first interview layer** to the existing knowledge base without rewriting the original notes.
>
> Rule: learn the **shared family skeleton first**, then memorize only the **version-specific delta**.

## Dimension notation

| Symbol | Meaning |
|---|---|
| `B` | batch size |
| `L` | text sequence length |
| `T` | video/audio time steps or frames |
| `N` | visual / point / latent token count |
| `D` | hidden dimension |
| `H,W` | spatial height / width |
| `C` | channel count |
| `K` | keypoints / classes / learned queries depending on context |
| `V` | vocabulary size |

**Important:** when a model family has many sizes (`n/s/m/l/x`, 2B/8B/32B, different ViT backbones, etc.), the diagrams use **symbolic dimensions** and only give fixed numeric shapes where the public architecture defines them. This prevents memorizing one checkpoint as if it were the whole family.

## Architecture supplements

1. [Deep-learning foundations: MLP / CNN / RNN / LSTM / GRU](./00B_Deep_Learning_Fundamentals/ARCHITECTURES_AND_DIMENSIONS.md)
2. [Classical ML model structures: Linear / Logistic / KNN / SVM / Trees / RF / GBDT / XGBoost / clustering / PCA](./00C_Machine_Learning_Fundamentals/MODEL_STRUCTURES_AND_DIMENSIONS.md)
3. [Transformer / LLM architectures](./01_Transformer_LLM_Fundamentals/ARCHITECTURES_AND_DIMENSIONS.md)
4. [Vision backbones & visual pretraining](./02A_Vision_Backbones_Pretraining/ARCHITECTURES_AND_DIMENSIONS.md)
5. [Detection / segmentation / grounding](./02B_Detection_Segmentation_Grounding/31_architectures_dimensions_innovations.md)
6. [OCR / Document AI](./02C_OCR_Document_AI/16_architectures_dimensions_innovations.md)
7. [Pose / tracking / motion](./02D_Pose_Tracking/19_architectures_dimensions_innovations.md)
8. [Depth / 3D perception / geometry](./02E_Depth_3D_Perception/25_architectures_dimensions_innovations.md)
9. [Multimodal core + representative VLM / Omni models](./04_Representative_Models_2026/ARCHITECTURES_AND_DIMENSIONS.md)
10. [Generative / diffusion / world-model architectures](./03B_Multimodal_Generation_World_Models/ARCHITECTURES_AND_DIMENSIONS.md)
11. [Speech / audio architectures](./08A_Speech_Audio_Fundamentals/ARCHITECTURES_AND_DIMENSIONS.md)

## How to memorize models

Use the same five questions for every architecture:

```text
1. Input tensor是什么？
2. Backbone/Encoder 如何改变 H/W/N/D？
3. 信息在哪里融合？
4. Head 输出什么 shape？
5. 新版本到底改了哪一个模块？
```

For interview review, the target is not to reproduce every implementation line. The target is to be able to draw the **data flow + tensor flow + innovation delta** from memory.

## Coverage principle

The supplement covers concrete model families named in the repository, from classical ML and neural-network foundations through Transformer/LLM, ResNet/ViT/Swin/ConvNeXt, CLIP/DINO/MAE/SigLIP, YOLO/DETR/SAM/GroundingDINO, OCR/Document models, pose/tracking models, depth/3D models, Flamingo/BLIP-2/LLaVA and representative 2026 VLM/Omni models, VAE/VQ-VAE/Diffusion/DiT/MMDiT, Whisper/wav2vec 2.0 and related speech models.

Algorithms, losses or protocols such as NMS, IoU, CTC itself, RAG, MCP and A2A are **not treated as standalone neural-network models**. They stay in their original conceptual modules. For system algorithms such as SORT/SLAM, the supplement shows the real data-flow pipeline rather than inventing a neural backbone.

For closed models whose internal vision encoder/projector/layer dimensions are not publicly disclosed, the supplement stops at the publicly documented interface and explicitly marks the internal architecture as **not publicly disclosed**.