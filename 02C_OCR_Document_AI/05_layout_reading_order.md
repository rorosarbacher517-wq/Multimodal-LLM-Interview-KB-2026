# Layout Analysis 与 Reading Order

## 面试一句话

文档理解的关键不只是识别文字，而是知道每一块“是什么”和“应该按什么顺序读”。

## Layout 常见类别

- title / heading
- paragraph
- list
- table
- figure
- formula
- caption
- header / footer / page number

## Pipeline

```text
Page image
→ layout detector
→ regions + classes + coordinates
→ OCR / table / formula recognizer
→ reading-order sorting
→ structured output
```

## Reading order 为什么难

多栏排版、浮动图表、脚注、跨页表格会让简单的 `top-to-bottom` 排序失败。

## 工程建议

输出中保留：`page_id + bbox + block_type + reading_order + parent/child hierarchy`，不要只留下纯文本。