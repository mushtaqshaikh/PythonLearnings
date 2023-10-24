import yaml

class Configs:
    def __init__(self):
        self.__config_path = './configs.yaml'

    def read_configs(self):
        try:
            with open(self.__config_path) as f:
                configs = yaml.load(f, Loader=yaml.FullLoader)
            return configs
        except FileNotFoundError:
            quit()
