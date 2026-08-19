# 01 · Transformer & LLM Fundamentals

> 目标：从 **Tokenizer → Embedding → Attention → Transformer Block → Training → Decoding → KV Cache → Long Context → MoE → Serving** 建立完整知识链。
>
> 如果前面的 tensor、loss、optimizer、normalization 还不熟，先看：[00B Deep Learning Fundamentals](../00B_Deep_Learning_Fundamentals/README.md)。

---

# Part A. 从文本到模型输入

## Q1. LLM 看到的是“文字”吗？

不是。LLM 真正接收的是 **token id**。

```text
"I love AI"
   ↓ tokenizer
[40, 1842, 15592]
   ↓ embedding lookup
[B, L, D]
```

模型内部从头到尾都在处理数值 tensor。

---

## Q2. Tokenizer 是什么？

Tokenizer 把字符串转换成离散 token。

常见粒度：

- character；
- word；
- subword。

现代 LLM 大多使用 subword，因为它在 vocabulary 大小和未知词之间折中较好。

例如：

```text
unbelievable
→ un + believable
```

或者可能被切成更细的 pieces。

---

## Q3. BPE 的核心思想是什么？

Byte Pair Encoding 从较小基本单元开始，反复合并训练语料中最常见的相邻 token pair。

简化：

```text
l o w
l o w e r

发现 l+o 很常见
→ lo

再发现 lo+w 很常见
→ low
```

最终得到一套有限 vocabulary。

**核心直觉：高频片段用较少 token 表示，低频词仍能拆开表示。**

---

## Q4. BPE、WordPiece、SentencePiece 怎么区分？

面试不需要死背实现细节，抓住：

- BPE：频繁合并 symbol pairs；
- WordPiece：合并规则更强调语言模型/概率收益；
- SentencePiece：把分词当作原始字符串上的模型，可直接处理空格并支持 BPE/Unigram 等算法。

它们都服务于一个目标：**把开放的自然语言映射到有限 token vocabulary。**

---

## Q5. Vocabulary size 为什么不能无限大？

Embedding matrix：

```text
[V, D]
```

`V` 越大：

- embedding 参数越多；
- LM head 输出维度越大；
- softmax 成本增加。

但 `V` 太小又会让一句话被拆成更多 token，sequence length 增长。

所以 vocabulary size 是：

> 参数量 / 序列长度 / 多语言覆盖之间的权衡。

---

## Q6. BOS、EOS、PAD、UNK 是什么？

- `BOS`：begin of sequence；
- `EOS`：end of sequence；
- `PAD`：batch 对齐时补长度；
- `UNK`：unknown token，现代 byte/subword tokenizer 中往往更少依赖。

Chat model 还会有：

- system/user/assistant role tokens；
- tool call tokens；
- image/video special tokens。

---

## Q7. Embedding 是什么？

输入 token ids：

```text
[B, L]
```

查 embedding table：

```text
E: [V, D]
```

输出：

```text
X: [B, L, D]
```

本质上是：**每个离散 token id 对应一个可学习向量。**

---

## Q8. Hidden State、Logits、Probability 分别是什么？

典型 Decoder-only LLM：

```text
token ids
   ↓
embedding
[B,L,D]
   ↓
Transformer blocks
[B,L,D]      ← hidden states
   ↓
LM Head
[B,L,V]      ← logits
   ↓
softmax
[B,L,V]      ← probabilities
```

不要把 hidden state 和 token probability 混在一起。

---

## Q9. Weight Tying 是什么？

输入 embedding：

```text
[V,D]
```

输出 LM head 原本需要：

```text
[D,V]
```

Weight tying 可以让两者共享参数（通常转置使用），减少参数并让输入/输出 token 表示共享结构。

不是所有模型都必须这么做，但很常见。

---

# Part B. Transformer 为什么出现

## Q10. 为什么 Transformer 取代 RNN 成为大模型主干？

**一句话：** Transformer 用 attention 直接建立任意 token 之间的联系，同时训练阶段可以并行处理整个序列。

RNN：

```text
h1 → h2 → h3 → ... → hL
```

- 严格串行；
- 长距离依赖路径长；
- 梯度传播困难。

Self-Attention：

```text
每个 token ↔ 所有允许看到的 token
```

训练可以把整个 `[B,L,D]` 一次送入 GPU。

代价是标准 dense attention 在序列维度上有 `O(L²)` 的计算/中间矩阵压力。

---

## Q11. Transformer 原始 Encoder 和 Decoder 有什么区别？

