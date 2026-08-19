# DUSt3R：为什么可以弱化传统 SfM Pipeline

## 面试一句话

DUSt3R 不先显式做 feature matching + calibrated geometry，而是让网络直接从图像对预测两张图在共同坐标中的 3D point maps。

## 输入输出

```text
image1 + image2
→ shared/paired vision transformer
→ point map 1 [H,W,3]
→ point map 2 [H,W,3]
→ confidence
```

## 为什么重要

传统 SfM 依赖：keypoints、matching、camera calibration、triangulation。DUSt3R 把很多步骤吸收到 learned prediction 里。

## 多视图

多个 pair 的 point maps 还需要 global alignment 才形成一致场景。

## Reference

- https://github.com/naver/dust3r