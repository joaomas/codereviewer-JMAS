from abc import *


class Validator:
    
    def __init__(self) -> None:
        
        self.rule_validator_dic = {}
    
    @abstractmethod    
    def run_validator(self):
        pass


