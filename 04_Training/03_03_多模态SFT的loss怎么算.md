# 03_多模态SFT的loss怎么算

## 面试一句话

最常见仍是自回归 next-token cross-entropy，但通常只对 assistant 输出 token 计 loss。

## 核心回答

- 图像本身不一定有单独 pixel loss；视觉信息通过影响文本 token 预测被监督。
- user/system/image placeholder 往往 mask 掉，不参与语言 loss。
- grounding/检测类模型可能额外加入 bbox/coordinate token 或专门 loss。
- 生成-理解统一模型还可能加入 diffusion/tokenizer 等生成目标。