原始 Transformer：

### Encoder

```text
Self-Attention
→ FFN
```

能双向看整个输入。

### Decoder

```text
Masked Self-Attention
→ Cross-Attention to encoder
→ FFN
```

生成时不能看未来 token。

现代通用 LLM 多采用 **Decoder-only**：反复堆 causal self-attention + FFN block。

---

## Q12. 为什么现代 LLM 大多采用 Decoder-only？

因为它把很多任务统一为：

```text
context → predict next token
```

优点：

- 训练目标简单；
- 预训练和生成形式一致；
- prompt、代码、工具结果、图像 token 都可以拼到上下文；
- 容易扩展到极大规模。

Encoder-only 更适合 representation；Encoder-Decoder 对翻译/seq2seq 仍然合理，并不是“过时”。

---

# Part C. Self-Attention 从 shape 开始

## Q13. Q、K、V 到底是什么？

输入：

```text
X: [B,L,D]
```

线性投影：

```text
Q = XWq
K = XWk
V = XWv
```

直观理解：

- **Q**：我现在要找什么信息；
- **K**：我能用什么特征被别人找到；
- **V**：如果别人关注我，我真正提供什么内容。

它们不是三个固定语义标签，而是模型训练出的连续表示。

---

## Q14. Self-Attention 完整公式是什么？

```text
Attention(Q,K,V)
= softmax(QKᵀ / √d_k + Mask) V
```

按顺序：

```text
Q [B,H,L,d]
K [B,H,L,d]
        ↓ Kᵀ
QKᵀ [B,H,L,L]
        ↓ scale + mask + softmax
A [B,H,L,L]
        ↓ × V
O [B,H,L,d]
```

其中 `A[i,j]` 表示第 `i` 个 query 对第 `j` 个 key 的注意力权重。

---

## Q15. 为什么 attention 要除以 `sqrt(d_k)`？

假设 Q/K 各维近似零均值、方差 1，点积是 `d_k` 个乘积相加，其方差大约随 `d_k` 增长。

`d_k` 大时 logits 绝对值会变大：

```text
softmax([20, 1, -8])
```

会过度饱和，使梯度变小。

除以 `sqrt(d_k)` 把尺度拉回更稳定范围。

---

## Q16. Multi-Head Attention 为什么需要多头？

单头只在一个投影空间计算相似度。

多头：

```text
[B,L,D]
→ [B,L,H,d]
→ [B,H,L,d]
```

其中：

```text
D = H × d
```

不同 head 可以学习不同的信息路由模式。

最后：

```text
heads concat
[B,L,D]
→ output projection
[B,L,D]
```

---

## Q17. 为什么多头通常不是把 hidden size 乘 H？

常见设计保持总 hidden size `D` 不变，只把它拆成 H 个 head：

```text
D = 4096
H = 32
head_dim = 128
```

不是：

```text
32 × 4096
```

否则参数和计算都会爆炸。

---

## Q18. Self-Attention 和 Cross-Attention 区别？

### Self-Attention

Q/K/V 来自同一序列。

### Cross-Attention

Q 和 K/V 来自不同序列。

多模态例子：

```text
Text hidden → Q
Image features → K,V
```

Flamingo 类使用 cross-attention；LLaVA 类更常把视觉 token 与文本 token 拼起来后做统一 self-attention。

---

# Part D. Mask

## Q19. Causal Mask 是什么？

生成第 `t` 个 token 时不能看到未来 token。

attention logits：

```text
      key
      1 2 3 4
q1    ✓ × × ×
q2    ✓ ✓ × ×
q3    ✓ ✓ ✓ ×
q4    ✓ ✓ ✓ ✓
```

未来位置加 `-∞`，softmax 后变成 0。

---

## Q20. Padding Mask 和 Causal Mask 有什么区别？

### Padding Mask

防止模型关注为了凑 batch 长度加入的 PAD。

### Causal Mask

防止模型看到未来。

Decoder-only training 经常同时需要两者。

---

## Q21. 为什么多模态 token 的 mask 更复杂？

例如：

```text
<image tokens> + user text + assistant text
```

需要同时考虑：

- PAD；
- causal order；
- 哪些视觉 token 可被哪些文本 token 看见；
- training loss 哪些位置需要 mask；
- packed sequence 中不同样本不能互相 attention。

因此 attention mask 和 loss mask 是两个不同概念。

---

# Part E. Transformer Block 内部到底发生什么

## Q22. 一个现代 Decoder Block 可以怎么画？

