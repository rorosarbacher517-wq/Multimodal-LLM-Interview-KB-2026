# 00A · Math Fundamentals for AI

> 目标：只补 **AI / Deep Learning / Transformer / Vision / 3D / RL 真正会反复用到的数学**。
>
> 不按大学教材重新学一遍高数、线代和概率论，而是按：**数学概念 → 直觉 → 公式 → 在模型里怎么用** 来组织。
>
> 建议顺序：**向量矩阵 → 几何与相似度 → 微积分与梯度 → 概率统计 → 信息论 → 优化 → 数值稳定性 → AI 映射**。

---

# Part A. 数值、函数与基本直觉

## Q1. 标量、向量、矩阵、Tensor 分别是什么？

- 标量：一个数，例如学习率 `1e-4`。
- 向量：一列/一行数，例如一个 token embedding `x ∈ R^D`。
- 矩阵：二维数组，例如 Linear 权重 `W ∈ R^{D_in×D_out}`。
- Tensor：更高维数组，例如 `[B,L,D]`。

在深度学习里，最重要的不是“几维”，而是每一维代表什么。

```text
[B, L, D]
B = batch
L = sequence length
D = hidden dimension
```

---

## Q2. 为什么指数函数 `exp(x)` 在深度学习里这么常见？

因为它总为正，而且能把较大的输入快速放大。

常见位置：

- Softmax；
- Gaussian distribution；
- exponential moving average；
- log-likelihood。

Softmax 本质上就是：

```text
score → exp(score) → normalize
```

---

## Q3. 为什么对数 `log(x)` 这么重要？

因为它可以把“乘法”变成“加法”：

```text
log(ab) = log(a) + log(b)
```

这在概率模型中非常重要，因为大量小概率直接相乘容易下溢。

例如：

```text
P(sequence) = Π_t P(x_t | x_<t)
```

训练时通常改成：

```text
log P(sequence) = Σ_t log P(x_t | x_<t)
```

---

## Q4. `log-sum-exp` 为什么是数值稳定里的经典技巧？

直接算：

```text
log(Σ exp(x_i))
```

如果 `x_i` 很大，`exp(x_i)` 可能溢出。

用：

```text
m = max(x)
log Σ exp(x_i) = m + log Σ exp(x_i - m)
```

数学等价，但数值稳定很多。

Softmax、CrossEntropy 的底层实现会大量使用这个思路。

---

## Q5. 为什么很多 loss 喜欢用平方？

平方有三个特点：

- 总是非负；
- 大误差会被更重惩罚；
- 可导且导数简单。

MSE：

```text
L = (y_hat - y)^2
```

导数：

```text
dL/dy_hat = 2(y_hat-y)
```

所以误差越大，更新通常越强。

---

# Part B. 向量与矩阵：Transformer 最核心的数学语言

## Q6. 向量可以怎么理解？

向量不只是“一串数”，还可以理解为一个点、一个方向或一个特征表示。

例如一个 token embedding：

```text
x = [0.2, -1.1, 0.7, ...]
```

它在高维空间中的位置编码了语义信息。

---

## Q7. 点积到底在计算什么？

两个向量：

```text
a · b = Σ_i a_i b_i
```

几何上：

```text
a · b = ||a|| ||b|| cosθ
```

所以点积同时受到：

- 向量长度；
- 夹角相似度

影响。

Attention 的 `QK^T` 本质就是大批量点积相似度。

---

## Q8. 向量的 L1、L2 Norm 是什么？

```text
L1 = Σ |x_i|
L2 = sqrt(Σ x_i^2)
```

直觉：

- L1：所有绝对值相加；
- L2：欧氏空间中的长度。

应用：

- L1 regularization 倾向产生稀疏权重；
- L2 / weight decay 倾向整体缩小权重；
- embedding normalization 常用 L2 norm。

---

## Q9. Cosine Similarity 和 Dot Product 区别？

Cosine similarity：

```text
cos(a,b) = a·b / (||a|| ||b||)
```

它去掉了向量长度影响，更关注方向。

所以：

- CLIP / embedding retrieval 常见 cosine similarity；
- Attention 常直接使用 dot product，因为 Q/K 的长度本身也可以参与匹配。

---

## Q10. 为什么矩阵乘法不是逐元素乘法？

矩阵乘法：

