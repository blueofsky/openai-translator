from model import OpenAIModel, GLMModel, ZhipuAIModel
from utils import ConfigLoader


class ModelConfig:
    def __init__(self,args):
        config_loader = ConfigLoader(args.config)
        config = config_loader.load_config()
        model_type = args.model_type if args.model_type else config['common']['model_type']
        self.pdf_file_path = args.book if args.book else config['common']['book']
        self.file_format = args.file_format if args.file_format else config['common']['file_format']
        self.language = args.language if args.language else config['common']['language']

        if model_type == "OpenAIModel":
            model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
            api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
            self.model = OpenAIModel(model=model_name, api_key=api_key)
        elif model_type == "ZhipuAIModel":
            model_name = args.zhipuai_model if args.zhipuai_model else config['ZhipuAIModel']['model']
            api_key = args.zhipuai_api_key if args.zhipuai_api_key else config['ZhipuAIModel']['api_key']
            self.model = ZhipuAIModel(model=model_name, api_key=api_key)
        elif model_type == "GLMModel":
            timeout = args.timeout if args.timeout else config['GLMModel']['timeout']
            model_url = args.model_url if args.model_url else config['GLMModel']['model_url']
            self.model = GLMModel(model_url=model_url, timeout=timeout)
        else:
            raise ValueError("Invalid model_type specified. Please choose either 'GLMModel' or 'OpenAIModel' or 'ZhipuAIModel'.")