典型 Pre-Norm：

```text
x
│
├───────────────┐
↓ RMSNorm       │
Attention       │
↓               │
+ residual ◄────┘
│
├───────────────┐
↓ RMSNorm       │
FFN / SwiGLU    │
↓               │
+ residual ◄────┘
│
output
```

不同模型细节会变化，但这条主线非常常见。

---

## Q23. Residual Connection 为什么重要？

```text
x_{l+1} = x_l + F(x_l)
```

好处：

- 梯度有更直接路径；
- 网络只需要学习 residual；
- 深层模型更容易优化。

Transformer 能堆几十到几百层，与 residual 密切相关。

---

## Q24. LayerNorm 和 RMSNorm 有什么区别？

LayerNorm：

```text
(x - mean) / std
```

RMSNorm：

```text
x / sqrt(mean(x²)+eps)
```

RMSNorm 不减均值，结构更简单，现代 LLM 非常常见。

两者都比 BatchNorm 更适合变长序列，因为不依赖 batch 统计量。

---

## Q25. Pre-Norm 和 Post-Norm 区别？

### Post-Norm

```text
Norm(x + F(x))
```

### Pre-Norm

```text
x + F(Norm(x))
```

Pre-Norm 的 residual 主路径更接近 identity，深层训练通常更稳定，因此现代 LLM 中很常见。

---

## Q26. FFN 为什么很重要？

Attention 主要负责：

> token 之间交换信息。

FFN 主要负责：

> 对每个 token 的特征做非线性变换。

经典：

```text
D → Dff → D
```

由于 `Dff` 通常远大于 `D`，FFN 参数量常常非常大。

---

## Q27. SwiGLU 是什么？

简化：

```text
u = xW1
v = xW2
h = SiLU(u) ⊙ v
out = hW3
```

它比传统：

```text
Linear → GELU → Linear
```

多了一个 gate 分支。

很多现代 LLM 采用 SwiGLU/GLU family。

---

# Part F. Position Encoding

## Q28. Attention 为什么必须知道位置？

纯 self-attention 如果没有位置信息，对 token 排列本身不敏感。

例如：

```text
A B C
C B A
```

内容集合相同，但语义可能完全不同。

所以必须给模型某种位置表示。

---

## Q29. 原始 Sinusoidal Positional Encoding 是什么？

原始 Transformer 用不同频率的 sin/cos：

```text
PE(pos, 2i)   = sin(pos / 10000^(2i/D))
PE(pos, 2i+1) = cos(pos / 10000^(2i/D))
```

再加到 token embedding 上。

优点：无需学习每个绝对位置参数，并带有规则结构。

---

## Q30. RoPE 是什么？

RoPE 不直接把位置向量加到 hidden state，而是根据 position 对 Q/K 的二维分量做旋转。

简化理解：

```text
Q_pos = Rotate(Q, pos)
K_pos = Rotate(K, pos)
```

两者点积后自然带入相对位置信息。

---

## Q31. 为什么 RoPE 很适合现代 LLM？

- 与 attention 直接结合；
- 相对位置自然进入 QK 点积；
- 不增加 sequence-length 相关 embedding table；
- 可以扩展到长上下文；
- 可推广为多维位置编码。

在 VLM 中还可以表达：

```text
T / H / W
```

等多维位置。

---

## Q32. 长上下文为什么不能简单把 max length 改大？

因为训练时模型只见过一定位置范围。

直接 extrapolate 可能出现：

- RoPE phase 分布超出训练范围；
- attention pattern 失真；
- 内存和计算成本暴涨。

所以长上下文通常还需要：

- RoPE scaling；
- position interpolation；
- YaRN / NTK-aware 等方法；
- long-context continued training。

不要把“配置文件 max_position_embeddings 改大”当作真正长上下文能力。

---

# Part G. MHA / MQA / GQA / KV Cache

## Q33. MHA、MQA、GQA 区别？

### MHA

每个 Q head 都有独立 K/V head。

### MQA

所有 Q heads 共用一组 K/V。

### GQA

多个 Q heads 共享一组 K/V，介于两者之间。

例如：

```text
32 Q heads
8 KV heads
```

每 4 个 Q heads 共用一组 K/V。

---

## Q34. 为什么 GQA 能显著降低推理成本？

KV Cache 需要保存每层历史 token 的 K 和 V。

K/V head 越少：

```text
KV cache ↓
memory bandwidth ↓
```

而 Q 只对当前新 token 临时计算，不需要长期缓存。

