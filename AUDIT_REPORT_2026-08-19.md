# Repository Audit — 2026-08-19

This report records the structural/content audit performed after the 2026-08 knowledge-base expansion.

## Scope

Audited layers:

1. Math / classical ML / deep learning / PyTorch-CUDA foundations;
2. Transformer / LLM fundamentals;
3. Vision backbones and pretraining;
4. Detection / segmentation / grounding;
5. OCR / document AI;
6. Pose / tracking / motion;
7. Depth / 3D geometry;
8. Speech / audio;
9. MLLM architecture and representative 2026 models;
10. Multimodal generation / world models;
11. Data / pretraining / SFT / RL / safety;
12. Retrieval / RAG / agents / GUI / VLA / Omni;
13. Distributed training / serving;
14. Evaluation / code / system design / project interview.

## Audit criteria

- knowledge dependency is coherent;
- major interview domains are not missing;
- understanding, generation, perception and systems are balanced;
- rapidly changing model claims use primary sources;
- closed-source/internal architecture is not guessed;
- relative Markdown navigation is valid;
- numbered modules contain a README;
- future updates follow a written policy.

## Content changes made in this audit

- Added Machine Learning Fundamentals.
- Added PyTorch & CUDA Engineering.
- Added Vision Backbones & Visual Pretraining.
- Completed semantic/instance/panoptic segmentation fundamentals.
- Added optical flow, SOT, SLAM/VIO, NeRF, 3D Gaussian Splatting and sensor calibration.
- Added Speech & Audio Fundamentals.
- Added Multimodal Generation & World Models.
- Added Multimodal Safety & Reliability.
- Added Retrieval & Vector Search fundamentals.
- Added advanced data, training, RL, distributed, serving, evaluation and code notes.
- Updated the Qwen lineage through Qwen3.8 and added InternVL-U as a unified understanding/generation example.
- Added automated repository audit workflow.

## Machine audit

The GitHub Actions workflow `Knowledge Base Audit` is used as the final structural check. Final status is recorded after the workflow run completes.
