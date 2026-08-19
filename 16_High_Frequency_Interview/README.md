# 16 · 高频面试题索引（100+）

> 用法：先不看答案，口述 1–3 分钟；说不清再进入对应模块复习。

## A. Transformer / LLM

1. Q、K、V 分别是什么？为什么不是三个固定含义的向量？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
2. 为什么 attention 要除以 `sqrt(d_k)`？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
3. Multi-Head Attention 为什么需要多头？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
4. Self-Attention 和 Cross-Attention 区别？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
5. Causal Mask 怎么实现？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
6. 为什么现在大模型多用 Decoder-only？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
7. RMSNorm 和 LayerNorm 区别？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
8. Pre-Norm 为什么更好训？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
9. SwiGLU 是什么？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
10. RoPE 怎么把位置加入 attention？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
11. MHA / MQA / GQA 区别？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
12. KV Cache 为什么能加速 decode？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
13. KV Cache 显存怎么估算？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
14. Prefill 和 Decode 为什么一个偏计算、一个偏带宽？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
15. MoE 的 total params 和 active params 区别？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
16. MoE 为什么需要 load balancing？ → [01](../01_Transformer_LLM_Fundamentals/README.md)
17. Sliding Window / Linear Attention / Full Attention 怎么选？ → [01](../01_Transformer_LLM_Fundamentals/README.md)

## B. Vision

18. CNN 和 ViT 的根本区别？ → [02](../02_Vision_Fundamentals/README.md)
19. 图像如何从 `[B,3,H,W]` 变成 `[B,N,D]`？ → [02](../02_Vision_Fundamentals/README.md)
20. patch size 如何影响 token 数？ → [02](../02_Vision_Fundamentals/README.md)
21. CLIP 对比学习如何做？ → [02](../02_Vision_Fundamentals/README.md)
22. SigLIP 和 CLIP 的训练目标有何不同？ → [02](../02_Vision_Fundamentals/README.md)
23. DINOv2 为什么能作为强视觉 backbone？ → [02](../02_Vision_Fundamentals/README.md)
24. 为什么 Vision Encoder 不是先输出标签？ → [02](../02_Vision_Fundamentals/README.md)
25. 为什么 ViT 中间层有时比最后一层更有细节？ → [02](../02_Vision_Fundamentals/README.md)
26. OCR 为什么需要高分辨率？ → [02](../02_Vision_Fundamentals/README.md)
27. Grounding 和 VQA 区别？ → [02](../02_Vision_Fundamentals/README.md)
28. 动态分辨率为什么重要？ → [02](../02_Vision_Fundamentals/README.md)
29. 切 tile 有什么副作用？ → [02](../02_Vision_Fundamentals/README.md)

## C. MLLM 架构

30. 一个 VLM 最基本的三块是什么？ → [03](../03_Multimodal_Core_Architecture/README.md)
31. Projector 为什么需要 `Dv → Dl`？ → [03](../03_Multimodal_Core_Architecture/README.md)
32. MLP projector、Q-Former、Resampler 怎么比较？ → [03](../03_Multimodal_Core_Architecture/README.md)
33. Projector 和 token compressor 是一回事吗？ → [03](../03_Multimodal_Core_Architecture/README.md)
34. Early fusion 和 cross-attention fusion 区别？ → [03](../03_Multimodal_Core_Architecture/README.md)
35. LLaVA 为什么结构简单却有效？ → [03](../03_Multimodal_Core_Architecture/README.md)
36. Flamingo 和 LLaVA 路线差异？ → [03](../03_Multimodal_Core_Architecture/README.md)
37. BLIP-2 的 Q-Former 是怎么压视觉 token 的？ → [03](../03_Multimodal_Core_Architecture/README.md)
38. Native resolution 到底是什么意思？ → [03](../03_Multimodal_Core_Architecture/README.md)
39. 多图输入怎么组织？ → [03](../03_Multimodal_Core_Architecture/README.md)
40. 视频为什么不能只当多张图片？ → [03](../03_Multimodal_Core_Architecture/README.md)
41. 多模态位置编码为什么要 T/H/W？ → [03](../03_Multimodal_Core_Architecture/README.md)
42. 多层视觉特征融合为什么有用？ → [03](../03_Multimodal_Core_Architecture/README.md)

## D. 2026 模型

