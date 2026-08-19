# 00C · Machine Learning Fundamentals

> 目标：补齐算法岗仍然高频的传统机器学习基础。它不是和大模型“无关的旧知识”，而是数据质量建模、排序、异常检测、特征诊断、轻量 baseline 和实验分析的重要工具。
>
> 建议顺序：**问题定义 → 数据划分 → 线性模型 → 树模型 → 聚类/降维 → 指标 → 泛化与诊断**。

---

## Part A. 问题定义与数据

### Q1. 监督学习、无监督学习、自监督学习、强化学习怎么区分？
- **监督学习**：有人工/业务标签，学习 `x → y`。
- **无监督学习**：没有目标标签，发现结构，例如聚类。
- **自监督学习**：标签从数据本身构造，例如 masked prediction、contrastive learning。
- **强化学习**：通过 action 与环境交互，根据 reward 学 policy。

多模态预训练里大量使用自监督/弱监督，后训练又会结合监督学习和 RL。

### Q2. Regression、Classification、Ranking 有什么区别？
- Regression：输出连续值，例如质量分数。
- Classification：输出类别概率，例如“是否低质”。
- Ranking：关注相对顺序，例如检索 reranker。

面试先明确任务类型，再谈 loss 和 metric。

### Q3. Train / Validation / Test 为什么必须分开？
- Train：更新参数。
- Validation：选模型、阈值、超参。
- Test：最后一次独立评估。

如果 test 参与调参，就不再是真正独立测试。

### Q4. 什么是 Data Leakage？
训练时获得了部署时不应知道的信息。例如：
- 同一个用户/站点同时出现在 train 和 test；
- 先用全数据统计均值再切分；
- 未来信息进入历史预测；
- benchmark 样本进入训练语料。

泄漏通常比“模型选错”更严重，因为结果会看起来非常漂亮但无法泛化。

### Q5. IID Split、Time Split、Group Split 怎么选？
- IID/random split：样本近似独立同分布。
- Time split：未来预测必须按时间切。
- Group split：用户、站点、病人、视频等不能跨集合泄漏。

真实问题先决定泛化目标，再决定 split。

### Q6. Bias–Variance Trade-off 怎么理解？
- 高 bias：模型太简单，训练和验证都差。
- 高 variance：训练很好，验证明显差。

增加模型复杂度通常降低 bias、提高 variance；更多高质量数据、正则化和合适 inductive bias 可降低 variance。

### Q7. Overfitting 和 Underfitting 如何从曲线判断？
- train loss 高、val loss 也高：更像 underfitting。
- train 很低、val 明显更差：更像 overfitting。
- 两者都持续改善：可以继续训练。

不要只看最终一个点，最好看完整 learning curve。

---

## Part B. 线性模型

### Q8. Linear Regression 在学什么？

```text
y_hat = Xw + b
```

它假设输入特征对目标的影响可以通过线性组合表示。价值在于：简单、可解释、是非常好的 baseline。

### Q9. 为什么最小二乘对应 MSE？
最小化残差平方：

```text
Σ (y - y_hat)^2
```

在“噪声近似高斯且方差固定”的假设下，也可以从最大似然推导出 MSE。

### Q10. Logistic Regression 为什么名字叫 Regression 却做 Classification？
它先做线性打分：

```text
z = w^T x + b
```

再通过 sigmoid 得到二分类概率：

```text
p = 1 / (1 + exp(-z))
```

所以它本质是**线性决策边界 + 概率输出**。

### Q11. Sigmoid 和 Softmax 区别？
- Sigmoid：每个输出独立映射到 `[0,1]`，适合 multi-label。
- Softmax：多个类别归一化为总和 1，适合 mutually exclusive multi-class。

### Q12. L1 与 L2 Regularization 区别？
- L1：`λ|w|`，更容易产生稀疏权重。
- L2：`λw²`，平滑压小权重。

不要机械地说“L1 一定做特征选择”；效果取决于数据相关性和优化。

### Q13. 为什么很多传统模型需要 Feature Standardization？
如果不同特征尺度差异巨大：
- 距离模型会被大尺度特征主导；
- 梯度优化条件数变差；
- 正则化对各维影响不一致。

Tree-based model 对单调尺度变化通常不那么敏感。

---

## Part C. 距离、间隔与树模型

### Q14. KNN 的核心是什么？
根据距离找到最近的 `K` 个训练样本，用邻居投票/平均预测。

优点：几乎没有训练；缺点：推理慢、高维距离退化、对尺度敏感。

### Q15. 什么是 Curse of Dimensionality？
维度升高后，样本空间变得极其稀疏，最近和最远距离的差别可能变小。KNN、密度估计等方法会明显受影响。

### Q16. SVM 的 Margin 是什么？
SVM 不只想把样本分开，还希望找到与最近样本距离最大的分界面。

```text
更大 margin → 对小扰动更鲁棒
```

### Q17. Kernel Trick 在做什么？
不显式构造高维映射 `φ(x)`，而是直接计算：

```text
K(x_i, x_j) = <φ(x_i), φ(x_j)>
```

从而得到非线性边界。

### Q18. Decision Tree 如何决定一次分裂？
寻找“特征 + 阈值”，让子节点更纯。分类常用 Gini/Entropy；回归常用方差/MSE reduction。

