# Top-down / Bottom-up / One-stage Pose

## 面试一句话

Top-down 先检测人再对每个人做 pose；bottom-up 先找全图关键点再组装成人；one-stage 直接联合预测实例和关键点。

## Top-down

```text
image → person detector → N crops → pose estimator → N poses
```

优点：精度高。缺点：人越多计算越多，依赖 detector。

## Bottom-up

```text
image → all keypoints + association → person instances
```

计算更接近固定，但多人关键点 grouping 更难。

## One-stage

直接输出 instance + keypoints，适合实时场景，例如部分 YOLO-Pose / RTMO 路线。