43. Qwen3-VL 的 Interleaved-MRoPE 是什么？ → [04](../04_Representative_Models_2026/README.md)
44. Qwen3-VL 的 DeepStack 解决什么？ → [04](../04_Representative_Models_2026/README.md)
45. Qwen3-VL 的 timestamp alignment 为什么重要？ → [04](../04_Representative_Models_2026/README.md)
46. Qwen3.5 为什么叫 native multimodal foundation？ → [04](../04_Representative_Models_2026/README.md)
47. Qwen3.5 的 Gated DeltaNet + MoE 思路？ → [04](../04_Representative_Models_2026/README.md)
48. InternVL3.5 的 ViR 是什么？ → [04](../04_Representative_Models_2026/README.md)
49. InternVL3.5 的 DvD 为什么是系统创新？ → [04](../04_Representative_Models_2026/README.md)
50. GLM-4.6V 的 native multimodal function calling 是什么？ → [04](../04_Representative_Models_2026/README.md)
51. GLM-5V-Turbo 为什么强调 native multimodal agent？ → [04](../04_Representative_Models_2026/README.md)
52. Seed1.5-VL 的 MoE / agent 能力怎么理解？ → [04](../04_Representative_Models_2026/README.md)
53. Kimi-VL 的 MoonViT / 2.8B active 有什么意义？ → [04](../04_Representative_Models_2026/README.md)
54. MiniCPM-V 4.6 为什么适合端侧？ → [04](../04_Representative_Models_2026/README.md)
55. Qwen3-Omni Thinker–Talker 怎么分工？ → [04](../04_Representative_Models_2026/README.md)
56. Full-duplex Omni 比 ASR→LLM→TTS 难在哪？ → [08](../08_Video_Audio_Omni/README.md)
57. Llama 4 的 MoE 多模态路线怎么讲？ → [04](../04_Representative_Models_2026/README.md)
58. 闭源 VLM 被问内部架构时应该怎么回答？ → [04](../04_Representative_Models_2026/README.md)

## E. 数据

59. 多模态预训练数据有哪些类型？ → [05](../05_Multimodal_Data_Engineering/README.md)
60. 图文对怎么清洗？ → [05](../05_Multimodal_Data_Engineering/README.md)
61. 多模态去重怎么做？ → [05](../05_Multimodal_Data_Engineering/README.md)
62. benchmark contamination 怎么查？ → [05](../05_Multimodal_Data_Engineering/README.md)
63. 图文相似度打分怎么做？ → [05](../05_Multimodal_Data_Engineering/README.md)
64. 数据配比怎么优化？ → [05](../05_Multimodal_Data_Engineering/README.md)
65. OCR / PDF 数据如何保留 layout？ → [05](../05_Multimodal_Data_Engineering/README.md)
66. 视频训练数据如何采样？ → [05](../05_Multimodal_Data_Engineering/README.md)
67. GUI trajectory 数据长什么样？ → [05](../05_Multimodal_Data_Engineering/README.md)
68. 合成数据怎么过滤 teacher hallucination？ → [05](../05_Multimodal_Data_Engineering/README.md)
69. 如何评价一批数据是否真的有价值？ → [05](../05_Multimodal_Data_Engineering/README.md)
70. 如何搭建训练反馈驱动的数据闭环？ → [05](../05_Multimodal_Data_Engineering/README.md)

## F. 训练与 RL

71. 为什么先训 projector 再解冻模型？ → [06](../06_Pretraining_SFT_PEFT/README.md)
72. Vision Encoder 到底要不要冻结？ → [06](../06_Pretraining_SFT_PEFT/README.md)
73. Multimodal pretraining 和 SFT 区别？ → [06](../06_Pretraining_SFT_PEFT/README.md)
74. MLLM 的 CE loss 怎么算？ → [06](../06_Pretraining_SFT_PEFT/README.md)
75. 为什么只对 assistant token 计 loss？ → [06](../06_Pretraining_SFT_PEFT/README.md)
76. LoRA 的低秩矩阵为什么这样初始化？ → [06](../06_Pretraining_SFT_PEFT/README.md)
77. LoRA 应该加 LLM、vision 还是 projector？ → [06](../06_Pretraining_SFT_PEFT/README.md)
78. QLoRA 为什么省显存？ → [06](../06_Pretraining_SFT_PEFT/README.md)
79. SFT 后视觉能力下降怎么诊断？ → [06](../06_Pretraining_SFT_PEFT/README.md)
80. SFT / DPO / RLHF / RLVR 区别？ → [07](../07_PostTraining_RL_Reasoning/README.md)
81. Reward Model 怎么训练？ → [07](../07_PostTraining_RL_Reasoning/README.md)
82. GRPO 为什么不一定需要 value model？ → [07](../07_PostTraining_RL_Reasoning/README.md)
83. RLVR 为什么适合视觉数学/GUI？ → [07](../07_PostTraining_RL_Reasoning/README.md)
84. Reward Hacking 怎么防？ → [07](../07_PostTraining_RL_Reasoning/README.md)
85. Thinking 越长为什么不一定越好？ → [07](../07_PostTraining_RL_Reasoning/README.md)
86. Test-time scaling 怎么做？ → [07](../07_PostTraining_RL_Reasoning/README.md)
87. Active perception 是什么？ → [07](../07_PostTraining_RL_Reasoning/README.md)

