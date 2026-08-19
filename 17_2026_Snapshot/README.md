# 17 · 2026-08-19 Multimodal AI Snapshot

> 这里只放**变化快、但已有论文/官方仓库支持**、且对算法面试有方法价值的内容。稳定基础放前面的模块，不在这里重复。

## 1. Qwen3.5 → Qwen3.6 → Qwen3.8：当前 Qwen open-model lineage

Qwen 官方当前仓库为 `QwenLM/Qwen3.8`。官方说明：
- Qwen3.5：Unified Vision-Language Foundation、Gated Delta Networks + sparse MoE、scalable RL；
- Qwen3.6：在其基础上强调 agentic coding、thinking preservation 与稳定性；
- Qwen3.8：built on Qwen3.5 architectural foundation，重点提升 coding、professional work、research、long-horizon agents。

2026-08-12/14 分别公开 Qwen3.8-2.4T-A95B 与 Qwen3.8-27B。

**注意：** 不因为版本号更新就自行推断新的 vision encoder/projector。具体 checkpoint 的模态和内部实现按 model card。

Primary: https://github.com/QwenLM/Qwen3.8

## 2. Qwen3-VL：高分辨率、多层视觉特征、时间对齐

公开技术报告的关键点：
- Interleaved-MRoPE；
- DeepStack；
- text-based timestamp alignment；
- dense/MoE、长 interleaved multimodal context。

Primary: https://arxiv.org/abs/2511.21631

## 3. InternVL3.5：模型设计直接连 Serving

Cascade RL + Visual Resolution Router + Decoupled Vision-Language Deployment。

它说明“视觉分辨率”已经同时是**能力问题、token-budget 问题和服务负载问题**。

Primary: https://arxiv.org/abs/2508.18265

## 4. InternVL-U：理解与生成开始统一

公开 InternVL-U 路线把 multimodal understanding/reasoning 与 image generation/editing 放入同一约 4B 系统，并结合 MLLM 与 MMDiT-style generation head。

**面试趋势：** MLLM 不能只准备 VQA/grounding；Diffusion/DiT/Flow/Unified Generation 也进入知识栈。

Primary: https://arxiv.org/abs/2603.09877

## 5. Qwen3-Omni / Full-duplex：从 VLM 走向实时 Omni

Omni 模型需要 text/image/audio/video 的时间同步、streaming state、speech codec、turn-taking 与 interruption。

Qwen3-Omni: https://github.com/QwenLM/Qwen3-Omni

## 6. GLM-V：Native Multimodal Agent

公开路线强调视觉感知直接参与 reasoning、planning、tool use 与 execution。

Primary: https://github.com/zai-org/GLM-V

## 7. Seed1.5-VL：Data / Model / Agent 一体化

公开报告给出 532M vision encoder + 20B-active MoE LLM，并覆盖 OCR、grounding、3D、video、GUI/game agent。

对数据策略岗位尤其有价值，因为报告同时讨论 data construction 与 training。

Primary: https://arxiv.org/abs/2505.07062

## 8. MiniCPM-V 4.6：视觉 Token Compression 是端侧核心

官方路线公开 mixed `4×/16×` visual-token compression 与轻量视觉/语言 backbone。

趋势：VLM edge optimization 不只是 LLM INT4，也包括**视觉 token 数、vision compute、KV/prefill**。

Primary: https://github.com/OpenBMB/MiniCPM-V

## 9. YOLO26 / Open-Vocabulary Real-time Perception

Ultralytics YOLO26 公开路线强调 end-to-end NMS-free、DFL-free；YOLOE 等又把 open-vocabulary/promptable detection/segmentation 带入实时模型。

Primary: https://docs.ultralytics.com/models/yolo26/

## 10. SAM2 + GroundingDINO：Perception Toolchain 模块化

```text
text → GroundingDINO box → SAM2 mask → video propagation/tracking
```

这条链对 auto-labeling、GUI、robot perception、video annotation 都有直接意义。

SAM2: https://github.com/facebookresearch/sam2
GroundingDINO: https://github.com/IDEA-Research/GroundingDINO

## 11. Document AI：OCR → Structure Recovery → LLM-ready Parsing

现代文档系统不再只做字符识别，而是 layout、reading order、table/formula、multi-page structure、Markdown/JSON output 与 RAG 一体化。

PaddleOCR: https://github.com/PaddlePaddle/PaddleOCR
MinerU: https://github.com/opendatalab/MinerU

