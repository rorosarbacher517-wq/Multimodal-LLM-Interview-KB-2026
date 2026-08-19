# U-Net / DeepLab：经典 Semantic Segmentation

## U-Net
Encoder 降采样提语义，decoder 上采样恢复空间；skip connection 把高分辨率浅层特征直接送给 decoder。

```text
high-res shallow ─────────┐
image → encoder → bottleneck → decoder → mask
                         ↑
                 skip features
```

## DeepLab
核心是 atrous/dilated convolution 和 ASPP，用不同 dilation rate 扩大感受野而不必持续降低分辨率。

## 面试要点
U-Net 强在 encoder-decoder + skip；DeepLab 强在 multi-scale context + atrous convolution。
