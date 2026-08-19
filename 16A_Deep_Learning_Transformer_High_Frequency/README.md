# 16A · Deep Learning & Transformer 高频题（50）

> 用法：先闭卷口述 1–3 分钟。说不清再回到对应模块。
>
> - 深度学习基础 → [00B](../00B_Deep_Learning_Fundamentals/README.md)
> - Transformer / LLM → [01](../01_Transformer_LLM_Fundamentals/README.md)

## A. Deep Learning Fundamentals

1. Tensor 的 `[B,L,D]` 每一维分别表示什么？
2. `[B,L,D] @ [D,D2]` 为什么得到 `[B,L,D2]`？
3. 矩阵乘法和逐元素乘法区别？
4. Broadcasting 为什么可能让代码“能跑但语义错”？
5. Forward / Loss / Backward / Optimizer Step 各做什么？
6. Gradient 的正负和大小分别表示什么？
7. Backpropagation 为什么依赖 chain rule？
8. PyTorch 为什么要 `zero_grad()`？
9. MSE、MAE、Huber 各适合什么情况？
10. CrossEntropyLoss 为什么输入 logits 而不是 softmax 后概率？
11. BCE 和多分类 CE 的区别？
12. KL divergence 为什么不是对称距离？
13. 为什么神经网络必须有非线性 activation？
14. ReLU、GELU、SiLU 有什么直观区别？
15. SGD、Momentum、Adam、AdamW 怎么区分？
16. AdamW 为什么把 weight decay 解耦？
17. Warmup + Cosine Decay 为什么常见？
18. Gradient accumulation 为什么能模拟大 batch？
19. Gradient clipping 在什么情况下有用？
20. Xavier / Kaiming initialization 解决什么问题？
21. Gradient vanishing / exploding 为什么发生？
22. BatchNorm / LayerNorm / RMSNorm 的统计维度有什么不同？
23. Residual connection 为什么能让网络堆得更深？
24. Overfitting 和 underfitting 怎么从 train/val 曲线判断？
25. FP16 和 BF16 最大区别是什么？
26. Mixed precision 为什么能省显存和提速？
27. FP16 loss scaling 解决什么？
28. 训练显存为什么远大于“参数量 × dtype bytes”？
29. Activation checkpointing 为什么是 compute-for-memory？
30. Loss 变 NaN 时你怎么排查？

## B. Transformer & LLM Fundamentals

31. Tokenizer 为什么不能简单按单词切分？
32. BPE 的合并逻辑是什么？
33. Vocabulary 太大和太小分别有什么问题？
34. `[B,L]` token ids 如何变成 `[B,L,D]`？
35. hidden state、logits、probability 三者区别？
36. 为什么现代通用 LLM 多用 Decoder-only？
37. Q/K/V 分别来自哪里？
38. `QK^T` 的完整 shape 怎么推？
39. 为什么 attention 要除以 `sqrt(d_k)`？
40. Multi-Head Attention 如何从 `[B,L,D]` reshape 到 `[B,H,L,d]`？
41. causal mask 和 padding mask 区别？
42. Pre-Norm 为什么更适合深 Transformer？
43. FFN 和 Attention 在 block 内分别负责什么？
44. RoPE 为什么作用在 Q/K 上？
45. MHA / MQA / GQA 为什么主要影响 KV cache？
46. KV cache 的 shape 和显存公式是什么？
47. teacher forcing 为什么允许训练并行？
48. Prefill 和 Decode 为什么瓶颈不同？
49. top-k / top-p / temperature 各改变什么？
50. FlashAttention 为什么没有把理论复杂度从 `O(L²)` 变成 `O(L)`？

## 通过标准

- 40/50 题能在 2 分钟内讲清；
- 至少 10 题能继续追问两层；
- 能现场画出 `tokenizer → embedding → Transformer → logits → sampling`；
- 能现场画出 `forward → loss → backward → optimizer`；
- 能手算一个简单 Linear、Attention、KV Cache 的 shape。
