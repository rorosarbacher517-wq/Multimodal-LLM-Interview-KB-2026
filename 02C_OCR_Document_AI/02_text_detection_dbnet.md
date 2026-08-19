# Text Detection：DBNet 为什么常用

## 面试一句话

DBNet 把文字检测看成像素级分割，并把传统不可导的二值化过程改成 **Differentiable Binarization**，因此可以端到端学习文字区域边界。

## 核心回答

- Backbone 提取特征，FPN 融合多尺度信息。
- 网络预测 probability map `P` 和 threshold map `T`。
- 用可微近似得到 binary map：`B = sigmoid(k(P-T))`。
- 后处理从 binary map 提取连通区域，再恢复 polygon/box。

## 为什么适合文字

文字可能很长、弯曲、方向任意。分割式表示比固定 anchor 更自然。

## 常见追问

**检测和识别为什么常分开？**

整页先找文本区域，再把 crop 送给 recognizer，可以分别优化召回率和字符准确率，也方便替换模块。

## Reference

- DBNet: https://arxiv.org/abs/1911.08947