```text
A[m,n] @ B[n,p] → C[m,p]
```

其中：

```text
C_ij = Σ_k A_ik B_kj
```

它的本质是：每个输出元素都是输入维度上的加权组合。

Linear layer：

```text
[B,L,D_in] @ [D_in,D_out]
→ [B,L,D_out]
```

---

## Q11. 矩阵转置有什么意义？

转置交换行和列：

```text
A[m,n] → A^T[n,m]
```

Attention 中：

```text
Q [L,d]
K [L,d]
K^T [d,L]
QK^T [L,L]
```

这样每个 query 就能和所有 key 两两计算相似度。

---

## Q12. Rank（秩）是什么？

Rank 可以理解为一个矩阵真正包含多少个“独立方向”。

如果一个大矩阵很多列都可以由少数基础方向组合出来，它就是低秩的。

这直接解释了 LoRA：

```text
ΔW ≈ A B
```

其中 rank `r` 很小，用少量参数近似原本巨大的权重更新。

---

## Q13. 为什么低秩分解能压缩参数？

原矩阵：

```text
W ∈ R^{m×n}
参数 = mn
```

低秩：

```text
A ∈ R^{m×r}
B ∈ R^{r×n}
参数 = r(m+n)
```

若 `r << min(m,n)`，参数显著减少。

这就是 LoRA 参数高效的数学基础。

---

## Q14. 逆矩阵是什么？为什么深度学习里很少显式求逆？

如果：

```text
A A^{-1} = I
```

则 `A^{-1}` 是逆矩阵。

但显式求逆：

- 成本高；
- 数值稳定性可能差；
- 很多问题可以直接用线性方程求解器解决。

所以工程中通常避免写：

```python
x = inverse(A) @ b
```

更常用：

```python
x = solve(A, b)
```

---

## Q15. 伪逆（Pseudo-inverse）是什么？

不是所有矩阵都可逆。

Moore–Penrose 伪逆 `A^+` 可以用于：

- 非方阵；
- rank 不满；
- 最小二乘问题。

经典线性回归就是它的重要背景。

---

# Part C. 几何、投影与表示空间

## Q16. 什么叫两个向量正交？

如果：

```text
a · b = 0
```

则正交。

几何上是 90°。

高维模型中“不同方向”可以表示不同变化因素，所以正交性经常用于：

- 特征解耦；
- basis；
- PCA；
- SVD。

---

## Q17. Basis（基）是什么？

一组线性无关向量，如果可以组合出整个空间里的任意向量，就构成一个 basis。

直觉：

```text
二维空间只需要 x轴 + y轴
```

高维 embedding 空间也是类似，只是 basis 不再直观可见。

---

## Q18. Projection（投影）是什么？

把一个向量映射到另一个方向或子空间。

投影到单位向量 `u`：

```text
proj_u(x) = (x·u)u
```

Linear layer、PCA、Q/K/V projection 都可以从“把表示投到不同子空间”这个角度理解。

---

## Q19. Euclidean Distance 和 Cosine Similarity 怎么选？

Euclidean：

```text
||a-b||_2
```

关注绝对位置距离。

Cosine：

```text
cosθ
```

关注方向。

如果 embedding 已做 L2 normalization，两者关系很强：

```text
||a-b||^2 = 2 - 2cosθ
```

---

## Q20. 为什么 embedding 可以做语义检索？

训练目标把语义相近样本推到相近方向/位置。

因此：

```text
query embedding
      ↓
nearest neighbors
      ↓
similar documents/images
```

向量数据库本质上就是在高维空间里做近邻搜索。

---

# Part D. Eigen / SVD / PCA：理解降维和低秩

## Q21. Eigenvalue / Eigenvector 是什么？

如果：

```text
Av = λv
```

说明矩阵 `A` 作用在 `v` 上后，只改变长度，不改变方向。

- `v`：eigenvector；
- `λ`：eigenvalue。

它描述矩阵最重要的“天然方向”。

---

## Q22. Covariance Matrix 为什么会和 PCA 连起来？

协方差矩阵：

```text
Σ = E[(x-μ)(x-μ)^T]
```

它描述不同维度如何一起变化。

PCA 就是在找协方差矩阵方差最大的 eigenvectors。

---

## Q23. SVD 是什么？

任意矩阵可以写成：

```text
A = U Σ V^T
```

