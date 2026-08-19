# 06_InternVL3_5核心思路

## 面试一句话

InternVL3.5 的面试重点是“视觉分辨率路由 + 推理后训练 + 视觉/语言部署解耦”。

## 核心回答

- Visual Resolution Router（ViR）按输入自适应视觉 token/分辨率。
- Cascade RL 把离线 RL 与在线 RL 组合，增强多模态 reasoning。
- Decoupled Vision-Language Deployment（DvD）把视觉编码器和 LLM 分置不同 GPU，平衡负载。
- 它说明 2026 面试已经不仅问模型精度，也会问视觉 token 的系统成本。

## 参考

- https://arxiv.org/abs/2508.18265
