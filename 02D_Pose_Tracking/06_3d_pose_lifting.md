# 2D → 3D Pose Lifting 与 MotionBERT

## 面试一句话

3D pose lifting 把 2D 关键点序列映射到 3D 关节位置；视频方法利用时间信息减少单帧深度歧义。

## Pipeline

```text
video
→ 2D detector / pose estimator
→ 2D joints [T,K,2]
→ temporal encoder
→ 3D joints [T,K,3]
```

## 为什么需要时间

单张图像中前后深度不唯一，连续动作的速度、骨骼长度和运动轨迹提供额外约束。

## MotionBERT 思路

把人体运动序列当作时空 token 做自监督/预训练，再用于 3D pose 等下游任务。

## 面试注意

2D detector 的误差会传给 3D lifting，因此要区分前端 perception error 和 3D model error。