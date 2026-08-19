# Agent System Design Cases

> Agent 系统设计统一按：**Goal/SLO → Environment → Observation/Action → Agent Loop → Tools → State/Memory → Verifier → Safety → Retry/Checkpoint → Evaluation/Cost**。

---

## Case 1. 设计一个企业 Research Agent

### 需求
用户给出研究问题，系统自动搜索、阅读、整理证据并生成带引用报告。

### 架构

```text
User Query
   ↓
Planner
   ↓
Query Decomposition
   ↓
Search / RAG / Web Tools
   ↓
Evidence Store
   ↓
Source Quality + Dedup
   ↓
Synthesis
   ↓
Citation Verifier
   ↓
Report
```

### 关键设计
- 每条 claim 绑定 source id；
- 去重同源转载；
- 对冲突证据显式保留；
- 低质量来源降权；
- stop condition：证据充分 / budget exhausted。

### 指标
- factuality；
- citation precision；
- source coverage；
- latency；
- cost。

---

## Case 2. 设计一个 Coding Agent

### Pipeline

```text
Task
→ repository inspect
→ plan
→ read relevant files
→ edit patch
→ run test
→ inspect failure
→ repair
→ final test
→ diff verifier
```

### 必须有
- sandbox；
- filesystem/shell tools；
- git diff；
- unit/integration tests；
- timeout；
- checkpoint；
- secret isolation。

### 失败处理

```text
test fail
→ classify compile/runtime/logic/environment
→ inspect logs
→ patch
→ rerun only relevant tests
```

### 指标
- task success；
- tests passed；
- unnecessary diff；
- tool calls；
- token/cost；
- unsafe shell actions。

---

## Case 3. 设计一个 GUI / Computer-Use Agent

```text
Screenshot + Accessibility Tree
        ↓
Perception / Grounding
        ↓
Planner
        ↓
click / type / scroll / key
        ↓
New Screenshot
        ↓
Verifier
        ↓
continue / replan / stop
```

### 难点
- resolution/coordinate mapping；
- hidden/dynamic state；
- pop-up / loading / stale UI；
- irreversible actions。

### Safety
支付、删除、发送、授权等动作前 human confirmation。

---

## Case 4. 设计一个企业 Multi-Agent Workflow

角色：

```text
Manager
├─ Research Agent
├─ Data Agent
├─ Coding Agent
└─ Verification Agent
```

### 核心问题
1. 谁拥有 global state？
2. worker 如何拿到最小必要上下文？
3. handoff 如何追踪？
4. 如何防止重复工作？
5. remote agent 如何发现能力？

### 通信
- tool call：本地功能；
- MCP：工具/资源连接；
- A2A：远程 agent interoperability。

### 生产要求
- shared state versioning；
- task id；
- trace；
- max delegation depth；
- loop detection。

---

## Case 5. 设计一个 Long-Horizon Agent Runtime

任务可能运行数小时。

```text
Request
→ Harness
→ Checkpointed State
→ Sandbox Pool
→ Tool Calls
→ Artifact Store
→ Verifier
→ Checkpoint
→ Resume / Continue
```

### State 需要持久化
- goal；
- completed subgoals；
- pending tasks；
- tool results references；
- artifacts；
- approvals；
- budget；
- environment snapshot id。

### 为什么 Harness 与 Sandbox 分离？
让 credential、policy、trace、state 留在受控层，模型生成代码只在隔离 compute 执行。

### Failure Recovery
sandbox crash → provision new sandbox → restore snapshot/artifacts → resume。

---

## Case 6. 设计一个 Agent 数据生产平台

```text
Task Generator
     ↓
Environment Factory
     ↓
Rollout Workers
     ↓
Trajectory Store
     ↓
Executable Verifier
     ↓
Quality / Safety / Dedup
     ↓
Capability Buckets
     ↓
SFT / Preference / RL
     ↓
Evaluation
     ↓
Failure Mining
     └────────→ New Tasks
```

### 关键能力
- environment reproducibility；
- schema/version；
- trajectory lineage；
- synthetic + human data；
- failure/recovery trajectory；
- contamination control。

---

## Case 7. 设计一个低成本客服 Agent

优先 workflow 化：

```text
Intent Router
→ FAQ/RAG
→ deterministic policy
→ tool call if needed
→ escalation if uncertain
```

### 不应让 Agent 自由决定的动作
-退款金额超阈值；
- 修改关键账户信息；
- 高风险权限操作。

### Cost Optimization
- cheap classifier/router；
- cache common answers；
- small model for easy cases；
- strong model only for complex cases；
- max tool/step budget。

---

## Case 8. 设计一个安全的 Agent Tool Gateway

```text
Agent
→ Tool Request
→ Policy Gateway
   ├─ authn/authz
   ├─ schema validate
   ├─ rate limit
   ├─ risk classification
   ├─ confirmation
   └─ audit
→ Tool
```

### 为什么需要 Gateway？
不能让 LLM 直接拿 production credential 调任意 API。

### Least Privilege
每个 tool/session 只发最小 scope token。

---

## Case 9. Agent 系统怎么做 Observability？

Trace hierarchy：

```text
run_id
  ├─ model_call
  ├─ tool_call
  │   ├─ latency
  │   └─ error
  ├─ state_update
  ├─ handoff
  └─ verifier
```

必须记录版本：model、prompt、tool schema、policy、environment。

---

## Case 10. Agent System Design 面试最后主动讲什么？
主动补 trade-off：
- autonomy vs determinism；
- accuracy vs tool cost；
- memory vs context size；
- planning depth vs latency；
- multi-agent specialization vs communication cost；
- retry vs duplicate side effects；
- sandbox isolation vs execution speed；
- automation vs human confirmation。

真正成熟的答案不是组件最多，而是**知道哪里应该让模型决策，哪里必须由系统控制。**
