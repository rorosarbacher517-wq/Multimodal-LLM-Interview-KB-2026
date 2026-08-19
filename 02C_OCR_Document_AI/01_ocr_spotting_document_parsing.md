# OCR、Text Spotting、Document Parsing 有什么区别

## 面试一句话

**OCR** 解决“图里有什么文字”；**text spotting** 同时解决“文字在哪里 + 是什么”；**document parsing** 还要恢复版面、表格、公式、图片、标题层级和阅读顺序。

## 核心回答

- OCR recognition：输入文字 crop，输出字符序列。
- Text detection：输入整图，输出文本框/多边形。
- Text spotting：detection + recognition 联合输出。
- Document layout analysis：识别 title、paragraph、table、figure、formula 等区域。
- Document parsing：把这些元素按 reading order 组织成 Markdown/HTML/JSON。

## 面试追问

**为什么 Document AI 比普通 OCR 难？**

因为“识别对字”还不够。多栏排版、跨页表格、公式、图表、脚注和扫描畸变都会影响结构恢复。

## 易错点

不要把“VLM 能读字”直接等同于“完整文档解析”。工程系统通常还需要 layout、裁剪、顺序恢复和结构化后处理。