## G. Video / Agent / RAG

88. 长视频为什么要检索后重看？ → [08](../08_Video_Audio_Omni/README.md)
89. 视频 token 怎么压缩？ → [08](../08_Video_Audio_Omni/README.md)
90. Multimodal Agent 的闭环是什么？ → [09](../09_RAG_Tools_Agents_GUI_VLA/README.md)
91. Function Calling 怎么训练？ → [09](../09_RAG_Tools_Agents_GUI_VLA/README.md)
92. MCP 和 Function Call 区别？ → [09](../09_RAG_Tools_Agents_GUI_VLA/README.md)
93. Multimodal RAG 完整 pipeline？ → [09](../09_RAG_Tools_Agents_GUI_VLA/README.md)
94. Embedding 和 Reranker 区别？ → [09](../09_RAG_Tools_Agents_GUI_VLA/README.md)
95. GUI Agent 为什么需要 grounding？ → [09](../09_RAG_Tools_Agents_GUI_VLA/README.md)
96. 为什么不能只看 next-action accuracy？ → [09](../09_RAG_Tools_Agents_GUI_VLA/README.md)
97. VLA 输出动作有哪些方式？ → [09](../09_RAG_Tools_Agents_GUI_VLA/README.md)

## H. 分布式与推理系统

98. DDP 和 FSDP 区别？ → [10](../10_Distributed_Training/README.md)
99. ZeRO 1/2/3 分别切什么？ → [10](../10_Distributed_Training/README.md)
100. TP / PP / DP / EP 分别切什么？ → [10](../10_Distributed_Training/README.md)
101. MoE 为什么需要 Expert Parallel？ → [10](../10_Distributed_Training/README.md)
102. Activation Checkpointing 省什么、牺牲什么？ → [10](../10_Distributed_Training/README.md)
103. 多模态训练为什么 rank 容易负载不均？ → [10](../10_Distributed_Training/README.md)
104. Continuous Batching 是什么？ → [11](../11_Inference_Serving_Optimization/README.md)
105. PagedAttention 为什么省 KV 内存碎片？ → [11](../11_Inference_Serving_Optimization/README.md)
106. Prefix Cache 什么时候最有效？ → [11](../11_Inference_Serving_Optimization/README.md)
107. FlashAttention 为什么不是 O(N) attention？ → [11](../11_Inference_Serving_Optimization/README.md)
108. INT4 / AWQ / GPTQ 怎么理解？ → [11](../11_Inference_Serving_Optimization/README.md)
109. TTFT / TPOT 分别受什么影响？ → [11](../11_Inference_Serving_Optimization/README.md)
110. Vision Encoder 和 LLM 为什么可能拆服务？ → [11](../11_Inference_Serving_Optimization/README.md)
111. 多模态 Serving OOM 怎么查？ → [11](../11_Inference_Serving_Optimization/README.md)

## I. 评测 / 手撕 / 项目

112. MMMU 和 MathVista 分别测什么？ → [12](../12_Evaluation_Diagnostics/README.md)
113. 怎么判断模型是真的看图还是靠语言猜？ → [12](../12_Evaluation_Diagnostics/README.md)
114. 怎么区分 perception error 和 reasoning error？ → [12](../12_Evaluation_Diagnostics/README.md)
115. Agent 评测为什么要看最终环境状态？ → [12](../12_Evaluation_Diagnostics/README.md)
116. 手写 Attention → [13](../13_Code_Handwriting/README.md)
117. 手写 LoRA → [13](../13_Code_Handwriting/README.md)
118. 手写 masked SFT loss → [13](../13_Code_Handwriting/README.md)
119. 手算视觉 token 数 → [13](../13_Code_Handwriting/README.md)
120. 手算 KV Cache → [13](../13_Code_Handwriting/README.md)
121. 设计企业 PDF 多模态问答 → [14](../14_System_Design/README.md)
122. 设计长视频 QA → [14](../14_System_Design/README.md)
123. 设计 GUI Agent → [14](../14_System_Design/README.md)
124. 90 秒怎么介绍项目？ → [15](../15_Project_Interview/README.md)
125. 如何证明增益来自你的模块？ → [15](../15_Project_Interview/README.md)
126. 项目 OOM 怎么讲才有技术含量？ → [15](../15_Project_Interview/README.md)

---

### 面试前最后一条规则

**不会的就明确边界。** “官方没有公开这一部分，我能解释常见实现，但不能把它当成该模型的事实。” 这句话比编架构更加分。