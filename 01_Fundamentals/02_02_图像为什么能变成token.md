# 02_图像为什么能变成token

## 面试一句话

Vision Transformer 会把图像切成 patch，把每个 patch 映射成向量；这些向量就是最基础的视觉 token。

## 核心回答

- 若输入为 H×W×3、patch size 为 P，则 patch 数约为 (H/P)×(W/P)。
- 每个 patch 展平后经线性层映射到视觉 hidden size D_v，得到 N×D_v。
- 连接器再把 D_v 映射到 LLM hidden size D_l，得到 N'×D_l。
- 最终序列常见形式是 `[text tokens] + [visual tokens] + [text tokens]`，再送入 LLM。

## 常见追问

**Q：为什么视觉 token 很贵？**

因为注意力和 KV cache 都随 token 数增加；高分辨率图像、长视频会快速把视觉 token 数推高。

## 易错点

- N' 不一定等于原始 patch 数：模型可能做 pooling、resampler、token merge 或动态压缩。
