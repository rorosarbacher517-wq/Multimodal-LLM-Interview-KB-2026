# Repository Audit — 2026-08-19

This report records the structural and content audit of the 2026 multimodal-algorithm interview knowledge base.

## Overall conclusion

The repository now has a coherent dependency chain:

```text
Math
→ Machine Learning / Deep Learning / PyTorch-CUDA
→ Transformer / LLM
→ Vision / Audio Perception
→ MLLM Architecture
→ Multimodal Generation / World Models
→ Data / Training / RL / Safety
→ Retrieval / Agent / VLA / Omni
→ Distributed / Serving
→ Evaluation / Code / System Design / Project Interview
```

The earlier structure was already strong for MLLM understanding and visual perception, but it was under-covered in classical ML, PyTorch/CUDA engineering, segmentation fundamentals, audio, multimodal generation/world models, retrieval internals, safety, and several large-scale training/serving details. Those gaps were filled in this audit.

## Scope reviewed

1. AI math, classical ML, deep learning and PyTorch/CUDA;
2. Transformer / LLM fundamentals;
3. Vision backbones and visual pretraining;
4. Detection / semantic-instance-panoptic segmentation / grounding;
5. OCR / document AI;
6. Pose / SOT / MOT / optical flow / point tracking;
7. Depth / camera geometry / SfM / SLAM / point cloud / BEV / NeRF / 3DGS;
8. Speech / ASR / speaker / codec / TTS;
9. MLLM architecture and representative 2026 models;
10. Diffusion / DiT / Flow / unified generation / world models;
11. Data / pretraining / SFT / RL / safety;
12. Retrieval / vector search / RAG / agents / GUI / VLA / Omni;
13. Distributed training / inference serving;
14. Evaluation / code / system design / project interview.

## Main improvements made

- Added `00C Machine Learning Fundamentals`.
- Added `00D PyTorch & CUDA Engineering`.
- Added `02A Vision Backbones & Visual Pretraining`.
- Completed semantic / instance / panoptic segmentation, U-Net, Mask R-CNN, Mask2Former, segmentation losses and metrics.
- Added RAFT optical flow and single-object tracking.
- Added SLAM/VIO, NeRF, 3D Gaussian Splatting and sensor calibration/fusion.
- Added `08A Speech & Audio Fundamentals`.
- Added `03B Multimodal Generation & World Models`.
- Added `07B Multimodal Safety & Reliability`.
- Added `09A Retrieval & Vector Search`.
- Added advanced notes for data infrastructure, training engineering, RL math/rollouts, distributed systems, serving, evaluation statistics and code drills.
- Updated the Qwen lineage through Qwen3.8 and added InternVL-U as a verified unified understanding/generation example.
- Rebuilt the root README and Roadmap around knowledge dependencies rather than a flat model list.
- Added automated repository auditing and an explicit update policy.

## Fast-moving facts specifically rechecked

- Qwen3.5 / 3.6 / 3.8 wording is grounded in the current official `QwenLM/Qwen3.8` repository; the knowledge base no longer treats a redirected `Qwen3.6` URL as the primary source.
- Qwen3-VL retains the publicly documented DeepStack / Interleaved-MRoPE / timestamp-alignment framing.
- InternVL3.5 is kept for ViR / Cascade RL / DvD; InternVL-U is separated as a unified understanding + generation model rather than being mixed into the InternVL3.5 architecture description.
- Rapidly changing closed or partially disclosed models are described only to the level supported by official reports/model cards.

## Machine audit result

GitHub Actions workflow: **Knowledge Base Audit — run #3 — SUCCESS**.

```text
Markdown files: 134
Explicit Q headings: 737
Standalone topic files: 98
Broken relative links: 0
Top-level modules missing README: 0
TODO/TBD/FIXME markers: 0
Duplicate normalized question titles: 5 (warnings only)
```

The five duplicate-title warnings are intentional cross-layer concepts rather than broken structure:

1. `Gradient` — mathematical definition vs deep-learning training interpretation;
2. `KL Divergence` — information-theory definition vs deep-learning use;
3. `Bias–Variance` — generic DL/generalization view vs classical-ML model-selection view;
4. `Sequence Packing` — Transformer concept vs multimodal training-engineering constraints;
5. `KV Cache memory` — model-level formula vs serving-capacity budgeting.

These are retained because the same concept is useful at different abstraction levels. The policy now requires their surrounding explanation to be different rather than duplicated verbatim.

## Remaining scope boundary

The repository is now sufficiently systematic for a **multimodal / large-model algorithm candidate**. It intentionally does not become a complete CS encyclopedia. Full LeetCode algorithms, operating systems, database internals and computer networking should remain separate preparation tracks.

## Maintenance rule

Future additions should answer one question first: **does this introduce a new reusable concept, or is it only a newer model name / leaderboard update?** Only the former deserves new core knowledge content.
