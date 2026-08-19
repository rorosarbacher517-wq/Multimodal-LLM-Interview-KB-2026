# 04_Projector_Resampler_QFormer区别

## 面试一句话

连接器解决两个问题：**维度不一致**和**视觉 token 太多**。MLP 更简单，Q-Former/Resampler 更强但更复杂。

## 核心回答

- MLP projector：逐 token 做 `D_v → D_l`，简单、快，LLaVA 类方法常用。
- Q-Former：用一组可学习 query 从视觉特征中抽取固定数量的信息，能显著压缩视觉 token。
- Perceiver/Resampler：用 cross-attention 把可变长视觉 token 压到固定或受控长度。
- 选型本质是：信息保真度、计算量、训练稳定性、是否需要固定 token 数之间的权衡。

## 常见追问

**Q：为什么后来很多模型又回到简单 MLP？**

强视觉编码器 + 大量高质量多模态数据后，简单 projector 往往已经足够，而且训练和部署成本更低。


## 参考

- https://arxiv.org/abs/2301.12597
- https://arxiv.org/abs/2304.08485
