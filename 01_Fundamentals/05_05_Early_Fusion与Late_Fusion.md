# 05_Early_Fusion与Late_Fusion

## 面试一句话

Early fusion 更早让不同模态共享 Transformer 表示；late fusion 则先各自编码，再在较后阶段通过 cross-attention 或 projector 交互。

## 核心回答

- Early fusion 优点：跨模态交互充分，适合统一建模；缺点：训练和推理成本高。
- Late fusion 优点：模块化强，视觉塔可以冻结或缓存；缺点：模态之间交互深度可能不足。
- 现代模型经常不是二选一，而是“独立编码 + 早期 token 拼接 + LLM 内统一 self-attention”的混合形式。
- 面试中应回答“融合发生在哪一层、是 self-attention 还是 cross-attention、视觉 token 是否进入 LLM 主序列”。
