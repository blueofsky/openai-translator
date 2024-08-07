# Chatglm3-6b 模型部署

### 1. 安装依赖
```bash
pip install -r requirements.txt
```
### 2. 执行命令
```bash
# 配置本地模型路径
export MODEL_PATH=/opt/modules/chatglm3-6b
python api_server.py
```

- 访问地址：http://127.0.0.1:8000/

- 接口文档地址: http://127.0.0.1:8000/docs

### 3. 测试

```python
from openai import OpenAI
client = OpenAI(base_url='http://localhost:8000/v1',api_key='XXX')

messages=[
    {
        "role": "user", 
        "content": "你好!"
    }
]

data = client.chat.completions.create(
  model="chatglm3-6b",
  messages = messages
)
```
