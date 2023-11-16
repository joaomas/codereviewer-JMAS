from ValidatorConstructor import ValidatorConstructor
from Parser_XML import Parser_XML
from Validator_XML import Validator_XML

class ValidatorConstructor_XML(ValidatorConstructor):
    
    def __init__(self) -> None:
        super().__init__()
        
        
    def construct(self):    
        parser_xml = Parser_XML()
        validator_xml = Validator_XML(parser_xml)
        
        # TODO instantiate all rules
        # self.rule_validator_arr.append(ruleValidatorXML_1)
        # self.rule_validator_arr.append(ruleValidatorXML_2)