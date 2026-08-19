# 2D Pose、3D Pose、Mesh Recovery 区别

## 面试一句话

2D Pose 输出图像平面关键点；3D Pose 输出三维关节点；Mesh Recovery 进一步恢复人体表面网格和姿态/形状参数。

## 输出形式

- 2D keypoints：`[K,2] + confidence`
- 3D joints：`[K,3]`
- Mesh：`vertices [V,3]`，常再输出 SMPL 等参数。

## 典型任务

human body、hand、face、whole-body、animal pose。

## 易错点

“3D pose”不一定意味着直接从 3D 传感器输入；很多方法是单目图像或 2D keypoints → 3D lifting。