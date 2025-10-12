# 🤖 LangGraph 多 Agent 系统实战

本项目展示如何使用 LangGraph 构建复杂的多 Agent 协作系统，并使用 LangSmith 进行监控和调试。

## 📋 环境配置

### 配置方案

本项目采用**混合配置**方式：
- **全局环境变量**：`LANGCHAIN_API_KEY` (LangSmith API Key)
- **项目环境变量**：其他配置项（TRACING、PROJECT、DeepSeek）

### 快速开始

#### 方法 1：使用 Shell 脚本（推荐）

1. **编辑配置脚本**：
   ```bash
   nano setup_env.sh
   # 修改 OPENAI_API_KEY 为你的 DeepSeek API Key
   ```

2. **加载环境变量**：
   ```bash
   cd /Users/arkin/Desktop/Dev/notebooks/langgraph-multi-agent
   source setup_env.sh
   ```

3. **启动 Jupyter**：
   ```bash
   jupyter notebook
   # 或
   jupyter lab
   ```

#### 方法 2：使用 Python 配置

1. **编辑 config.py**：
   ```python
   # 在 config.py 中找到这一行，填入你的 API Key
   if not os.environ.get('OPENAI_API_KEY'):
       os.environ['OPENAI_API_KEY'] = 'your_deepseek_api_key_here'
   ```

2. **直接运行 Notebook**（会自动加载配置）

### 验证配置

运行诊断脚本检查配置是否正确：

```bash
cd /Users/arkin/Desktop/Dev/notebooks/langgraph-multi-agent
python config.py
```

或运行详细测试：

```bash
python test_langsmith_detailed.py
```

## 🔑 获取 API Keys

### LangSmith API Key（全局配置）

1. 访问 [https://smith.langchain.com/](https://smith.langchain.com/)
2. 注册/登录账号
3. 点击右上角头像 → Settings → API Keys
4. 创建 API Key（格式：`lsv2_pt_xxxxx`）
5. 在全局配置：
   ```bash
   # 编辑 ~/.zshrc 或 ~/.bashrc
   export LANGCHAIN_API_KEY='lsv2_pt_your_key'
   
   # 重新加载
   source ~/.zshrc
   ```

### DeepSeek API Key（项目配置）

1. 访问 [https://platform.deepseek.com/](https://platform.deepseek.com/)
2. 注册/登录账号
3. 创建 API Key
4. 在 `setup_env.sh` 或 `config.py` 中配置

## 📁 项目结构

```
langgraph-multi-agent/
├── langgraph-multi-agent.ipynb   # 主要的演示 Notebook
├── config.py                      # Python 配置管理
├── setup_env.sh                   # Shell 环境变量脚本
├── check_langsmith.py             # LangSmith 配置检查
├── test_langsmith_detailed.py     # 详细测试脚本
└── README.md                      # 本文件
```

## 🚀 使用方法

### 1. 启动项目

```bash
# 进入项目目录
cd /Users/arkin/Desktop/Dev/notebooks/langgraph-multi-agent

# 加载环境变量
source setup_env.sh

# 启动 Jupyter
jupyter notebook
```

### 2. 运行 Notebook

打开 `langgraph-multi-agent.ipynb`，按顺序运行单元格。

### 3. 查看 LangSmith 监控

- 访问 [https://smith.langchain.com/](https://smith.langchain.com/)
- 在左侧找到项目：`langgraph-multi-agent`
- 查看实时执行详情、性能分析、成本统计

## 🔍 故障排查

### 问题 1：LangSmith 看不到数据

**检查**：
```bash
python check_langsmith.py
```

**常见原因**：
- 环境变量未设置或未生效
- Jupyter Kernel 未重启
- API Key 不正确

**解决**：
1. 确认环境变量已正确设置
2. 重启 Jupyter Kernel
3. 刷新 LangSmith 网页

### 问题 2：环境变量不生效

**原因**：环境变量只在当前 shell 会话有效

**解决**：
```bash
# 确保在同一个终端中：
# 1. 设置环境变量
source setup_env.sh

# 2. 启动 Jupyter
jupyter notebook
```

### 问题 3：API Key 错误

**检查配置**：
```bash
echo "LANGCHAIN_API_KEY: ${LANGCHAIN_API_KEY:0:20}..."
echo "OPENAI_API_KEY: ${OPENAI_API_KEY:0:20}..."
```

## 📚 学习目标

通过本项目，你将学会：

- ✅ LangGraph 基础概念（State、Node、Edge、Graph）
- ✅ 构建多 Agent 协作系统
- ✅ 实现条件路由和动态决策
- ✅ 使用 LangSmith 监控和调试
- ✅ 实战案例：智能内容创作团队

## 🎯 实战案例

### 1. 基础示例
简单的两步工作流，理解 LangGraph 基本概念。

### 2. 内容创作团队
研究员 → 作家 → 编辑的协作流程，展示多 Agent 串行协作。

### 3. 质量循环
带质量检查的循环改进机制，展示条件路由和迭代优化。

## 💡 最佳实践

1. **清晰的状态设计**：定义完整的状态结构
2. **单一职责**：每个 Agent 专注一个任务
3. **使用 LangSmith**：监控所有执行细节
4. **错误处理**：考虑异常情况和回退机制
5. **性能优化**：通过 LangSmith 分析瓶颈

## 📖 参考资源

- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [LangSmith 文档](https://docs.smith.langchain.com/)
- [DeepSeek API 文档](https://platform.deepseek.com/api-docs/)

---

**🎉 祝学习愉快！有问题随时查看故障排查部分或运行诊断脚本。**
