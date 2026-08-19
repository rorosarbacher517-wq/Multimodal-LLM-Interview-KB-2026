# Detection、Segmentation、Grounding 到底有什么区别？

## 面试一句话

Detection 回答“是什么、在哪里”；Segmentation 进一步给出像素级区域；Grounding 则把自然语言中的对象和图像区域对齐。

## 核心回答

- **Object Detection**：输出 bbox、类别和置信度，例如 `boxes [N,4] + scores + labels`。
- **Instance Segmentation**：在 detection 基础上再为每个实例输出 mask。
- **Semantic Segmentation**：给每个像素类别，但通常不区分同类的不同实例。
- **Visual Grounding**：输入 category name 或 referring expression，输出与文本对应的 box/region。
- **Open-vocabulary detection**：类别不再固定在训练时的 `num_classes`，而由文本/视觉 prompt 定义。

## 面试追问

Grounding 和普通 VQA 的关键区别是：Grounding 必须给出**空间对应关系**，而 VQA 只要求最终语言答案。
