# 00B · Deep Learning Fundamentals

> 目标：把后面 Transformer、ViT、YOLO、VLM、RL 和分布式训练真正依赖的深度学习底层补齐。
>
> 学习时不要只背定义。对每个概念至少能回答四件事：**输入 shape 是什么？计算做了什么？为什么需要它？出问题时会出现什么现象？**

---

## 一、先建立最基本的计算视角

### Q1. 深度学习模型到底在学什么？

一个神经网络可以看成一个带参数的函数：

```text
ŷ = f(x; θ)
```

- `x`：输入数据；
- `θ`：模型参数，例如 Linear/Conv/Attention 中的权重；
- `ŷ`：模型预测；
- `y`：真实标签。

训练的目标是寻找一组参数 `θ`，让 loss 尽可能小：

```text
θ* = argmin_θ L(f(x;θ), y)
```

真正训练时不断重复：

```text
Forward
  ↓
Prediction
  ↓
Loss
  ↓
Backward
  ↓
Gradient
  ↓
Optimizer Step
```

这条链是后面所有大模型训练的共同底座。

---

### Q2. Tensor 的 shape 为什么是算法面试最重要的基础之一？

Tensor 就是多维数组。常见约定：

```text
图像      [B, C, H, W]
文本      [B, L]
Embedding [B, L, D]
视频      [B, T, C, H, W]
点云      [B, N, 3] 或 [B, N, C]
```

其中：

- `B`：batch size；
- `L`：sequence length；
- `D`：hidden dimension；
- `T`：frames；
- `N`：points / tokens。

**面试中最容易暴露是否真正理解模型的地方，就是 shape。**

例如一个 Linear：

```text
x: [B, L, Din]
W: [Din, Dout]
----------------
y: [B, L, Dout]
```

它只改变最后一个维度，不改变 batch 和 sequence length。

---

### Q3. 矩阵乘法和逐元素乘法有什么区别？

矩阵乘法：

```text
[A, B] @ [B, C] → [A, C]
```

内部维度 `B` 被求和消掉。

逐元素乘法：

```text
[A, B] * [A, B] → [A, B]
```

Transformer 中：

- `QK^T` 是矩阵乘法；
- SwiGLU 中两个分支相乘是逐元素乘法；
- attention weight × V 是矩阵乘法。

---

### Q4. Broadcasting 是什么？为什么既方便又危险？

Broadcasting 允许不同 shape 的 tensor 在满足规则时自动扩展。

例如：

```text
x    [B, L, D]
bias [D]
-------------
x+b  [B, L, D]
```

危险在于：**代码能跑，不代表维度语义正确。**

例如本来想对 sequence 维归一化，却误在 hidden 维广播，可能不会报错，但结果完全变了。

---

## 二、Forward、Loss、Backward

### Q5. Forward propagation 是什么？

Forward 就是从输入一路计算到输出：

```text
x
↓ Linear
h1
↓ Activation
h2
↓ Linear
logits
↓ Softmax / task head
prediction
```

训练时 forward 不只是为了得到答案，还需要保存部分中间结果，供 backward 使用。

---

### Q6. Gradient 是什么？

梯度表示：

> 参数改变一点点，loss 会向哪个方向变化、变化多快。

对于一个参数 `w`：

```text
∂L/∂w
```

- 正：增大 `w` 会让 loss 增大；
- 负：增大 `w` 会让 loss 减小；
- 绝对值大：loss 对这个参数更敏感。

优化器一般沿负梯度方向更新参数。

---

### Q7. Backpropagation 本质是什么？

反向传播本质是**链式法则在计算图上的高效应用**。

如果：

```text
x → a → b → L
```

那么：

```text
∂L/∂x = ∂L/∂b · ∂b/∂a · ∂a/∂x
```

神经网络有亿万参数，但框架会按照计算图自动把局部梯度连起来。

---

### Q8. 什么是 Computational Graph？

例如：

```python
y = w * x + b
loss = (y - target) ** 2
```

可以看成：

```text
w ─┐
   × → + → y → subtract → square → loss
x ─┘   ↑
       b
```

PyTorch autograd 会记录这些操作，`loss.backward()` 后沿图反向计算梯度。

---

### Q9. `requires_grad`、`.grad`、`zero_grad()` 分别是什么？

- `requires_grad=True`：这个 tensor 需要参与梯度追踪；
- `.grad`：保存反向传播后累计的梯度；
- `zero_grad()`：清空旧梯度。

为什么要清零？

因为 PyTorch 默认是**梯度累加**：

```text
grad_new = grad_old + current_grad
```

