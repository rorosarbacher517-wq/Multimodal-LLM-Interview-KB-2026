# 单目深度为什么是病态问题

## 面试一句话

一张 RGB 图像可以由多种不同三维场景投影得到，所以绝对尺度无法仅靠几何唯一确定。

## 模型依赖哪些线索

- perspective；
- object size prior；
- texture gradient；
- occlusion；
- semantic prior；
- training-data scale statistics。

## Scale Ambiguity

同样的二维图像可以解释为“小物体近距离”或“大物体远距离”。

## 怎么获得 metric depth

- metric depth supervision；
- known camera intrinsics；
- stereo / multi-view；
- sparse LiDAR prompt；
- known object/scene scale prior。

## 面试结论

单目深度网络学到的不只是几何，也包含大量数据分布先验。