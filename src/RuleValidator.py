from abc import *
class RuleValidator:
    """_summary_
    The super class for rule validator
    """    
    def __init__(self, description_in) -> None:
        self.description = description_in
        # TODO - implement points for each rule ?
        self.points = 0
    
    @abstractmethod
    def check() -> str:
        pass




        