因此 GQA 在 decoder inference 中很划算。

---

## Q35. KV Cache 到底缓存什么？

生成第 `t` 个 token：

过去 token 的 K/V 已经计算过，并且不会改变。

所以缓存：

```text
K_cache[layer]: [B, n_kv_heads, L, head_dim]
V_cache[layer]: [B, n_kv_heads, L, head_dim]
```

新 token 只追加新的 K/V。

---

## Q36. KV Cache 显存怎么估算？

近似：

```text
2
× B
× L
× n_layers
× n_kv_heads
× head_dim
× bytes_per_element
```

`2` 是 K 和 V。

例如视觉 token、长视频都会让 `L` 很大，因此多模态 serving 特别关心 KV cache。

---

# Part H. Training Objective

## Q37. LLM 预训练到底怎么构造标签？

输入：

```text
I love deep learning
```

模型实际上训练：

```text
输入: I     → 目标: love
输入: I love → 目标: deep
输入: I love deep → 目标: learning
```

实现时常用 shift：

```text
logits[:, :-1]
labels[:, 1:]
```

---

## Q38. Teacher Forcing 是什么？

训练预测第 `t` 个 token 时，输入的是**真实历史 token**，而不是模型自己之前生成的 token。

所以训练可以并行计算整段 sequence。

推理时则不同：

```text
模型生成 token_t
→ append
→ 再生成 token_{t+1}
```

这是训练和生成速度差异的重要原因。

---

## Q39. LLM 的 Cross-Entropy Loss 怎么算？

每个有效位置都有：

```text
logits: [V]
label: 一个 token id
```

loss：

```text
L_t = -log P(y_t | x_<t)
```

再对有效 token 求平均。

Chat SFT 常把 system/user/input tokens 的 label 设为 `-100`，只对 assistant answer 计算 loss。

---

## Q40. Perplexity 是什么？

常见定义：

```text
PPL = exp(average NLL)
```

直观上：模型对下一个 token 越确定，PPL 越低。

但不同 tokenizer/vocabulary 下 PPL 不宜直接机械横向比较。

---

## Q41. Sequence Packing 是什么？

训练数据长度差异很大，如果每个短样本都 pad 到统一最大长度，非常浪费。

Packing：

```text
sample A + sample B + sample C
→ pack 到同一个长 sequence
```

但 attention mask 必须保证不同样本不能错误互相看到。

它能显著提高 token utilization。

---

# Part I. 推理到底怎么一步一步生成

## Q42. 一个 Decoder-only LLM 从 prompt 到第一个 token 的完整流程？

```text
Prompt text
   ↓ tokenizer
Token IDs [B,L]
   ↓ embedding
[B,L,D]
   ↓ Transformer blocks
[B,L,D]
   ↓ 取最后位置 hidden state
[B,D]
   ↓ LM Head
[B,V]
   ↓ decoding strategy
next token id
   ↓ append to context
repeat
```

这条链必须能闭卷画出来。

---

## Q43. Prefill 和 Decode 区别？

### Prefill

一次处理整个 prompt：

```text
L tokens → Transformer
```

矩阵规模大，通常更 compute-bound。

### Decode

每次只生成 1 个或少量 token，但需要：

- 读取大量模型权重；
- 读取历史 KV cache。

因此更容易 memory-bandwidth-bound。

---

# Part J. Decoding Strategies

## Q44. Greedy Decoding 是什么？

每一步：

```text
argmax P(token)
```

优点：确定、快。

缺点：局部最优，不一定得到整体最好的序列，也容易输出模式化。

---

## Q45. Temperature 做什么？

```text
softmax(logits / T)
```

- `T < 1`：分布更尖锐，更确定；
- `T > 1`：分布更平，更随机。

Temperature 不改变模型参数，只改变 sampling distribution。

---

## Q46. Top-k Sampling 是什么？

只保留概率最高的 `k` 个 token，然后重新归一化采样。

例如：

```text
V = 150000
k = 50
```

每步只从最高 50 个候选中采样。

---

## Q47. Top-p / Nucleus Sampling 是什么？

选择最小 token 集合，使累计概率达到 `p`：

```text
Σ P(token) >= p
```

候选数量会动态变化。

这是它和固定 top-k 的主要区别。

---

## Q48. Beam Search 为什么在聊天 LLM 中没那么常用？

Beam Search 保留多个高概率序列分支，适合翻译等概率目标明确的 seq2seq。

开放式聊天中：

- 高 likelihood 不一定等于高质量；
- 容易生成保守、重复文本；
- 计算成本更高。

