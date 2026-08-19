# Machine Learning Models — Structure, Input Dimensions & Innovation Logic

> 传统机器学习没有“层层 tensor backbone”这一统一结构，因此这里不强行画神经网络层，而是统一记录：**输入 shape → 决策结构 → 输出 shape → 相对前一类方法的核心创新**。

# 1. Linear Regression

```mermaid
flowchart LR
    X["Features X\n[B,D]"] --> L["Linear map\ny = Xw + b"]
    W["w\n[D,1]"] --> L
    L --> Y["Prediction\n[B,1]"]
```

```text
X                         [B,D]
w                         [D,1]
y_hat                     [B,1]
```

**核心意义：** 最简单的连续预测 baseline；每个特征通过一个线性系数直接贡献到输出。

---

# 2. Logistic Regression

```mermaid
flowchart LR
    X["X\n[B,D]"] --> Z["z=Xw+b\n[B,1]"]
    Z --> S["sigmoid"]
    S --> P["p(y=1|x)\n[B,1]"]
```

多分类 softmax 版本：

```text
W                         [D,K]
logits                    [B,K]
probabilities             [B,K]
```

**创新点相对线性回归：** 线性 score 后接概率 link function，把回归式线性组合变成分类概率模型。

---

# 3. KNN

```mermaid
flowchart LR
    Q["Query\n[Bq,D]"] --> DIST["Distance to train set\n[Bq,Ntrain]"]
    TR["Train features\n[Ntrain,D]"] --> DIST
    DIST --> TOP["Top-K nearest indices\n[Bq,K]"]
    TOP --> V["Vote / average"]
    V --> O["Prediction\n[Bq] or [Bq,C]"]
```

**结构特点：** 几乎没有参数训练；主要成本发生在 inference 的 neighbor search。高维时距离可区分性下降。

---

# 4. SVM

线性 SVM：

```text
X                         [B,D]
w                         [D]
score = Xw+b              [B]
```

```mermaid
flowchart LR
    X["Samples in D-dimensional space"] --> H["Maximum-margin hyperplane"]
    H --> O["signed decision score"]
```

Kernel SVM：

```text
kernel matrix K           [B,B]
K_ij = K(x_i,x_j)
```

**创新点：** 不只要求分类正确，还最大化 decision boundary 到最近样本的 margin；kernel trick 可在不显式构造高维 `φ(x)` 的情况下得到非线性边界。

---

# 5. Decision Tree

```mermaid
flowchart TB
    X["X [B,D]"] --> N1{"feature j < threshold?"}
    N1 -->|yes| N2{"next split"}
    N1 -->|no| N3{"next split"}
    N2 --> L1["leaf prediction"]
    N2 --> L2["leaf prediction"]
    N3 --> L3["leaf prediction"]
    N3 --> L4["leaf prediction"]
```

**结构特点：** 每个内部节点选择一个 feature + threshold；路径长度约等于 tree depth。天然表达非线性和 feature interaction。

---

# 6. Random Forest

```mermaid
flowchart LR
    X["Training data\n[N,D]"] --> B1["Bootstrap sample 1"]
    X --> B2["Bootstrap sample 2"]
    X --> BN["Bootstrap sample M"]
    B1 --> T1["Tree 1"]
    B2 --> T2["Tree 2"]
    BN --> TN["Tree M"]
    T1 --> A["Average / majority vote"]
    T2 --> A
    TN --> A
```

### 维度

```text
input                      [B,D]
M tree predictions         [B,M] regression
or                         [B,M,K] class probabilities
ensemble output            [B] / [B,K]
```

**创新点相对单树：** bootstrap + random feature subset 降低不同树之间相关性，再用 ensemble 降低 variance。

口诀：`树容易抖；森林让很多不完全一样的树投票。`

---

# 7. GBDT

```mermaid
flowchart LR
    X["X"] --> T1["Tree 1"]
    T1 --> R1["Residual / negative gradient"]
    R1 --> T2["Tree 2"]
    T2 --> R2["New residual"]
    R2 --> TN["Tree M"]
    T1 --> S["Weighted sum"]
    T2 --> S
    TN --> S
```

```text
F_m(x) = F_{m-1}(x) + η h_m(x)
```

