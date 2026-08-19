# MASt3R：3D Matching 与 Scalable Alignment

## 面试一句话

MASt3R 在 DUSt3R 的 point-map 几何基础上增加 local feature matching，并改进 metric point maps 和大场景 alignment。

## 为什么需要 matching head

DUSt3R 强于几何恢复，但大规模定位/SfM 仍需要可靠的跨图像对应关系。

## Pipeline 直观理解

```text
image pair
→ geometry-aware backbone
→ metric point maps
+ local descriptors
→ matches
→ sparse/global alignment
→ reconstruction / localization
```

## 面试区别

- DUSt3R：重点是 pairwise 3D point-map prediction；
- MASt3R：进一步强化 matching 和 scalable reconstruction。

## Reference

- https://github.com/naver/mast3r