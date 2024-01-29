import sys
import os

# TODO remove this. From terminal works exporting PYTHONPATH=/home/usuario/repo/codereviewer , but not from Vscode yet!!!

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Validator import Validator
from src.ValidatorConstructor_XML import ValidatorConstructor_XML

class CodeReviewer:
    """_summary_
    This is the main class for executing code review
    
    The other main classes of the project are:
    - Parser - Super class for parsing Fortran code, extended to XMLParser or others to be implemented
    - Validator - The super class Validator, extended to XMLValidator or others to be implemented
    - RuleValidator - The super class for rule validator, extended to RulesValidatorXML, which extends to all XML based rules
    
    """
    
    def __init__(self) -> None:
        self.validator_constructor_xml = ValidatorConstructor_XML()
        self.validator_xml = self.validator_constructor_xml.construct()

    def run_validator(self, file_f90):
        
        str_errors = self.validator_xml.run_validator(file_f90)
        if len(str_errors) > 0:
            print(f'Errors found:\n{str_errors}' )
        


                

def main() -> int:
    # TODO file_f90 via line command parameter
    file_f90 = './tests/dummy.F90' 
    cr = CodeReviewer()
    return cr.run_validator(file_f90)
    

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
        
        
        


