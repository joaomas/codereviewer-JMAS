
from abc import *
from src.RuleValidator import RuleValidator


class RuleValidator_XML(RuleValidator):
    """_summary_
    Class for validating XML structure parsed from Fortran code
    """
    
    def __init__(self, description_in) -> None:
        super().__init__(description_in)
        
    @abstractmethod
    def run():
        pass
        

# all rules

class RuleValidator_XML_1(RuleValidator_XML):
    
    def __init__(self) -> None:
        super().__init__('Implicit None')
    
    def check():
        # xml from self.xml_validator.xml
        
        ret = True
        
        # check rule
        # if not rule_ok:
          #ret = False
          
        return ret  

# other rules ...