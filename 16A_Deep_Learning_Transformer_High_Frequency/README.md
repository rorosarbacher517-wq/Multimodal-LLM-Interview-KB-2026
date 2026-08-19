# 16A · Math / Deep Learning / Transformer 高频题（75）

> 用法：先闭卷口述 1–3 分钟。说不清再回到对应模块。
>
> - 数学基础 → [00A](../00A_Math_Fundamentals_for_AI/README.md)
> - 深度学习基础 → [00B](../00B_Deep_Learning_Fundamentals/README.md)
> - Transformer / LLM → [01](../01_Transformer_LLM_Fundamentals/README.md)

## A. Math Fundamentals for AI

1. Dot Product 从代数和几何两个角度分别怎么理解？
2. Cosine Similarity 为什么要除两个向量的 norm？
3. L1 Norm 和 L2 Norm 的区别？
4. `[B,L,D] @ [D,D2]` 为什么输出 `[B,L,D2]`？
5. Matrix Multiplication 和 Element-wise Multiplication 区别？
6. 为什么 `QK^T` 可以看成大批量相似度计算？
7. Rank 是什么？为什么 LoRA 要假设权重更新近似低秩？
8. Projection 怎么理解？Q/K/V projection 在做什么？
9. Orthogonal / Basis / Subspace 分别是什么意思？
10. Eigenvalue / Eigenvector 的直觉是什么？
11. SVD 为什么比 eigen decomposition 更普遍？
12. PCA 为什么能降维？
13. Derivative、Partial Derivative、Gradient 区别？
14. Chain Rule 为什么是 Backpropagation 的核心？
15. Jacobian 是什么？为什么 Autograd 通常不显式构造完整 Jacobian？
16. Hessian 表示什么？为什么大模型训练不会存完整 Hessian？
17. Expectation、Variance、Covariance 分别是什么？
18. Conditional Probability 和 Bayes Rule 怎么理解？
19. Bernoulli、Categorical、Gaussian 分别对应什么类型的数据？
20. MLE 和 MAP 区别？为什么 next-token training 可以看作 MLE？
21. Entropy、Cross Entropy、KL Divergence 区别？
22. 为什么 KL Divergence 不是对称距离？
23. Softmax 为什么要减去最大 logit？
24. `log-sum-exp` 为什么能提高数值稳定性？
25. Softmax + Cross Entropy 为什么会得到 `p-y` 这样的简单梯度？

## B. Deep Learning Fundamentals

26. Tensor 的 `[B,L,D]` 每一维分别表示什么？
27. Broadcasting 为什么可能让代码“能跑但语义错”？
28. Forward / Loss / Backward / Optimizer Step 各做什么？
29. Gradient 的正负和大小分别表示什么？
30. PyTorch 为什么要 `zero_grad()`？
31. MSE、MAE、Huber 各适合什么情况？
32. CrossEntropyLoss 为什么输入 logits 而不是 softmax 后概率？
33. BCE 和多分类 CE 的区别？
34. 为什么神经网络必须有非线性 activation？
35. ReLU、GELU、SiLU 有什么直观区别？
36. SGD、Momentum、Adam、AdamW 怎么区分？
37. AdamW 为什么把 weight decay 解耦？
38. Warmup + Cosine Decay 为什么常见？
39. Gradient accumulation 为什么能模拟大 batch？
40. Gradient clipping 在什么情况下有用？
41. Xavier / Kaiming initialization 解决什么问题？
42. Gradient vanishing / exploding 为什么发生？
43. BatchNorm / LayerNorm / RMSNorm 的统计维度有什么不同？
44. Residual connection 为什么能让网络堆得更深？
45. Overfitting 和 underfitting 怎么从 train/val 曲线判断？
46. FP16 和 BF16 最大区别是什么？
47. Mixed precision 为什么能省显存和提速？
48. FP16 loss scaling 解决什么？
49. 训练显存为什么远大于“参数量 × dtype bytes”？
50. Activation checkpointing 为什么是 compute-for-memory？
51. Loss 变 NaN 时你怎么排查？
52. Gradient 为 0 时你会从哪里查？
53. Batch size 为什么会影响 gradient noise？
54. Weight decay、dropout、data augmentation 分别如何抑制过拟合？
55. Transfer learning 时什么时候 freeze，什么时候 unfreeze？

## C. Transformer & LLM Fundamentals

56. Tokenizer 为什么不能简单按单词切分？
57. BPE 的合并逻辑是什么？
58. Vocabulary 太大和太小分别有什么问题？
59. `[B,L]` token ids 如何变成 `[B,L,D]`？
60. hidden state、logits、probability 三者区别？
61. 为什么现代通用 LLM 多用 Decoder-only？
62. Q/K/V 分别来自哪里？
63. `QK^T` 的完整 shape 怎么推？
64. 为什么 attention 要除以 `sqrt(d_k)`？
65. Multi-Head Attention 如何从 `[B,L,D]` reshape 到 `[B,H,L,d]`？
66. causal mask 和 padding mask 区别？
67. Pre-Norm 为什么更适合深 Transformer？
68. FFN 和 Attention 在 block 内分别负责什么？
69. RoPE 为什么作用在 Q/K 上？
70. MHA / MQA / GQA 为什么主要影响 KV cache？
71. KV cache 的 shape 和显存公式是什么？
72. teacher forcing 为什么允许训练并行？
73. Prefill 和 Decode 为什么瓶颈不同？
74. top-k / top-p / temperature 各改变什么？
75. FlashAttention 为什么没有把理论复杂度从 `O(L²)` 变成 `O(L)`？

## 通过标准

- 60/75 题能在 2 分钟内讲清；
- 数学题不只背公式，要能映射到 Attention / CLIP / Loss / LoRA / 3D；
- 至少 15 题能继续追问两层；
- 能现场画出 `tokenizer → embedding → Transformer → logits → sampling`；
- 能现场画出 `forward → loss → backward → optimizer`；
- 能手算一个简单 Linear、Attention、KV Cache 的 shape；
- 能解释 `dot product → softmax → weighted sum` 为什么就是 Attention；
- 能解释 `low rank → LoRA`、`cross entropy → MLE/KL` 的数学联系。
