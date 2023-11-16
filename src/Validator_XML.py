
from src.Validator import Validator


class Validator_XML(Validator):
    """_summary_
    XML structure Validator for RuleValidator_XML rules
    """
    
    def __init__(self, parser_xml_in) -> None:
        super().__init__()
        # TODO
        self.parser_xml = parser_xml_in  #scturcture xml
        
    def run_validator(self):
        super().run_validator()
        
        xml = self.parser_xml.parse()
        # TODO loop over xml structure
        # for each rule check rule

        
        
        
