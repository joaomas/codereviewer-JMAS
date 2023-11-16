from abc import *
class RuleValidator:
    """_summary_
    The super class for rule validator
    """    
    def __init__(self, description_in) -> None:
        self.description = description_in
    
    @abstractmethod
    def check():
        pass




        