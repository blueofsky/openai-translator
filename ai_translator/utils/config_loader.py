import yaml

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path

    def load_config(self):
        with open(self.config_path, "r",encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config