# 02_Function_Call怎么训练

## 面试一句话

Function call 本质是让模型学习一个受 schema 约束的结构化输出分布。

## 核心回答

- 输入包含工具名、参数 schema 和用户请求。
- SFT 数据给出正确 tool call。
- 执行后把 tool result 回填，再训练模型继续回答。
- Agent 能力还需要 multi-step trajectory，而不是只做单次 function call。
