# GroundingDINO 1.5 和 DINO-X 代表了什么演进？

## Grounding DINO 1.5

- 分为 **Pro** 与 **Edge**：一个强调 open-set generalization，一个强调边缘实时性。
- 公开报告扩大模型/视觉 backbone，并把 grounded training data 扩展到 **20M+ images**。
- 说明开放词汇 detector 的竞争重点已经从“能否 zero-shot”走向“泛化 + 速度 + 部署”。

## DINO-X

- 延续 GroundingDINO-style encoder-decoder object representation。
- 支持 **text prompt、visual prompt、customized prompt**。
- 引入 universal object prompt，可做 prompt-free open-world detection。
- Grounding-100M 将 grounded data 扩大到 100M 级样本。
- object-level representation 进一步连接 detection、segmentation、pose、caption、object QA。

## 易错点

Grounded-SAM-2 仓库已经列出 Grounding DINO 1.6 支持，但如果没有同等完整公开的论文/训练细节，不要自行补写内部结构。

## Primary sources

- https://arxiv.org/abs/2405.10300
- https://arxiv.org/abs/2411.14347
- https://github.com/IDEA-Research/Grounded-SAM-2
