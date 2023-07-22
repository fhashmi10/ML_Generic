from src.utils.common import read_yaml_dict
from src.configuration import PARAMS_FILE_PATH
from ensure import EnsureError

from src import logger


class ParametersManager:
    def __init__(self, params_file_path=PARAMS_FILE_PATH):
        self.params={}
        try:
            self.params=read_yaml_dict(params_file_path)
        except EnsureError as ex:
            logger.exception("Problem reading parameters yaml file: %s", ex)

        
    def get_params(self) ->  dict:
        return self.params