**创新点相对 Random Forest：** 不是独立并行造树，而是串行地让下一棵树修正当前 ensemble 的错误。

口诀：`RF 并行投票；GBDT 串行纠错。`

---

# 8. XGBoost

整体 prediction shape 与 GBDT 相同：

```text
X                         [B,D]
M trees → scores          [B,M]
aggregate                 [B] / [B,K]
```

```mermaid
flowchart LR
    X["Features"] --> G["Gradient + Hessian statistics"]
    G --> T["Regularized tree growth"]
    T --> A["Additive boosted ensemble"]
```

**创新点相对基础 GBDT：** 二阶 gradient/Hessian information、显式 regularization、column sampling、missing-value direction 和高效工程实现，使 boosting tree 成为 tabular 强 baseline。

---

# 9. K-Means

```mermaid
flowchart LR
    X["Samples\n[N,D]"] --> D["Distance to centers\n[N,K]"]
    C["Centers\n[K,D]"] --> D
    D --> A["Assign cluster id\n[N]"]
    A --> U["Recompute centers\n[K,D]"]
    U --> D
```

**创新/核心：** 交替做 assignment 和 centroid update，最小化样本到所属中心的平方距离。

---

# 10. DBSCAN

```text
input points               [N,D]
pair/local neighbor search neighborhood-dependent
output cluster id          [N]
noise label                [N]
```

```mermaid
flowchart LR
    X["Points"] --> N["ε-neighborhood search"]
    N --> C["Core points: neighbors ≥ min_samples"]
    C --> E["Density-connected expansion"]
    E --> O["clusters + noise"]
```

**创新点相对 K-Means：** cluster 由 density connectivity 定义，不要求球状 cluster，也不用提前指定 `K`，还能显式标 noise。

---

# 11. PCA

```mermaid
flowchart LR
    X["Centered data\n[N,D]"] --> C["Covariance / SVD"]
    C --> W["Top-r components\n[D,r]"]
    X --> P["Projection XW\n[N,r]"]
    W --> P
```

### Shape

```text
X                         [N,D]
principal directions      [D,r]
reduced representation    [N,r]
```

**核心意义：** 找到最大方差的正交方向，用线性投影压缩冗余维度；不是 nonlinear representation model。

---

# 12. t-SNE / UMAP：可视化映射而非监督预测模型

典型输入/输出：

```text
high-dimensional X        [N,D]
low-dimensional embedding [N,2] or [N,3]
```

**关键提醒：** 低维图“看起来分成几团”不能直接证明原高维数据天然存在稳定类别结构。

---

# 一张表记住传统模型

| Model | 输入 | 核心结构 | 输出 | 该记什么 |
|---|---|---|---|---|
| Linear Regression | `[B,D]` | one linear map | `[B,1]` | continuous linear baseline |
| Logistic Regression | `[B,D]` | linear + sigmoid/softmax | `[B,K]` | linear probability classifier |
| KNN | query + training set | nearest-neighbor search | labels/value | lazy learning |
| SVM | `[B,D]` | maximum-margin boundary | score/class | margin + kernel |
| Decision Tree | `[B,D]` | feature-threshold tree | leaf output | nonlinear rules |
| Random Forest | `[B,D]` | many independent trees | vote/mean | bagging lowers variance |
| GBDT | `[B,D]` | sequential residual trees | additive score | boosting |
| XGBoost | `[B,D]` | regularized second-order boosting | additive score | strong engineered GBDT |
| K-Means | `[N,D]` | K centers `[K,D]` | cluster ids | centroid iteration |
| DBSCAN | `[N,D]` | density connectivity | clusters/noise | arbitrary shapes + noise |
| PCA | `[N,D]` | projection `[D,r]` | `[N,r]` | linear variance-preserving compression |

## 面试记忆口诀

```text
线性回归：直接加权
逻辑回归：加权后过 sigmoid/softmax
KNN：问邻居
SVM：找最大间隔
Tree：一路问阈值
RF：并行很多树
GBDT：后一棵修前一棵
XGBoost：把 boosting 做得更强更工程化
K-Means：围着中心分组
DBSCAN：按密度连起来
PCA：找最大方差方向
```
