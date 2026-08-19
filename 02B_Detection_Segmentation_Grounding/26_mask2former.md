# Mask2Former 的核心思想

Mask2Former 用统一的 masked-attention Transformer framework 处理 semantic、instance、panoptic segmentation。

核心是让 object queries 只关注当前预测 mask 对应区域，而不是每层都全图 cross-attention。

```text
multi-scale features
→ pixel decoder
→ transformer queries
→ class + mask
```

## 面试意义
它体现了 segmentation 从“逐像素分类 head”走向“query/set prediction + mask classification”的路线。