其中：

- `U`：左侧主要方向；
- `Σ`：singular values；
- `V`：右侧主要方向。

SVD 不要求矩阵必须方阵，因此比 eigen decomposition 更普遍。

---

## Q24. 为什么截断 SVD 可以做低秩近似？

只保留最大的前 `r` 个 singular values：

```text
A ≈ U_r Σ_r V_r^T
```

相当于只保留矩阵中最重要的变化方向。

这就是很多压缩、降维、低秩方法的数学基础。

---

## Q25. PCA 到底在做什么？

PCA 找一组新的正交坐标轴，使：

- 第一维解释最大方差；
- 第二维解释剩余最大方差；
- 依次类推。

所以它本质上是：

```text
高维数据
→ 找主要变化方向
→ 投影到低维
```

---

## Q26. LoRA 和 PCA/SVD 有什么数学上的相似点？

它们都利用“高维变化往往集中在较低维子空间”这个思想。

不同点：

- PCA/SVD 是对已有矩阵/数据做分解；
- LoRA 是直接把训练更新参数化成低秩形式。

---

# Part E. 微积分：Backpropagation 的语言

## Q27. 导数是什么？

导数描述：

> 输入变化一点，输出会变化多少。

```text
dy/dx
```

例如：

```text
y=x^2
 dy/dx = 2x
```

---

## Q28. Partial Derivative 为什么需要？

神经网络函数有很多变量。

例如：

```text
L(w1,w2,...,wn)
```

对某个参数 `w_i`：

```text
∂L/∂w_i
```

表示只改变 `w_i` 时 loss 的局部变化率。

---

## Q29. Gradient 是什么？

Gradient 是所有偏导数组成的向量：

```text
∇L = [∂L/∂w1, ..., ∂L/∂wn]
```

它指向 loss 增长最快方向。

所以梯度下降使用：

```text
w ← w - η∇L
```

---

## Q30. 为什么 Gradient Descent 要减梯度？

梯度指向函数增长最快方向。

我们想让 loss 下降，所以走反方向：

```text
-∇L
```

学习率 `η` 决定每一步走多远。

---

## Q31. Chain Rule 为什么是 Backprop 的核心？

如果：

```text
x → z → y → L
```

则：

```text
dL/dx = dL/dy · dy/dz · dz/dx
```

神经网络就是很多函数层层组合，所以反向传播就是不断应用 chain rule。

---

## Q32. Jacobian 是什么？

如果输入和输出都是向量：

```text
y=f(x)
```

Jacobian：

```text
J_ij = ∂y_i / ∂x_j
```

它描述每个输出对每个输入的局部敏感度。

自动微分系统不会总把完整 Jacobian 显式存下来，而是高效计算 vector-Jacobian product。

---

## Q33. Hessian 是什么？

Hessian 是二阶偏导矩阵：

```text
H_ij = ∂²L / ∂w_i∂w_j
```

它描述 loss surface 的曲率。

直觉：

- 一阶梯度告诉你“往哪走”；
- 二阶信息告诉你“地面有多弯”。

---

## Q34. 为什么深度学习通常不用完整 Hessian？

因为参数可能有几十亿。

完整 Hessian 尺寸：

```text
N × N
```

几乎不可存储。

所以大模型优化通常使用一阶方法或近似二阶统计。

---

## Q35. MSE 的梯度为什么这么简单？

```text
L = (y_hat-y)^2
```

所以：

```text
∂L/∂y_hat = 2(y_hat-y)
```

这解释了为什么大误差会产生更大梯度。

---

## Q36. Softmax + Cross Entropy 为什么组合得特别自然？

Softmax 把 logits 变成概率：

```text
p_i = exp(z_i) / Σ_j exp(z_j)
```

Cross Entropy：

```text
L = -log p_y
```

组合后对 logits 的梯度非常简洁：

```text
∂L/∂z = p - y_onehot
```

也就是“预测概率 - 真实分布”。

---

# Part F. 概率：理解 Loss、Sampling 和不确定性

## Q37. Random Variable 是什么？

随机变量把随机结果映射成数值。

例如：

```text
X = 下一个 token 的类别
```

模型实际学习的是：

```text
P(X = token_i | context)
```

---

## Q38. Probability Distribution 是什么？

它描述所有可能结果及对应概率。

语言模型最后一个位置输出：

