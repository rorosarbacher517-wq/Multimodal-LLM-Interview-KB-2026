# SAM 的 Prompt Encoder 与 Data Engine 怎么理解？

## Prompt Encoder

SAM 把不同交互提示统一到 256 维 prompt space：

- **Point**：位置编码 + positive/negative point type embedding。
- **Box**：两个角点编码为 sparse tokens。
- **Mask**：下采样后变成与 image embedding 对齐的 dense feature。
- 没有 mask prompt 时使用 learnable no-mask embedding。

## 为什么是 Data Engine？

SAM 不只是一个 segmentation model。它用 model-in-the-loop 的方式提高人工标注效率，再利用更强模型生成更多 masks，形成数据闭环。

SA-1B 公开规模为 **11M images、超过 1B masks**。

## 面试关联

这和 2026 大模型数据岗位的逻辑高度一致：

**模型发现/生成数据 → 规则/人工审核 → 数据回流训练 → 模型变强 → 再生产数据。**

## Primary source

- https://arxiv.org/abs/2304.02643
