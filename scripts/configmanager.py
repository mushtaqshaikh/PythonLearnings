import yaml
import os 

class Configs:
    def __init__(self):
        # self.__config_path = './config.yaml'
        self.__config_path = 'scripts/config.yaml'
        
    def read_configs(self):
        try:
            print(os.getcwd())
            with open(self.__config_path) as f:
                configs = yaml.load(f, Loader=yaml.FullLoader)
            return configs
        except FileNotFoundError:
            quit()