这也是 gradient accumulation 能实现的基础。

---

## 三、Loss Functions

### Q10. MSE Loss 什么时候用？

回归最常见：

```text
MSE = mean((ŷ - y)^2)
```

特点：

- 大误差被平方后惩罚更重；
- 对 outlier 比 MAE 更敏感；
- 梯度连续、优化方便。

---

### Q11. MAE 和 MSE 怎么选？

```text
MAE = mean(|ŷ-y|)
MSE = mean((ŷ-y)^2)
```

- MSE 更强调大误差；
- MAE 对离群点更鲁棒；
- MSE 在 0 附近梯度更平滑；
- 实际也常用 Huber / Smooth L1 作为折中。

---

### Q12. Cross-Entropy Loss 到底在算什么？

分类模型通常先输出 logits：

```text
logits: [B, C]
```

softmax 得到概率：

```text
p_i = exp(z_i) / Σ_j exp(z_j)
```

若真实类别为 `y`：

```text
CE = -log p_y
```

也就是：**真实类别概率越高，loss 越小。**

LLM 的 next-token prediction 本质也是对 vocabulary 做 cross entropy。

---

### Q13. 为什么实现 Cross-Entropy 时通常不要先手动 Softmax？

因为成熟框架会把 `log_softmax + NLLLoss` 合并成数值更稳定的实现。

如果先手动 softmax：

- 可能产生极小概率；
- 再 `log()` 时数值容易不稳定；
- 还会重复计算。

所以 PyTorch `CrossEntropyLoss` 输入通常应该是**raw logits**。

---

### Q14. BCE 和 Cross-Entropy 的区别？

- 单标签多分类：通常 Cross-Entropy；
- 多标签分类：每个类别独立判断，通常 BCE。

例如图片同时有：

```text
cat = 1
sofa = 1
person = 1
```

这不是互斥类别，适合 sigmoid + BCE，而不是 softmax。

---

### Q15. KL Divergence 是什么？

KL divergence 衡量两个概率分布的差异：

```text
KL(P || Q) = Σ P(x) log(P(x)/Q(x))
```

常见于：

- knowledge distillation；
- policy optimization；
- 控制 RL 后的模型不要偏离 reference model 太远。

注意 KL **不是对称距离**。

---

## 四、Activation Functions

### Q16. 为什么神经网络需要非线性激活？

如果每层都是 Linear：

```text
W2(W1x) = (W2W1)x
```

多层线性网络最终仍然等价于一层线性变换。

加入 ReLU/GELU/SiLU 后，模型才能表示复杂非线性函数。

---

### Q17. ReLU 为什么曾经非常流行？

```text
ReLU(x)=max(0,x)
```

优点：

- 简单；
- 正区间梯度恒为 1；
- 比 sigmoid/tanh 更不容易在正区间严重饱和。

问题：负区间梯度为 0，可能出现 dying ReLU。

---

### Q18. GELU、SiLU / Swish 为什么在 Transformer 中常见？

它们比 ReLU 更平滑。

SiLU：

```text
SiLU(x) = x · sigmoid(x)
```

GELU 可以理解为对输入做平滑门控。

现代 LLM 常进一步使用 **SwiGLU**：

```text
SiLU(xW1) ⊙ (xW2)
```

再投影回 hidden size。

---

## 五、Optimization

### Q19. SGD 最基本的更新是什么？

```text
w ← w - η ∂L/∂w
```

`η` 是 learning rate。

学习率太大：震荡甚至发散；
学习率太小：训练非常慢，容易停在不理想区域。

---

### Q20. Momentum 为什么有用？

普通 SGD 只看当前梯度；Momentum 会累积历史方向：

```text
v_t = βv_{t-1} + g_t
w_t = w_{t-1} - ηv_t
```

直观上像一个有惯性的球：

- 相同方向持续加速；
- 来回震荡的方向相互抵消。

---

### Q21. Adam 的核心是什么？

Adam 同时维护：

- 一阶矩：梯度均值；
- 二阶矩：梯度平方均值。

简化理解：

> Momentum 决定“往哪个方向走”；二阶矩帮助决定“每个参数走多大一步”。

这使 Adam 对不同参数自适应调节步长。

---

### Q22. Adam 和 AdamW 的关键区别？

AdamW 把 **weight decay** 从梯度更新中解耦出来。

不要把下面两件事完全等同：

```text
L2 regularization
weight decay
```

在普通 SGD 中二者关系简单，但在 Adam 这种自适应优化器中并不完全等价。

现代 Transformer/LLM 训练通常更常见 AdamW。

---

