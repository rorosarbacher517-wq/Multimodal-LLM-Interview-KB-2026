# RTMPose / RTMO / RTMW：实时姿态估计

## 面试一句话

RTMPose 系列面向实际部署，在准确率、模型规模、推理速度之间做平衡；MMPose 还提供 RTMO、RTMW 等多人/whole-body 路线。

## RTMPose

常见 top-down pipeline：

```text
detector → person crop → lightweight backbone → SimCC head → keypoints
```

## RTMO

更偏 one-stage multi-person pose，不需要为每个人单独 crop。

## RTMW

面向 whole-body keypoints，可覆盖 body/hand/face 等更完整关键点集合。

## Reference

- MMPose: https://github.com/open-mmlab/mmpose
- RTMPose: https://arxiv.org/abs/2303.07399