import sys
from Validator import Validator
from ValidatorConstructor_XML import ValidatorConstructor_XML

class CodeReviewer:
    """_summary_
    This is the main class for executing code review
    
    The other main classes of the project are:
    - Parser - Super class for parsing Fortran code, extended to XMLParser or others to be implemented
    - Validator - The super class Validator, extended to XMLValidator or others to be implemented
    - RulesValidator - The super class for rule validator, extended to RulesValidatorXML, which extends to all XML based rules
    
    """
    
    def __init__(self) -> None:
        pass
        
    def run_validator(self):
        
        validator_constructor_xml = ValidatorConstructor_XML()
        validator_xml = validator_constructor_xml.construct()
        validator_xml.run_validator()
                

def main() -> int:
    cr = CodeReviewer()
    return cr.run_validator()
    

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
        
        
        


