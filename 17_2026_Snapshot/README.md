# 17 · 2026-08 Multimodal AI Snapshot

> 截止 2026-08，只记录有官方仓库/论文支撑、且对算法面试真正有价值的变化。

## 1. 从“外挂视觉塔”走向 Native Multimodal Foundation

Qwen3.5 官方强调 Unified Vision-Language Foundation 和更统一的多模态训练。多模态正在从“在文本 LLM 外加 vision adapter”走向 foundation-model 级统一训练。

- Official: https://github.com/QwenLM/Qwen3.6

## 2. Qwen3-VL：高分辨率 + 多层视觉特征 + 时间对齐

公开技术报告的重要升级包括 Interleaved-MRoPE、DeepStack 和 text-based timestamp alignment。

- Paper: https://arxiv.org/abs/2511.21631
- Repo: https://github.com/QwenLM/Qwen3-VL

## 3. Qwen3-Omni：从 VLM 走向实时 Omni

Qwen3-Omni 公开采用 MoE-based Thinker–Talker，处理 text/image/audio/video，并支持实时 text/speech 输出。

- Official: https://github.com/QwenLM/Qwen3-Omni

## 4. InternVL3.5：模型设计开始直接面向 Serving

InternVL3.5 同时提出 Cascade RL、Visual Resolution Router 和 Decoupled Vision-Language Deployment。

- Paper: https://arxiv.org/abs/2508.18265

## 5. GLM-V：Native Multimodal Agent

GLM-V 路线把视觉感知更直接地放入 reasoning、planning、tool use、execution。

- Repo: https://github.com/zai-org/GLM-V
- GLM-5V-Turbo: https://arxiv.org/abs/2604.26752

## 6. MiniCPM-V：Visual Token Compression 进入端侧核心

轻量 VLM 的优化已经不只是 LLM quantization，也包括视觉 token 数、vision compute 和端侧 pipeline。

- Official: https://github.com/OpenBMB/MiniCPM-V

## 7. Omni：Full-Duplex Real-time Interaction

实时系统需要同时处理 streaming input/output、用户打断、turn-taking 和多模态同步。

## 8. Seed / Kimi 等模型强调 Data + Model + Agent 一体化

2025–2026 的公开模型越来越把 grounding、video、GUI、agent data 放入同一能力链，而不是把视觉只当静态 VQA。

## 9. Multimodal Retrieval 成为独立基础能力

Embedding / Reranker 开始统一 text、image、document image、video，用于 multimodal RAG。

## 10. Test-time Scaling 与 Active Perception

能力扩展不再只靠参数，也在扩展 inference-time compute、visual lookback、crop/zoom/retrieval 和 verifier。

## 11. FlashAttention-4：模型和硬件共同设计

2026 FlashAttention-4 针对 Blackwell GPU 进一步重构 attention pipeline 和数据搬运。

- Paper: https://arxiv.org/abs/2603.05451

## 12. YOLO26：实时检测也走向 End-to-End

Ultralytics 2026 的 YOLO26 默认采用 **NMS-free end-to-end inference**，并移除 DFL regression；公开训练配方还包含 Progressive Loss、STAL 与 MuSGD。

- Docs: https://docs.ultralytics.com/models/yolo26
- Paper: https://arxiv.org/abs/2606.03748

**面试关键词：** one-to-one head、NMS-free、DFL-free、edge deployment。

## 13. Open-Vocabulary Real-Time Detection：YOLOE-26

YOLOE-26 把文本/视觉/prompt-free detection & segmentation 与 YOLO26 的实时 NMS-free 路线结合。

- Docs: https://docs.ultralytics.com/models/yoloe

这说明开放词汇感知不再只是大型 Transformer detector 的能力，正在快速进入实时部署模型。

## 14. SAM 2 + GroundingDINO：视觉工具开始模块化组合

SAM 2 使用 streaming memory 做 image/video promptable segmentation；GroundingDINO / DINO-X 提供 text-to-box open-world grounding。Grounded SAM 2 把两者组合成 text → box → mask → tracking pipeline。

- SAM 2: https://github.com/facebookresearch/sam2
- GroundingDINO: https://github.com/IDEA-Research/GroundingDINO
- Grounded SAM 2: https://github.com/IDEA-Research/Grounded-SAM-2

**面试价值：** 自动标注、视频跟踪、GUI/robot perception tool、MLLM agent tool use。

## 15. 当前最重要的 10 条技术主线

1. Native multimodal pretraining；
2. Dynamic/native resolution；
3. Visual-token routing/compression；
4. Multimodal reasoning + RLVR；
5. Active perception / visual lookback；
6. Long-video retrieval + temporal grounding；
7. GUI/tool/agent integration；
8. Omni streaming + efficient serving；
9. Open-vocabulary detection / grounding；
10. Promptable segmentation + model-in-the-loop data engine。

## 16. 哪些内容不要编？

对闭源模型或未充分披露版本：vision encoder、hidden size、projector、MoE routing、pretraining data composition、loss，如果官方未披露，就明确 unknown / not publicly disclosed。

对于 YOLO11 等没有正式论文的版本，架构细节优先引用官方 YAML/docs；对于 Grounding DINO 1.6 等后续服务版本，如果没有同等完整论文，不自行推断训练配方。

**截至 2026，可信地说清楚公开事实，比背一份看似完整但混有猜测的架构表更重要。**