树的优势是非线性和特征交互自然；缺点是单棵树方差大。

### Q19. Random Forest 为什么比单棵树稳？
对多个 bootstrap 数据子集训练多棵树，并随机抽特征，最后平均/投票。

核心是通过**降低树之间相关性 + ensemble** 降低 variance。

### Q20. Bagging 和 Boosting 的区别？
- Bagging：多个模型相对独立训练，再平均；主要降 variance。
- Boosting：后一个模型持续关注前面没学好的部分；逐步构造强模型。

Random Forest 是典型 bagging；GBDT/XGBoost 属于 boosting。

### Q21. GBDT 的核心思想？
每一步新增一棵树去拟合当前模型的 residual / negative gradient：

```text
F_m(x) = F_{m-1}(x) + η h_m(x)
```

所以它是在函数空间里做 gradient boosting。

### Q22. XGBoost 为什么常作为强 baseline？
它把 gradient boosting 做成高度工程化的树模型系统，支持二阶信息、正则化、缺失值处理、列采样、并行等。

结构化/tabular 数据上它通常是非常强的起点。

---

## Part D. 类别不平衡与概率质量

### Q23. 类别极不平衡时为什么 Accuracy 会骗人？
如果 99% 都是负样本，全部预测负就有 99% accuracy，但正样本完全找不到。

应结合 precision、recall、F1、PR-AUC 和业务 cost。

### Q24. Class Weight、Oversampling、Undersampling 怎么选？
- class weight：改变 loss 权重；
- oversampling：提高少数类出现频率；
- undersampling：减少多数类。

都可能有效，但要在独立 validation 上看 calibration 和真实分布表现。

### Q25. 什么是 Calibration？
如果模型给出 0.8 概率的样本中，长期约 80% 真的为正，则模型较校准。

排序好不代表概率准。风险决策、阈值策略和 agent confidence 都很依赖 calibration。

---

## Part E. 聚类、降维与异常发现

### Q26. K-Means 在优化什么？
把样本分成 K 组，使样本到所属 cluster center 的平方距离之和最小。

对球状、尺度相近的 cluster 更合适；对复杂形状不一定好。

### Q27. DBSCAN 和 K-Means 区别？
DBSCAN 基于局部密度：
- 不必预先指定 cluster 数；
- 能发现不规则形状；
- 可标记 noise。

但对不同密度和高维 embedding 参数更难选。

### Q28. PCA 为什么能降维？
寻找方差最大的正交方向，把数据投影到前几个 principal components。

它是线性方法，适合压缩、可视化前处理、去冗余；数学基础见 00A 的 eigen/SVD。

### Q29. t-SNE / UMAP 能不能证明数据天然分成几类？
不能。它们主要用于低维可视化，结果受超参数和随机性影响。

“图上分开”不等于高维空间一定有稳定 cluster。

### Q30. 多模态数据工程为什么也会用 Clustering？
例如：
- embedding 聚类做数据分桶；
- 发现重复/模板；
- bad-case taxonomy；
- long-tail domain discovery；
- active sampling。

---

## Part F. Evaluation

### Q31. Precision、Recall、F1 怎么记？

```text
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1        = 2PR / (P + R)
```

- Precision：报出来的有多少是真的。
- Recall：真的有多少被找到了。

### Q32. ROC-AUC 和 PR-AUC 怎么选？
ROC-AUC 看 TPR/FPR；PR-AUC 更关注 positive class 的 precision-recall。

类别极不平衡时，PR-AUC 往往更直观。

### Q33. RMSE、MAE、R² 分别反映什么？
- MAE：平均绝对误差，较直观。
- RMSE：平方后再开根，对大误差更敏感。
- R²：相对均值 baseline 解释了多少方差；可能为负。

### Q34. Ranking 常见指标有哪些？
- Recall@K：目标是否被召回；
- Precision@K；
- MRR：第一个正确结果的位置；
- NDCG：考虑不同相关等级和排序位置。

多模态检索通常不能只报一个 Recall@1。

### Q35. Cross Validation 为什么有用？
当数据不大时，通过多个 train/validation split 减少一次划分的偶然性。

但 time/group 数据必须用相应 blocked CV，不能破坏真实泛化约束。

### Q36. Hyperparameter Search 怎么做更合理？
常见：grid、random、Bayesian/Optuna-style search。

高维空间 random search 通常比全 grid 更有效；最终仍需固定 test 做一次独立评估。

### Q37. Distribution Shift / OOD 是什么？
部署分布和训练分布不一样。例如新设备、新地区、新界面、新语言。

模型性能下降不一定是过拟合，也可能是 covariate/label/concept shift。

### Q38. 一个传统 ML baseline 应该如何进入大模型项目？
先做简单、可解释、便宜的 baseline：

```text
数据特征 → Linear / RF / XGBoost
```

它能帮助判断：复杂模型的增益到底来自表示能力，还是数据本身已经容易解决。

### Q39. 面试被问“你会不会传统 ML”，最重要的回答框架？
不要背模型列表。按：

**任务定义 → split → baseline → feature → loss → metric → overfit diagnosis → calibration → ablation**。

这套思路同样适用于深度学习和大模型实验。