### Q23. Weight Decay 为什么能帮助泛化？

Weight decay 会持续把参数往 0 拉：

```text
w ← (1 - ηλ)w - ηg
```

它抑制参数无约束变大，可以作为一种正则化。

实践中通常不会对所有参数一视同仁，例如 bias、norm scale 常不做 decay。

---

### Q24. 为什么大模型训练经常 Warmup + Cosine Decay？

训练刚开始时参数还没有进入稳定区域，如果直接用较大学习率，可能使更新过猛。

所以：

```text
Warmup: LR 从小逐渐升高
       ↓
Peak LR
       ↓
Cosine Decay: 逐渐降低
```

后期降低 LR 有利于更稳定地收敛。

---

### Q25. Batch Size 为什么会影响训练？

batch 越大：

- 梯度估计通常更稳定；
- GPU 利用率可能更高；
- 显存占用更大；
- 更新次数变少；
- 可能需要相应调整 learning rate。

大模型训练常用 **tokens per batch**，而不仅仅是 sample count，因为不同样本长度差异很大。

---

### Q26. Gradient Accumulation 是什么？

显存不够放大 batch 时，可以多次 forward/backward 后再 optimizer step：

```text
micro batch 1 → backward
micro batch 2 → backward
micro batch 3 → backward
micro batch 4 → backward
                  ↓
             optimizer.step()
```

若每个 micro batch 为 8，累积 4 次，等效 batch 近似 32。

---

### Q27. Gradient Clipping 为什么需要？

如果梯度突然非常大，参数一步可能被推得很远。

常见 global norm clipping：

```text
if ||g|| > threshold:
    g ← g * threshold / ||g||
```

RNN、RL、大模型训练中都可能使用。

---

## 六、Initialization 与训练稳定性

### Q28. 为什么参数不能全部初始化为 0？

如果同一层神经元初始权重完全相同，它们会得到相同梯度，始终学成一样的东西，产生**对称性问题**。

随机初始化就是为了打破这种对称。

---

### Q29. Xavier 和 Kaiming Initialization 在解决什么？

核心目标：让信号和梯度经过很多层后，不要快速爆炸或消失。

- Xavier：常与 tanh 等激活搭配；
- Kaiming/He：考虑 ReLU 截断特性。

现代 Transformer 还有自己的 residual / scaling 初始化策略，但底层目标相同：**控制方差传播。**

---

### Q30. Vanishing Gradient 和 Exploding Gradient 是什么？

链式法则不断乘局部导数：

```text
0.5 × 0.5 × 0.5 × ... → 0
2 × 2 × 2 × ... → huge
```

就可能出现梯度消失/爆炸。

解决思路包括：

- 合理初始化；
- ReLU 类激活；
- normalization；
- residual connection；
- gradient clipping；
- LSTM/GRU gate。

---

## 七、Normalization 与 Residual

### Q31. BatchNorm、LayerNorm、RMSNorm 最核心的区别？

### BatchNorm

常见 CNN 中按 batch 统计：

```text
同一 channel
跨 batch / spatial positions 统计均值方差
```

训练和推理行为不同，需要 running statistics。

### LayerNorm

对单个样本的 feature dimension 归一化，基本不依赖 batch size，适合 Transformer。

### RMSNorm

不减均值，只按 RMS 缩放，计算更简单，现代 LLM 很常见。

---

### Q32. Residual Connection 为什么如此重要？

```text
output = x + F(x)
```

模型不必直接学习完整映射，而只需要学习 residual `F(x)`。

它还给梯度提供更直接的路径，使非常深的网络更容易优化。

ResNet、Transformer 都大量依赖 residual connection。

---

### Q33. Dropout 是什么？

训练时随机把一部分 activation 置 0：

```text
train: random drop
inference: no random drop
```

目的是降低神经元之间的过度共适应。

注意：超大规模 LLM 中 dropout 的使用强度和位置可能与传统小模型不同，不能机械套固定数值。

---

## 八、Generalization

### Q34. Overfitting 和 Underfitting 怎么判断？

### Underfitting

```text
train error 高
val error 也高
```

说明模型/训练本身还没学好。

### Overfitting

```text
train error 很低
val error 明显更高
```

说明模型记住训练集，但泛化差。

---

### Q35. Train / Validation / Test 为什么不能混？

- Train：用于更新参数；
- Validation：用于调超参数、early stopping、选模型；
- Test：最终一次性评价泛化。

如果 test 被反复拿来调模型，它实际上已经变成 validation，最终指标会偏乐观。

大模型还必须考虑 benchmark contamination。

---