## 12. 3D Foundation：SfM Pipeline 正在被 Learned Geometry 重构

DUSt3R / MASt3R / VGGT 等把 correspondence、point-map、camera/depth prediction 更深地整合进 feed-forward learned system；同时 SLAM、NeRF、3DGS 仍是理解 3D world representation 的关键基础。

VGGT: https://github.com/facebookresearch/vggt

## 13. Multimodal Retrieval 成为独立基础能力

Text/image/document/video embedding + reranker 让 multimodal RAG 从“caption 图片后做 text search”升级为真正的跨模态 retrieval。

面试必须同时懂 BM25、dense embedding、ANN/HNSW/IVF-PQ、reranking 和 retrieval evaluation。

## 14. RL / Agent 正在把 Verifier 与 Rollout Infrastructure 变成核心

后训练已不只是“知道 DPO/GRPO 名字”。要理解：
- rollout generation；
- verifier/reward；
- advantage/KL；
- asynchronous inference-training；
- environment-level success。

## 15. Serving 从单体模型走向 Disaggregation

重要关键词：
- chunked prefill；
- prefill/decode disaggregation；
- vision encoder 与 LLM 拆池；
- multi-LoRA；
- multimodal feature cache；
- admission control。

## 16. Safety 的攻击面也变成 Multimodal

Image/PDF/website/tool result 都可能携带 indirect prompt injection。可靠 Agent 需要：instruction/data separation、least privilege、confirmation、sandbox、action verification、audit log。

## 17. Agent Protocol：Function Calling → MCP → A2A

2026 面试不能把三者混成一个概念：

```text
Function Calling
= 模型生成结构化工具调用

MCP
= Agent / model 与 tool / resource / data 的标准连接层

A2A
= Agent 与 Agent 的发现、通信和协作层
```

Google 在 A2A 的公开说明中明确把 A2A 定位为 Agent interoperability，并说明它与 MCP 的工具/上下文连接能力是互补关系。

A2A: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
2026 protocol guide: https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols/

## 18. MCP 2026-07-28：从“会用 MCP”转向理解协议工程

官方 2026-07-28 规范更新重点包括：
- stateless protocol core；
- Multi Round-Trip Requests；
- header-based routing；
- cacheable list results；
- authorization hardening；
- formal extensions / tasks。

面试价值：MCP 已经不仅是“一个工具协议名”，而开始涉及**负载均衡、路由、缓存、授权和可扩展协议设计**。

Primary: https://blog.modelcontextprotocol.io/posts/2026-07-28/

## 19. Agent Runtime：Harness + Sandbox + Durable Execution

2026 Agent 工程越来越强调把：

```text
Harness
instructions / tools / approvals / tracing / state

与

Sandbox
files / shell / code / isolated compute
```

分离。

OpenAI 2026 Agents SDK 的公开更新强调 native sandbox、harness-compute separation，以及通过 snapshot/rehydration 支持 durable execution。无论使用哪个框架，这背后的工程思想都值得掌握：**credential isolation、checkpoint/resume、failure recovery、long-horizon execution**。

Primary: https://openai.com/index/the-next-evolution-of-the-agents-sdk/

## 20. Agent Evaluation：从短任务转向 Long-Horizon Executable Workflows

OSWorld 2.0 把 computer-use 评测推进到更长、更真实的跨应用工作流，强调 dynamic environments、cross-source reasoning、implicit state、visual-spatial precision 和安全执行。

面试中不要只讨论 next-action accuracy，要看：
- end-to-end success；
- partial completion；
- steps / tool calls；
- cost / latency；
- recovery；
- safety。

OSWorld 2.0: https://arxiv.org/abs/2606.29537
BrowserGym: https://arxiv.org/abs/2412.05467

## 当前最值得持续追踪的 12 条主线
1. Native multimodal foundation training；
2. Dynamic/native resolution；
3. Visual-token routing/compression；
4. Understanding + generation unification；
5. Multimodal reasoning + RL/verifier；
6. Active perception / lookback；
7. Long-video retrieval + tracking/memory；
8. Agent protocols：MCP / A2A / tool interfaces；
9. Long-horizon Agent runtime：state / sandbox / checkpoint / resume；
10. GUI/VLA/tool integration；
11. Omni streaming/full-duplex；
12. Disaggregated efficient serving + safety.

---

### 更新纪律
对快速变化的模型和 Agent 协议：**先确认官方 release/spec/model card，再更新本页；不能用第三方文章反推内部架构或协议行为。**