```text
logits [V]
↓ softmax
probabilities [V]
```

这就是对 vocabulary 上的 categorical distribution 建模。

---

## Q39. Joint / Marginal / Conditional Probability 区别？

- Joint：`P(A,B)`，A 和 B 同时发生；
- Marginal：`P(A)`，只关心 A；
- Conditional：`P(A|B)`，已知 B 后 A 的概率。

LLM 的核心就是条件概率：

```text
P(x_t | x_<t)
```

---

## Q40. Bayes Rule 是什么？

```text
P(A|B) = P(B|A)P(A) / P(B)
```

直觉：

> 看到了新的证据 B 后，重新更新对 A 的相信程度。

它是 Bayesian inference、MAP、probabilistic modeling 的基础。

---

## Q41. Independence 是什么？

若：

```text
P(A,B)=P(A)P(B)
```

则 A、B 独立。

注意：

- correlation=0 不一定独立；
- independence 通常比“无线性相关”更强。

---

## Q42. Expectation 是什么？

离散情况：

```text
E[X] = Σ_x x P(x)
```

它就是随机变量的概率加权平均。

训练 loss 常写：

```text
E_(x,y) [L(f(x),y)]
```

实际 mini-batch 只是用有限样本近似这个 expectation。

---

## Q43. Variance 是什么？

```text
Var(X)=E[(X-E[X])^2]
```

表示随机变量围绕均值的波动程度。

高 variance = 波动大。

在训练中：

- gradient variance；
- estimator variance；
- batch size

都有直接关系。

---

## Q44. Covariance 和 Correlation 区别？

Covariance：

```text
Cov(X,Y)=E[(X-μx)(Y-μy)]
```

Correlation 是标准化后的 covariance：

```text
ρ = Cov(X,Y)/(σxσy)
```

Correlation 无量纲，范围通常在 `[-1,1]`。

---

## Q45. Bernoulli / Categorical / Gaussian 分别适合什么？

- Bernoulli：二元结果，例如 yes/no；
- Categorical：多个离散类别，例如 token；
- Gaussian：连续变量，围绕均值波动。

很多 loss 都对应某种概率分布假设。

---

## Q46. 为什么 MSE 常对应 Gaussian 假设？

假设：

```text
y = f(x) + ε
ε ~ N(0,σ²)
```

最大化 Gaussian likelihood，等价于最小化平方误差（忽略常数项）。

所以 MSE 不只是“随便选的 loss”，背后有概率解释。

---

# Part G. 统计：训练数据为什么只能近似真实世界

## Q47. Population 和 Sample 区别？

- Population：真正关心的整体数据分布；
- Sample：实际拿到的有限数据。

机器学习永远是在 sample 上训练，却希望对 population 泛化。

---

## Q48. Sample Mean 为什么可以估计真实均值？

```text
x_bar = (1/n) Σ x_i
```

在独立同分布等条件下，随着样本变多，sample mean 会趋近真实 expectation。

这就是大数定律背后的直觉。

---

## Q49. Bias 和 Variance 怎么理解？

- Bias 高：模型假设太强，系统性偏离真实规律；
- Variance 高：对训练样本过于敏感，换一批数据结果差很多。

常见：

```text
underfitting → high bias
overfitting  → high variance
```

---

## Q50. MLE 是什么？

Maximum Likelihood Estimation：

找参数 `θ`，让观测数据最可能出现：

```text
θ* = argmax_θ P(D|θ)
```

通常转成 log-likelihood：

```text
argmax Σ log P(x_i|θ)
```

LLM next-token training 就可以看作大规模 maximum likelihood training。

---

## Q51. MAP 和 MLE 区别？

MLE：

```text
argmax P(D|θ)
```

MAP：

```text
argmax P(θ|D)
∝ P(D|θ)P(θ)
```

MAP 多了 prior `P(θ)`。

直觉：

- MLE 只相信数据；
- MAP = 数据 + 先验。

---

# Part H. 信息论：Cross Entropy、KL、CLIP 的数学背景

## Q52. Entropy 是什么？

```text
H(P) = -Σ p(x) log p(x)
```

它衡量一个分布的不确定性。

- 很确定：entropy 低；
- 很平均：entropy 高。

LLM 输出分布的 entropy 可以反映模型当前有多“犹豫”。

---

