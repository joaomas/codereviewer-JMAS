from abc import *


class Validator:
    
    def __init__(self) -> None:
        self.rule_validator_arr = None
    
    @abstractmethod    
    def run_validator(self):
        pass