因此 chat LLM 更常使用 sampling family。

---

# Part K. Attention 复杂度与高效注意力

## Q49. Self-Attention 为什么是 `O(L²)`？

关键矩阵：

```text
QKᵀ: [L,d] @ [d,L] → [L,L]
```

需要对所有 token pair 计算相似度。

计算近似：

```text
O(L²d)
```

attention score 中间矩阵空间规模近似 `O(L²)`。

---

## Q50. 为什么视觉/视频让这个问题更严重？

假设一张图片变成 1024 visual tokens，文本本来只有 500 tokens：

```text
L: 500 → 1524
```

attention pair 数不是增加 3 倍，而近似：

```text
500²   = 0.25M
1524² ≈ 2.32M
```

所以 visual-token compression 对 MLLM 非常重要。

---

## Q51. FlashAttention 改变了 `O(L²)` 理论复杂度吗？

没有。

它的关键不是把 attention 变成 linear attention，而是：

> 通过 tiling、重计算和更好的 SRAM/HBM 数据访问，减少昂贵的显存读写。

数学结果仍然是 exact attention。

---

## Q52. Sliding Window Attention 是什么？

每个 token 只看附近窗口：

```text
窗口大小 W
复杂度约 O(LW)
```

优点：长序列便宜。

缺点：远距离信息不能一步直接交流。

因此一些模型会混合：

```text
local layers + occasional global layers
```

---

## Q53. Linear / Recurrent Attention 在解决什么？

目标是避免显式构造完整 `[L,L]` attention matrix。

不同方法可能使用：

- kernel trick；
- recurrent state；
- state-space / gated recurrence。

它们通常让长序列扩展更高效，但表达能力、训练稳定性和 cache 机制与标准 attention 不同。

---

## Q54. Hybrid Architecture 是什么？

不是所有层都必须使用同一种 sequence mixer。

例如可能：

```text
Full Attention
Recurrent/Linear Block
Recurrent/Linear Block
Full Attention
...
```

核心思想：

> 用少量强全局交互 + 大量更便宜的长序列模块做能力/成本折中。

---

# Part L. Mixture of Experts

## Q55. MoE 的核心思想是什么？

把 FFN 替换成多个 expert：

```text
x
↓ router
scores over experts
↓ top-k
Expert 2 + Expert 7
↓ weighted combine
output
```

不是每个 token 都跑所有 experts。

---

## Q56. Total Parameters 和 Active Parameters 区别？

例如：

```text
8 experts
每次激活 top-2
```

总参数包含 8 个专家；
单 token 计算只走其中 2 个。

因此 MoE 可以增加模型容量，同时控制单 token FLOPs。

---

## Q57. MoE 为什么不一定更快？

因为还存在：

- router 开销；
- token dispatch；
- all-to-all communication；
- expert load imbalance；
- batch 太小时 GPU 利用率差。

所以“active params 少”不等于端到端 latency 一定低。

---

## Q58. Load Balancing 为什么重要？

如果 80% token 都进入同一个 expert：

```text
Expert A: overload
Expert B-H: under-utilized
```

会导致：

- 丢 token / capacity overflow；
- 分布式 straggler；
- 专家学习失衡。

因此常引入 auxiliary balancing loss 或其他 router balancing 方法。

---

# Part M. 参数量、显存和计算

## Q59. 一个 Linear 层参数量怎么算？

```text
Linear(Din, Dout)
```

参数：

```text
Din × Dout + Dout(bias)
```

LLM 很多 Linear 默认不使用 bias，所以要看具体实现。

---

## Q60. Attention 的 QKV 参数量怎么粗估？

MHA 情况下，如果输入输出 hidden size 都为 D：

```text
Wq: D×D
Wk: D×D
Wv: D×D
Wo: D×D
```

约：

```text
4D²
```

GQA 时 K/V projection 会因为 KV heads 更少而下降。

---

## Q61. FFN 参数量为什么常比 Attention 大？

若经典 FFN：

```text
D → 4D → D
```

两层约：

```text
8D²
```

而 attention projection 约：

```text
4D²
```

SwiGLU 会有三个 projection，具体 expansion ratio 通常重新调整。

---

## Q62. 参数量和运行显存为什么不是一回事？

Inference 除权重外还有：

- KV cache；
- activations；
- temporary buffers。

Training 还要加：

- gradients；
- optimizer states；
- forward activations。

所以：

> 7B 参数 ≠ 只需要 7B×2 bytes 显存就能训练。