## Q53. Cross Entropy 是什么？

真实分布 `P`，模型分布 `Q`：

```text
H(P,Q) = -Σ P(x) log Q(x)
```

分类 one-hot 情况：

```text
L = -log Q(y)
```

也就是只惩罚真实类别的预测概率。

---

## Q54. KL Divergence 是什么？

```text
KL(P||Q)=Σ P(x) log(P(x)/Q(x))
```

它衡量用 `Q` 近似 `P` 时的信息损失。

性质：

- `KL >= 0`；
- `KL(P||Q) != KL(Q||P)`；
- 所以不是严格意义上的距离。

应用：

- distillation；
- RL；
- variational methods；
- distribution alignment。

---

## Q55. Cross Entropy 和 KL 有什么关系？

```text
H(P,Q) = H(P) + KL(P||Q)
```

训练时真实分布 `P` 固定，所以 `H(P)` 是常数。

因此最小化 Cross Entropy 等价于最小化 `KL(P||Q)`。

---

## Q56. Mutual Information 是什么？

它衡量知道 `X` 后，能减少多少关于 `Y` 的不确定性。

```text
I(X;Y)=KL(P(X,Y)||P(X)P(Y))
```

如果独立：

```text
I(X;Y)=0
```

很多 representation learning 方法都可以从“保留有用 mutual information”角度理解。

---

## Q57. Contrastive Learning 的数学核心是什么？

目标是：

```text
positive pair → similarity 高
negative pair → similarity 低
```

CLIP 类模型通常：

```text
image embedding
text embedding
→ normalize
→ similarity matrix
→ temperature scaling
→ contrastive cross entropy
```

数学核心就是向量几何 + softmax + cross entropy。

---

# Part I. 优化：为什么训练会收敛，也为什么会不稳定

## Q58. Convex 和 Non-convex 区别？

Convex function 可以直观理解为“碗形”，局部最优就是全局最优。

深度神经网络 loss 通常 non-convex，所以会有复杂的：

- saddle point；
- flat region；
- sharp region。

但大规模训练仍能找到很好解，说明“找到唯一全局最优”不是实际训练唯一目标。

---

## Q59. Learning Rate 为什么这么关键？

```text
θ ← θ - η∇L
```

- `η` 太大：跳过好区域，甚至发散；
- `η` 太小：训练很慢，可能卡在平台区。

Warmup、cosine decay 本质都在控制不同阶段的步长。

---

## Q60. L1 / L2 Regularization 的区别？

L1：

```text
λ Σ |w_i|
```

更容易把部分权重推到 0，产生稀疏性。

L2：

```text
λ Σ w_i^2
```

更倾向整体缩小权重。

---

## Q61. 为什么 Batch Size 会影响梯度噪声？

mini-batch gradient 只是总体 gradient 的估计。

- batch 小：估计噪声大；
- batch 大：估计更稳定。

但 batch 大并不总更好，因为它也会影响：

- generalization；
- learning-rate scaling；
- memory；
- communication。

---

## Q62. 为什么梯度接近 0 不一定代表训练完成？

可能是：

- 真正到达局部最优；
- saddle point；
- activation saturation；
- gradient vanishing；
- mask / detach / bug。

所以工程上不能只看 gradient norm 一个指标。

---

# Part J. 数值稳定性：大模型训练里非常实际的数学

## Q63. Floating Point 为什么有精度限制？

计算机浮点数不是连续实数，而是有限精度表示。

因此会出现：

- overflow；
- underflow；
- rounding error；
- cancellation。

FP16 比 BF16 更容易因为 exponent range 小而 overflow。

---

## Q64. 为什么 Softmax 要先减最大值？

```text
softmax(x_i)=exp(x_i)/Σexp(x_j)
```

改成：

```text
exp(x_i-m)/Σexp(x_j-m)
m=max(x)
```

结果不变，但所有 exponent ≤ 0，大幅降低 overflow 风险。

---

## Q65. 为什么概率不能直接连续相乘？

很多概率 < 1：

```text
0.001 × 0.002 × 0.0003 × ...
```

很快下溢为 0。

改到 log-space：

```text
log p_total = Σ log p_i
```

更稳定。

---

## Q66. 为什么标准差计算里需要 `eps`？

例如：

```text
x / sqrt(var + eps)
```

