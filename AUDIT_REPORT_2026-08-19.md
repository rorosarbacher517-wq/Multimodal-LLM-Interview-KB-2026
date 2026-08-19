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
→ Retrieval / RAG
→ Agent Loop / Tool / Planning / Memory / MCP / A2A
→ Web / GUI / Coding Agent / VLA / Omni
→ Distributed / Serving
→ Evaluation / Code / System Design / Project Interview
```

The earlier structure was already strong for MLLM understanding and visual perception. The first audit filled gaps in classical ML, PyTorch/CUDA engineering, segmentation, audio, multimodal generation/world models, retrieval internals, safety and large-scale systems. The Agent expansion then filled the remaining gap between “RAG/GUI overview” and a production-grade Agent knowledge stack.

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
12. Retrieval / vector search / RAG;
13. Agent loop / tool use / planning / memory / multi-agent / MCP / A2A;
14. Web / GUI / coding agents / VLA / Omni;
15. Agent data / Agent RL / Agent evaluation / Agent system design;
16. Distributed training / inference serving;
17. Evaluation / code / system design / project interview.

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
- Added `09B Agent Fundamentals & Engineering`.
- Added `16C Agent High Frequency` with a dedicated closed-book Agent interview checklist.
- Added `AGENT_DATA.md`, `AGENT_RL.md`, `AGENT_EVAL.md` and `AGENT_SYSTEM_DESIGN.md` in the modules where those topics logically belong.
- Added current Agent protocol/runtime material: MCP 2026-07-28, A2A, harness/sandbox separation, durable execution and long-horizon executable evaluation.
- Updated the Qwen lineage through Qwen3.8 and added InternVL-U as a verified unified understanding/generation example.
- Rebuilt the root README and Roadmap around knowledge dependencies rather than a flat model list.
- Added automated repository auditing and an explicit update policy.

## Fast-moving facts specifically rechecked

- Qwen3.5 / 3.6 / 3.8 wording is grounded in the current official `QwenLM/Qwen3.8` repository.
- Qwen3-VL retains the publicly documented DeepStack / Interleaved-MRoPE / timestamp-alignment framing.
- InternVL3.5 is kept for ViR / Cascade RL / DvD; InternVL-U is separated as a unified understanding + generation model.
- MCP 2026-07-28 is described from the official MCP specification update, including stateless core, MRTR, header routing, cacheable list results and authorization hardening.
- A2A is described as an Agent interoperability layer and kept conceptually separate from MCP and ordinary function calling.
- Harness/sandbox separation and durable execution are framed as Agent runtime engineering principles and are grounded in the public 2026 Agents SDK update.
- Rapidly changing closed or partially disclosed models are described only to the level supported by official reports/model cards.

## Machine audit result

GitHub Actions workflow: **Knowledge Base Audit — Agent expansion validation run #10 — SUCCESS**.

```text
Markdown files: 141
Explicit Q headings: 862
Standalone topic files: 103
Broken relative links: 0
Top-level modules missing README: 0
Placeholder markers: 0
Duplicate normalized question titles: 8 (warnings only)
```

The duplicate-title warnings are cross-layer concepts rather than broken navigation. Five already existed intentionally:

1. `Gradient` — mathematical definition vs deep-learning training interpretation;
2. `KL Divergence` — information-theory definition vs deep-learning use;
3. `Bias–Variance` — generic DL/generalization view vs classical-ML model-selection view;
4. `Sequence Packing` — Transformer concept vs multimodal training-engineering constraints;
5. `KV Cache memory` — model-level formula vs serving-capacity budgeting.

Three additional Agent-era overlaps are also intentional:

6. `Function Calling` — application overview vs Agent runtime/tooling interpretation;
7. `Least Privilege` — general multimodal safety vs production Agent permission design;
8. `Cost-normalized Evaluation` — general system evaluation vs trajectory-level Agent success/cost analysis.

These are retained because the same concept is useful at different abstraction levels. The policy requires the surrounding explanation to be different rather than duplicated verbatim.

## Remaining scope boundary

The repository is now sufficiently systematic for a **multimodal / large-model / Agent algorithm candidate**. It intentionally does not become a complete CS encyclopedia. Full LeetCode algorithms, operating systems, database internals and computer networking should remain separate preparation tracks.

## Maintenance rule

Future additions should answer one question first: **does this introduce a new reusable concept, or is it only a newer model name / leaderboard update?** Only the former deserves new core knowledge content.