---

# Part N. Pretraining → SFT → Alignment

## Q63. Pretraining、SFT、Preference/RL 的角色分别是什么？

### Pretraining

学世界知识、语言结构、基础能力。

### SFT

学：

- 指令跟随；
- 对话格式；
- task behavior；
- tool format。

### Preference / RL

进一步优化：

- helpfulness；
- reasoning behavior；
- safety；
- agent success。

详细内容放在：

- [06 Pretraining / SFT / PEFT](../06_Pretraining_SFT_PEFT/README.md)
- [07 Post-training / RL / Reasoning](../07_PostTraining_RL_Reasoning/README.md)

---

# Part O. 多模态为什么必须建立在这些基础上

## Q64. 图像进入 LLM 后，本质发生什么？

典型 VLM：

```text
Image [B,3,H,W]
   ↓ Vision Encoder
Visual Features [B,N,Dv]
   ↓ Projector
Visual Tokens [B,N,Dl]
   ↓ concat with text embeddings
[B,L_total,Dl]
   ↓ LLM
```

一旦进入 LLM，后面的：

- Attention；
- RoPE；
- GQA；
- KV Cache；
- Prefill；
- MoE；

都和纯文本 LLM 是同一套基础。

---

## Q65. 为什么视觉 token 数是 MLLM 的核心工程指标？

因为它同时影响：

```text
sequence length
    ↓
attention compute
prefill latency
KV cache
memory
throughput
```

所以 dynamic resolution、token merge、resampler、ViR、visual-token compression，本质都在控制：

> **信息保真度 vs token cost**。

---

# Part P. 面试中最常见的连续追问链

## 追问链 1：Attention

```text
什么是 attention？
→ QKV shape？
→ 为什么 sqrt(dk)？
→ 为什么 multi-head？
→ causal mask？
→ O(L²) 从哪来？
→ FlashAttention 优化什么？
→ GQA 为什么省 cache？
```

## 追问链 2：训练

```text
LLM 怎么训练？
→ next-token prediction
→ label shift
→ cross entropy
→ teacher forcing
→ padding/loss mask
→ packing
→ warmup / AdamW
```

## 追问链 3：推理

```text
输入 prompt 后发生什么？
→ tokenizer
→ embedding
→ prefill
→ KV cache
→ LM head
→ sampling
→ decode loop
→ TTFT / TPOT
```

## 追问链 4：多模态

```text
图片怎么进 LLM？
→ Vision Encoder
→ [B,N,Dv]
→ Projector
→ [B,N,Dl]
→ concat
→ L_total 增加
→ prefill / attention / cache 成本增加
```

---

# 闭卷通过标准：25 个必须能回答的问题

1. Tokenizer 为什么需要 subword？
2. `[B,L]` 怎么变成 `[B,L,D]`？
3. hidden state 和 logits 区别？
4. Decoder-only 为什么适合大模型？
5. Q/K/V 分别来自哪里？
6. `QK^T` 的 shape 是什么？
7. 为什么除以 `sqrt(d_k)`？
8. Multi-Head 怎么 reshape？
9. causal mask 和 padding mask 区别？
10. residual connection 为什么重要？
11. RMSNorm 和 LayerNorm 区别？
12. FFN 在 Transformer 中负责什么？
13. SwiGLU 为什么有两个输入分支？
14. RoPE 为什么作用在 Q/K？
15. GQA 为什么省 KV cache？
16. KV cache 的 shape 和显存公式？
17. next-token labels 怎么 shift？
18. teacher forcing 为什么允许训练并行？
19. prefill 和 decode 瓶颈区别？
20. temperature / top-k / top-p 区别？
21. `O(L²)` 到底来自哪里？
22. FlashAttention 为什么不是 linear attention？
23. MoE active params 是什么意思？
24. 参数量为什么不等于显存占用？
25. 图片多 1000 个 visual tokens 会影响哪些系统指标？

---

## Primary references

- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- RoFormer / RoPE: https://arxiv.org/abs/2104.09864
- GQA: https://arxiv.org/abs/2305.13245
- RMSNorm: https://arxiv.org/abs/1910.07467
- GLU Variants / SwiGLU: https://arxiv.org/abs/2002.05202
- FlashAttention: https://arxiv.org/abs/2205.14135
- MQA: https://arxiv.org/abs/1911.02150
- SentencePiece: https://arxiv.org/abs/1808.06226
- Switch Transformer / MoE: https://arxiv.org/abs/2101.03961
