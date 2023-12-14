from abc import *

class ValidatorConstructor:
    """_summary_
    Abstract Constructor class for Validators and RuleValidators
    """
    
    def __init__(self) -> None:
        pass
    
    
    @abstractmethod
    def construct(self):
        pass