### Q36. Bias–Variance Tradeoff 怎么理解？

- 高 bias：模型太简单或训练不足，连训练规律都学不好；
- 高 variance：模型过度适应训练数据，对新数据不稳定。

今天的大模型非常复杂，但高质量大数据、预训练和正则化改变了传统“小数据下越大越容易过拟合”的直觉，所以面试回答要结合数据规模。

---

### Q37. Data Augmentation 为什么有效？

通过不改变任务语义的变换增加数据多样性。

图像：

- crop；
- flip；
- color jitter；
- MixUp / CutMix；
- Mosaic。

文本和多模态不能随意增强，因为某些变换会改变语义或图文对应关系。

---

### Q38. Label Smoothing 是什么？

普通 one-hot：

```text
correct class = 1
others        = 0
```

Label smoothing 会稍微降低正确类别目标概率，把少量概率分给其他类别，减少模型过度自信。

它适合部分分类任务，但不是所有生成/检测任务都应该机械使用。

---

## 九、CNN / RNN：为什么还要懂？

### Q39. 卷积到底做了什么？

一个 kernel 在图像上滑动，对局部区域做共享权重计算。

输入：

```text
[B, Cin, H, W]
```

卷积后：

```text
[B, Cout, Hout, Wout]
```

空间输出尺寸：

```text
Hout = floor((H + 2P - K) / S) + 1
```

其中：`K` kernel，`S` stride，`P` padding。

---

### Q40. CNN 为什么参数共享？

同一个卷积核在所有位置复用。

这带来：

- 参数效率高；
- 强局部先验；
- 对平移具有较好的等变性。

YOLO 等实时检测模型至今仍大量依赖卷积结构。

---

### Q41. Receptive Field 是什么？

某个高层 feature 对应原图中“能影响它”的区域。

网络越深、stride/pooling 越多，receptive field 越大。

检测任务需要同时兼顾：

- 小目标：高分辨率 feature；
- 大目标：大 receptive field。

这就是 FPN / PAN 多尺度结构的重要背景。

---

### Q42. Pooling 和 Strided Convolution 的作用？

都是降低空间分辨率、扩大有效感受野。

例如：

```text
640×640
↓ /2
320×320
↓ /2
160×160
↓ /2
80×80
```

现代网络很多时候直接用 stride=2 的 Conv 替代 pooling，使下采样本身也可学习。

---

### Q43. RNN 的核心问题是什么？

RNN：

```text
h_t = f(x_t, h_{t-1})
```

它天然处理序列，但：

- 时间步串行，训练难并行；
- 长距离梯度路径长；
- 容易 vanishing/exploding gradient。

Transformer 的优势之一就是摆脱这种严格时间递归。

---

### Q44. LSTM 为什么比普通 RNN 更能记长信息？

LSTM 引入 gate：

- forget gate；
- input gate；
- output gate；
- cell state。

关键是 cell state 提供一条更稳定的信息通路，让模型学习“什么保留、什么忘掉”。

---

## 十、Embedding 与表示学习

### Q45. Embedding 本质是什么？

Embedding 就是一个可学习查找表：

```text
vocab_size × hidden_dim
```

输入 token id：

```text
[B, L]
```

查表后：

```text
[B, L, D]
```

Embedding 把离散符号变成连续向量，后续神经网络才能计算相似度和组合关系。

---

### Q46. Feature、Embedding、Hidden State 有什么区别？

它们都可能是连续向量，但语境不同：

- Feature：泛指网络抽取的表示；
- Embedding：通常强调把离散/原始对象映射到向量空间；
- Hidden state：强调某一层网络内部当前状态。

不要把这三个词当成严格互斥的数据类型。

---

## 十一、Mixed Precision 与显存

### Q47. FP32、FP16、BF16 有什么区别？

### FP32

精度高，但显存和带宽开销大。

### FP16

显存减半、Tensor Core 友好，但 exponent 范围较小，更容易 overflow/underflow。

### BF16

和 FP32 一样有 8-bit exponent，动态范围更大，但 mantissa 更少。

因此现代大模型训练经常优先使用 BF16。

---

### Q48. Mixed Precision 为什么能加速？

不是所有计算都必须 FP32。

通常：

- 大矩阵乘用 BF16/FP16；
- 某些累加、optimizer state、敏感运算保留更高精度。

这样可以降低：

- 显存；
- memory bandwidth；
- Tensor Core 计算成本。

---

### Q49. FP16 为什么需要 Loss Scaling？

FP16 对非常小的梯度表示能力有限，梯度可能 underflow 到 0。

做法：

