# 06_TP_PP_DP_EP怎么选

## 面试一句话

四种并行解决的是不同维度：数据、张量、层、专家。

## 核心回答

- DP/FSDP：切 batch 或模型状态。
- TP：一个矩阵乘在多卡拆。
- PP：不同层放不同 stage。
- EP：MoE experts 分到不同卡。
- 大模型常组合 2D/3D/4D parallelism，选择取决于模型结构、网络拓扑和 batch。
