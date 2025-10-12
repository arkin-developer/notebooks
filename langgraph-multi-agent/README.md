# 🤖 LangGraph 多 Agent 系统实战

## 📖 项目简介

本项目展示如何使用 LangGraph 框架构建复杂的多 Agent 协作系统。通过实战案例学习 Agent 编排、状态管理、条件路由等核心技能。

## 🎯 学习目标

- ✅ 掌握 LangGraph 核心概念（State、Node、Edge、Graph）
- ✅ 学会构建状态机工作流
- ✅ 实现多 Agent 协作模式
- ✅ 掌握条件路由和动态决策
- ✅ 了解实际应用场景和最佳实践

## 🛠️ 技术栈

- **框架**: LangGraph + LangChain
- **LLM**: DeepSeek API（兼容 OpenAI）
- **Python**: 3.11+
- **依赖**: langgraph, langchain, langchain-openai

## 📚 项目结构

```
langgraph-multi-agent/
├── langgraph-multi-agent.ipynb    # 主 Notebook
├── README.md                       # 项目说明
└── scripts/                        # 调试脚本（可选）
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install langgraph langchain langchain-openai sentence-transformers
```

### 2. 配置 API Key

在 Notebook 中替换你的 DeepSeek API Key：

```python
os.environ["OPENAI_API_KEY"] = "your-deepseek-api-key-here"
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"
```

### 3. 运行 Notebook

打开 `langgraph-multi-agent.ipynb` 并按顺序执行各个 cell。

## 📋 内容概览

### 一、LangGraph 基础概念

- State 状态管理
- Node 节点定义
- Edge 边和路由
- Graph 工作流编排
- 简单示例演示

### 二、实战案例：智能内容创作团队

**系统架构**：
```
用户需求 → 研究员 Agent → 作家 Agent → 编辑 Agent → 最终内容
```

**Agent 角色**：
- 📚 **研究员 Agent**：收集信息和资料
- ✍️ **作家 Agent**：撰写结构化内容
- 🔍 **编辑 Agent**：审核和改进文章
- 🎯 **质检 Agent**：评估内容质量

**核心功能**：
- 状态在 Agent 间传递
- 条件路由（根据质量决定是否重做）
- 循环迭代改进
- 完整的工作流管理

### 三、高级特性

- 动态路由机制
- 质量检查循环
- 智能决策分支
- 状态持久化

### 四、可视化工作流

- ASCII 流程图
- 工作流结构展示
- 决策节点说明

### 五、更多实用案例

**5.1 客服团队 Agent**
- 问题分类 Agent
- 技术支持 Agent
- 账单处理 Agent
- 智能路由到专家

**5.2 代码审查团队**
- 安全审查 Agent
- 性能审查 Agent
- 风格审查 Agent
- 并行处理机制

## 🎨 应用场景

### 1. 内容创作系统
- 自动化文章生成
- 多轮质量改进
- 协作式写作

### 2. 客户服务系统
- 智能问题分类
- 专家路由
- 自动化响应

### 3. 代码审查流程
- 多维度代码检查
- 并行审查
- 自动化建议

### 4. 数据分析管道
- 数据收集 → 清洗 → 分析 → 报告
- 多阶段处理
- 错误重试机制

### 5. 智能助手系统
- 任务分解
- 专业化处理
- 结果整合

## 💡 最佳实践

### 1. 状态设计
- 定义清晰的状态结构
- 使用 TypedDict 类型提示
- 考虑状态的演化过程

### 2. Agent 设计
- 单一职责原则
- 明确的输入输出
- 可测试性

### 3. 路由策略
- 清晰的决策逻辑
- 避免死循环
- 设置最大迭代次数

### 4. 错误处理
- 异常捕获
- 回退机制
- 日志记录

### 5. 性能优化
- 并行处理独立任务
- 缓存重复计算
- 流式输出

## 🔍 关键代码示例

### 定义状态

```python
class AgentState(TypedDict):
    topic: str
    research_notes: str
    draft_content: str
    final_content: str
    messages: Annotated[List, operator.add]
    next_agent: str
    iteration: int
```

### 创建 Agent

```python
def researcher_agent(state: AgentState) -> AgentState:
    # Agent 逻辑
    result = llm.invoke(prompt)
    return {
        **state,
        "research_notes": result.content,
        "next_agent": "writer"
    }
```

### 构建工作流

```python
workflow = StateGraph(AgentState)
workflow.add_node("researcher", researcher_agent)
workflow.add_node("writer", writer_agent)
workflow.add_conditional_edges("researcher", route_agent)
app = workflow.compile()
```

### 运行工作流

```python
result = app.invoke(initial_state)
```

## 📊 工作流可视化

```
    ┌─────────────┐
    │   开始      │
    └──────┬──────┘
           ↓
    ┌─────────────┐
    │  研究员      │ ← 收集信息
    └──────┬──────┘
           ↓
    ┌─────────────┐
    │   作家       │ ← 撰写内容
    └──────┬──────┘
           ↓
    ┌─────────────┐
    │   编辑       │ ← 审核改进
    └──────┬──────┘
           ↓
    ┌─────────────┐
    │  质量检查    │ ← 评估质量
    └──────┬──────┘
           ↓
      [分数>=8?]
       ↙     ↘
     是       否
     ↓         ↓
   结束    返回作家
```

## 🔧 DeepSeek 配置说明

### 为什么选择 DeepSeek？

- 💰 **价格优势**：比 OpenAI 便宜约 90%
- 🇨🇳 **中文友好**：对中文理解能力强
- 🔌 **API 兼容**：完全兼容 OpenAI API 格式
- 🚀 **性能优秀**：接近 GPT-3.5 水平

### 配置方式

```python
os.environ["OPENAI_API_KEY"] = "your-deepseek-api-key"
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"

llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_base="https://api.deepseek.com"
)
```

### 获取 API Key

1. 访问 [DeepSeek Platform](https://platform.deepseek.com/)
2. 注册/登录账号
3. 创建 API Key
4. 替换 Notebook 中的占位符

## 📈 进阶学习

### LangGraph 高级特性

1. **Checkpointing**：保存和恢复工作流状态
2. **Streaming**：流式输出中间结果
3. **Subgraphs**：嵌套工作流
4. **Parallel Execution**：并行执行节点
5. **Human-in-the-loop**：人机协作

### 扩展方向

- 集成更多工具（搜索、数据库等）
- 实现更复杂的决策逻辑
- 添加监控和可观测性
- 优化性能和并发
- 部署为 Web 服务

## 📖 参考资源

### 官方文档

- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [LangChain 文档](https://python.langchain.com/)
- [DeepSeek API 文档](https://platform.deepseek.com/docs)

### 学习资料

- LangGraph 教程
- Multi-Agent 系统设计模式
- Agent 协作最佳实践

## 🤝 贡献

欢迎提出问题和建议！

## 📄 许可证

MIT License

---

**🎉 开始你的多 Agent 系统之旅吧！**

