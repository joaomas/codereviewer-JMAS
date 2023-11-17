from abc import *


class Validator:
    
    def __init__(self) -> None:
        
        # TODO - swap from list do dict : key = rule_name , value = RuleValidator
        self.rule_validator_dic = {}
    
    @abstractmethod    
    def run_validator(self):
        pass


