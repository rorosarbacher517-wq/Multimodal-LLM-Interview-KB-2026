# 表格、公式、图表为什么不能只做普通 OCR

## 面试一句话

这些元素不仅有“字符”，还有强结构：表格需要 row/column/cell，公式需要二维符号关系，图表需要轴、图例和数据映射。

## 表格

目标通常是：

`image → cell structure + text → HTML/Markdown`

难点：merged cells、跨页表、无线表、复杂表头。

## 公式

目标常是：

`formula crop → LaTeX`

难点：上下标、分式、矩阵、嵌套结构。

## 图表

需要同时理解：OCR + visual marks + axes + legend + numerical relation。

## 面试结论

**Document parsing = OCR + structure understanding**，不能只用 character accuracy 衡量。