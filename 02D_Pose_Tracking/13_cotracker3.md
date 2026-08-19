# CoTracker3：Track Any Point

## 面试一句话

CoTracker3 是 transformer-based point tracker：它联合跟踪多个点，而不是每个点独立做 optical flow。

## 输入输出

```text
video [B,T,3,H,W]
+ query/grid points [B,N,3]  # time,x,y
→ tracks [B,T,N,2]
→ visibility [B,T,N,1]
```

## 为什么联合跟踪

不同点的运动具有共享场景结构。联合建模能利用对象刚性、相机运动和局部一致性。

## CoTracker3 训练特点

官方强调利用 pseudo-labelled real videos，降低只靠 synthetic tracking data 的 domain gap。

## Reference

- https://github.com/facebookresearch/co-tracker