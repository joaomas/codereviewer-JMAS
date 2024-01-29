from abc import *

class RuleValidator:
    """_summary_
    The super class for rule validator
    """    
    
    def __init__(self, description_in, code, points, mandatory=True) -> None:
        self.description = description_in
        self.code = code
        self.mandatory = mandatory
        self.points = points
    
    @abstractmethod
    def check() -> str:
        pass




        