from src.utils.common import read_yaml
from src.configuration import PARAMS_FILE_PATH


class ParametersManager:
    def __init__(self, params_file_path=PARAMS_FILE_PATH):
        self.params=read_yaml(params_file_path)

        
    def get_params(self) ->  dict:
        return self.params