```text
loss × large_scale
→ backward
→ gradients × large_scale
→ unscale gradients
→ optimizer step
```

BF16 动态范围更大，所以通常不需要同样强的 loss scaling 机制。

---

### Q50. 训练显存主要花在哪里？

粗略分四类：

1. **Parameters**；
2. **Gradients**；
3. **Optimizer states**；
4. **Activations**。

Adam 类优化器还会保存一阶、二阶状态，所以训练显存远大于“参数量 × 2 bytes”。

对大模型，还要考虑：

- temporary buffers；
- communication buffers；
- fragmentation。

---

### Q51. Activation Checkpointing 为什么省显存？

普通训练会保留很多 forward activation 给 backward。

Checkpointing 只保存部分节点，backward 时重新计算缺失 activation：

```text
memory ↓
compute ↑
```

本质是用计算换显存。

---

## 十二、Transfer Learning 与 Fine-tuning

### Q52. Pretraining 和 Fine-tuning 有什么区别？

- Pretraining：在大规模通用数据上学习通用表示；
- Fine-tuning：在目标任务/领域数据上继续训练。

多模态模型常进一步分成：

```text
pretraining
→ alignment
→ instruction tuning
→ preference / RL
```

后面模块会详细展开。

---

### Q53. Freeze / Unfreeze 的意义是什么？

冻结模块：

```text
requires_grad = False
```

优点：

- 省显存；
- 少训练参数；
- 减少小数据下破坏预训练表示的风险。

缺点：目标领域差异大时适应能力不足。

因此常采用逐阶段解冻。

---

### Q54. Fine-tuning 时为什么可能 Catastrophic Forgetting？

如果新数据分布很窄、learning rate 又大，模型可能为了适应新任务破坏原有能力。

常见缓解：

- 更小 LR；
- 混入通用数据；
- 冻结部分参数；
- LoRA；
- regularization / distillation。

---

## 十三、训练 Debug 必会

### Q55. Loss 不下降，优先查什么？

推荐顺序：

```text
1. 数据和标签是否对齐
2. loss / mask 是否写对
3. model.train() / eval() 状态
4. 参数是否 requires_grad
5. gradient 是否为 0 / NaN
6. learning rate
7. normalization / preprocessing
8. 是否存在严重 class imbalance
```

不要一上来就换更复杂模型。

---

### Q56. Loss 变 NaN 常见原因？

- learning rate 过大；
- FP16 overflow；
- `log(0)` / 除 0；
- softmax 前 logits 极端；
- normalization 数值问题；
- exploding gradient；
- 数据中存在 NaN/Inf。

Debug 时要逐层检查 tensor 的：

```text
shape / min / max / mean / std / isfinite
```

---

### Q57. 训练正常但验证很差，优先考虑什么？

- train/val 数据分布不同；
- leakage / split 错误；
- overfitting；
- preprocessing 不一致；
- BatchNorm train/eval 状态错误；
- 验证指标实现错误。

真正工程中“评估代码 bug”非常常见。

---

## 十四、进入 Transformer 前必须能闭卷回答的 12 题

1. `[B,L,D] @ [D,D2]` 输出 shape 是什么？
2. Backprop 为什么依赖链式法则？
3. 为什么 `CrossEntropyLoss` 通常直接吃 logits？
4. Adam 和 AdamW 区别？
5. Warmup 为什么有用？
6. LayerNorm 为什么比 BatchNorm 更适合序列模型？
7. Residual connection 为什么让深网络更好训练？
8. FP16 和 BF16 最大区别？
9. Gradient accumulation 为什么能模拟大 batch？
10. Activation checkpointing 为什么能省显存？
11. Conv stride=2 后空间 shape 怎么变？
12. Embedding 为什么把 `[B,L]` 变成 `[B,L,D]`？

如果这 12 个问题说得清楚，再进入 Transformer 会轻松很多。

---

## Primary references

- Deep Learning — Goodfellow, Bengio & Courville: https://www.deeplearningbook.org/
- PyTorch Autograd: https://pytorch.org/docs/stable/autograd.html
- Adam: https://arxiv.org/abs/1412.6980
- AdamW: https://arxiv.org/abs/1711.05101
- Batch Normalization: https://arxiv.org/abs/1502.03167
- Layer Normalization: https://arxiv.org/abs/1607.06450
- RMSNorm: https://arxiv.org/abs/1910.07467
- ResNet: https://arxiv.org/abs/1512.03385
- Dropout: https://jmlr.org/papers/v15/srivastava14a.html
- Mixed Precision Training: https://arxiv.org/abs/1710.03740
