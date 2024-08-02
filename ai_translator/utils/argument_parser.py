import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='A translation tool that supports translations in any language pair.')
        
        subparsers = self.parser.add_subparsers(dest='command',help='sub command: cmd,apiserver,gradio')

        cmd_parsers = subparsers.add_parser('cmd', help='Command for translation.')
        cmd_parsers.add_argument('--config_file', type=str, default='./config.yaml', help='Configuration file with model and API settings.')
        cmd_parsers.add_argument('--model_type', type=str,choices=['openai', 'ollama'], default='openai', help='model type,default openai.')
        cmd_parsers.add_argument('--model_name', type=str, default='gpt-3.5-turbo',help='Name of the Large Language Model')
        cmd_parsers.add_argument('--input_file', type=str, help='PDF file to translate.')
        cmd_parsers.add_argument('--source_language', type=str, help='The language of the original book to be translated.')
        cmd_parsers.add_argument('--target_language', type=str, help='The target language for translating the original book.')
        cmd_parsers.add_argument('--target_file_format', type=str, help='The file format of translated book. Now supporting PDF and Markdown')
       
        api_server_parsers = subparsers.add_parser('apiserver', help='API server for translation.')
        api_server_parsers.add_argument('--config_file', type=str, default='./config.yaml', help='Configuration file with model and API settings.')
        api_server_parsers.add_argument('--model_type', type=str,choices=['openai', 'ollama'], default='openai', help='model type,default openai.')
        api_server_parsers.add_argument('--model_name', type=str, default='gpt-3.5-turbo', help='model name')
        
        gradio_server_parsers = subparsers.add_parser('gradio', help='Grado server for translation.')
        gradio_server_parsers.add_argument('--config_file', type=str, default='./config.yaml', help='Configuration file with model and API settings.')      
        gradio_server_parsers.add_argument('--model_type', type=str,choices=['openai', 'ollama'], default='openai', help='model type,default openai.')
        gradio_server_parsers.add_argument('--model_name', type=str, default='gpt-3.5-turbo', help='model name')

    def parse_arguments(self):
        args = self.parser.parse_args()
        if args.command is None:
            self.parser.print_help()
        return args.command,args