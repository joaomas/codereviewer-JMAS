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
    - Parser        : Super class for parsing Fortran code, extended to XMLParser or others to be implemented
    - Validator     : The super class Validator, extended to XMLValidator or others to be implemented
    - RuleValidator : The super class for rule validator, extended to RulesValidatorXML, which extends to all XML based rules

    """

    def __init__(self) -> None:
        self.validator_constructor_xml = ValidatorConstructor_XML()
        self.validator_xml             = self.validator_constructor_xml.construct()

    def execute_validation(self, file_f90):

        str_errors = self.validator_xml.run_validator(file_f90)
        if len(str_errors) > 0:
            print(f'Errors found: \n{str_errors}')
            #print("--")
        return str_errors


def main() -> int:


    cr = CodeReviewer()

    # Example to get filename:
    # /bin/python3 src/CodeReviewer.py tests/dummy.f90
    file_f90 = get_file_name_from_command_line()

    return cr.execute_validation(file_f90)


def get_file_name_from_command_line() -> str:
    """_summary_
    Get the file name from the command line
    """
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        print('No file name provided')
        return ''

if __name__ == '__main__':

    sys.exit(main())  # next section explains the use of sys.exit