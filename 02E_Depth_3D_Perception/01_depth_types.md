# Relative Depth、Metric Depth、Disparity 区别

## 面试一句话

Relative depth 只保证远近排序和相对比例；metric depth 要输出真实物理尺度；disparity 是双目中左右匹配点的像素位移。

## 三种输出

- Relative depth：尺度/平移可能不唯一。
- Metric depth：单位通常是 meter。
- Disparity：`d = x_left - x_right`。

双目中有：

`Z = f * B / d`

其中 `f` 是焦距，`B` 是双目 baseline。

## 易错点

单目模型输出“看起来像深度”的连续图，不代表一定是 metric depth。