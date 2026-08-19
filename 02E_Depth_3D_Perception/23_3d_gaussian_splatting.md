# 3D Gaussian Splatting (3DGS) 是什么？

3DGS 用大量可优化 3D Gaussian primitives 表示场景，每个 Gaussian 包含位置、尺度、旋转、不透明度和颜色/SH 特征。

渲染时把 3D Gaussian 投影到屏幕并做 differentiable splatting。

相比经典 NeRF，3DGS 的重要优势是训练/渲染效率高，适合实时新视角渲染；但内存、动态场景和几何精度仍需具体方法处理。
