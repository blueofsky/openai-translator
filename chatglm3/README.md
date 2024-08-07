# Chatglm3-6b 模型部署

### 1. 安装依赖
```bash
pip install -r requirements.txt
```
### 2. 修改配置

```python
# 修改 api_server.py 的line:54 代码，把'THUDM/chatglm3-6b'为你自己的模型路径:
MODEL_PATH = os.environ.get('MODEL_PATH', 'THUDM/chatglm3-6b')
```

### 3. 运行
```bash
python api_server.py
```

- 访问地址：http://127.0.0.1:8000/

- 接口文档地址: http://127.0.0.1:8000/docs

### 4. 测试

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
