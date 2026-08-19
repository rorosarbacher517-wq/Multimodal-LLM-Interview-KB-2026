# 05_视觉grounding为什么重要

## 面试一句话

grounding 让“语言中的对象”对应到图像中的 bbox/point/region，是降低视觉幻觉的关键中间能力。

## 核心回答

- 输入可包含 bbox/point prompt，输出也可生成坐标 token。
- 训练数据来自检测/分割/region-caption/GUI 元素。
- 评测不仅看回答对不对，还看定位 IoU/point accuracy。
- Agent 点击任务本质上高度依赖 grounding。
