# OpenAI-Translator v2.0

## 介绍

OpenAI 翻译器是一个使用 AI 技术将英文 PDF 书籍翻译成中文的工具。这个工具使用了大型语言模型 (LLMs)，如 ChatGLM、ZhipuAI和 OpenAI 的 GPT-3 以及 GPT-3.5 Turbo 来进行翻译。它是用 Python 构建的，并且具有灵活、模块化和面向对象的设计。

## 特性

- [X] 使用大型语言模型 (LLMs) 将英文 PDF 书籍翻译成中文。
- [X] 支持 ChatGLM、ZhipuAI 和 OpenAI 模型。
- [X] 通过 YAML 文件或命令行参数灵活配置。
- [X] 对健壮的翻译操作进行超时和错误处理。
- [X] 模块化和面向对象的设计，易于定制和扩展。
- [X] 实现图形用户界面 (GUI) 以便更易于使用。
- [X] 创建一个网络服务或 API，以便在网络应用中使用。
- [X] 添加对其他语言和翻译方向的支持。
- [X] 添加对保留源 PDF 的原始布局和格式的支持。

## 使用说明

### 1. 环境准备
* Ollama环境准备
```bash
# 安装ollama
curl -fsSL https://ollama.com/install.sh | sh

# 配置启动端口，如已经启动了，可执行`systemctl restart ollama.service`重启ollama服务
# export OLLAMA_HOST=0.0.0.0:11434

# 如没有启动ollama，则受到启动ollama server
# ollama serve

# 拉取大模型
ollama pull glm4:9b
```
* Python环境准备
```bash
# 克隆仓库
git clone https://github.com/blueofsky/openai-translator.git
# 安装依赖
cd openai-translator
pip install -r requirements.txt
# 设置环境变量
## 使用ollama本地部署模型时，配置ollama_server地址，默认为http://localhost:11434
export OLLAMA_API_BASE="http://localhost:11434"
## 配置Openai API KEY
export OPENAI_API_KEY="sk-xxx"
```

### 2. 运行
```bash
# 执行翻译命令
python ai_translator/main.py cmd --help
# 运行API服务
python ai_translator/main.py apiserver --help
# 运行Gradio服务
python ai_translator/main.py gradio --help
```

### 3. 使用示例

您可以通过提供不同的命令行参数来使用 OpenAI-翻译器。

#### 1）使用命令行参数

- 使用Openai模型
```bash
python ai_translator/main.py cmd 
```

- 使用本地部署模型: glm4:9b
```bash
python ai_translator/main.py cmd  --model_type ollama --model_name glm4:9b
```

#### 2）使用图形界面

- 使用Openai模型
```bash
python ai_translator/main.py gradio
```

- 使用本地部署模型: glm4:9b
```bash
python ai_translator/main.py gradio --model_type ollama --model_name glm4:9b
```

- 访问地址：http://127.0.0.1:7860/

#### 3）使用API接口

- 使用Openai模型
```bash
python ai_translator/main.py apiserver
```

- 使用本地部署模型: glm4:9b
```bash
python ai_translator/main.py apiserver --model_type ollama --model_name glm4:9b
```

- Swagger地址: http://127.0.0.1:8000/docs

## 许可证

该项目采用 GPL-3.0 许可证。有关详细信息，请查看 [LICENSE](LICENSE) 文件。