如果 variance 非常小，直接除可能产生数值爆炸。

`eps` 是一个小正数，用来避免除 0 和极端放大。

LayerNorm / RMSNorm 都会用这个技巧。

---

# Part K. 把数学直接映射回 AI 模型

## Q67. Linear Layer 的数学本质是什么？

```text
y = xW + b
```

它做的是一个 affine transformation：

- 旋转/拉伸/投影；
- 再加 bias 平移。

没有非线性 activation，多层 Linear 仍等价于一层 Linear。

---

## Q68. Attention 的数学本质是什么？

可以拆成三步：

```text
1. Similarity
QK^T

2. Normalize
softmax

3. Weighted Average
AttentionWeights @ V
```

所以 attention 本质上是：

> 根据 query-key 相似度，对 value 做动态加权汇总。

---

## Q69. 为什么 CLIP 会用 normalized embedding + temperature？

L2 normalization 后：

```text
x·y = cosine similarity
```

避免 embedding norm 主导相似度。

temperature 则控制 softmax 的尖锐程度：

```text
softmax(similarity / τ)
```

`τ` 越小，分布越尖锐。

---

## Q70. LoRA 为什么数学上合理？

它假设 fine-tuning 需要的权重变化近似集中在一个低维子空间：

```text
W' = W + ΔW
ΔW = BA
rank(ΔW) ≤ r
```

所以不需要训练完整 `D×D` 更新。

---

## Q71. 为什么 PCA / SVD 思想也会出现在压缩和表示学习里？

因为很多高维数据的有效变化不是均匀分布在所有方向，而是集中在少数 principal directions。

因此可以：

- 降维；
- 压缩；
- 去噪；
- 低秩近似。

---

## Q72. 3D Perception 为什么必须懂矩阵变换？

坐标变换通常写成：

```text
p_camera = R p_world + t
```

齐次坐标：

```text
[p';1] = T [p;1]
T = [R t
     0 1]
```

所以机器人、BEV、SfM、VGGT、VLA 都离不开：

- matrix multiplication；
- rotation；
- translation；
- coordinate frames。

---

## Q73. 为什么概率、信息论和优化最终会汇合到 Cross Entropy？

从三个角度看同一个 loss：

### 概率角度
最大化真实类别 likelihood。

### 信息论角度
最小化真实分布和预测分布的 cross entropy / KL。

### 优化角度
得到简单稳定的 gradient：

```text
p - y
```

这就是为什么 Cross Entropy 在分类和语言模型里如此核心。

---

# 最值得手推的 10 个公式

建议面试前至少能自己推/解释：

```text
1. y = xW + b
2. a·b = ||a||||b||cosθ
3. cosine(a,b)
4. softmax(z)
5. cross entropy = -log p_y
6. ∂(softmax+CE)/∂z = p-y
7. gradient descent: θ ← θ-η∇L
8. attention = softmax(QK^T/√d)V
9. covariance = E[(x-μ)(x-μ)^T]
10. SVD: A = UΣV^T
```

---

# 面试时数学题怎么回答

不要一上来就背公式。推荐四步：

1. **先说直觉**：它解决什么问题；
2. **再给核心公式**；
3. **说明 shape / 变量含义**；
4. **映射到真实模型**。

例如被问 cosine similarity：

```text
它衡量两个向量方向是否接近，去掉模长影响。
公式是 a·b/(||a||||b||)。
在 CLIP / embedding retrieval 里通常先 L2 normalize，
这样 dot product 就等价于 cosine similarity。
```

这比只背一个公式更像算法工程面试回答。

---

# 通过标准

学完这一模块，至少应该做到：

- 能解释 dot product / cosine / matrix multiplication；
- 能看懂 `[B,L,D] @ [D,D2]`；
- 能解释 gradient / chain rule / Jacobian；
- 能解释 expectation / variance / covariance；
- 能解释 entropy / cross entropy / KL；
- 能解释 eigen / SVD / PCA / low rank；
- 能说明 LoRA 为什么是低秩；
- 能说明 softmax 和 cross entropy 为什么要做数值稳定；
- 能把矩阵变换用于 3D coordinate frame；
- 能把数学重新映射到 Attention / CLIP / Loss / LoRA / 3D Perception。

下一步： [00B Deep Learning Fundamentals](../00B_Deep_Learning_Fundamentals/README.md)
