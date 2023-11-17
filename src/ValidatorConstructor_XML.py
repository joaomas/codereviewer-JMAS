from ValidatorConstructor import ValidatorConstructor
from Parser_XML import Parser_XML
from Validator_XML import Validator_XML
from RuleValidator_XML import RuleValidator_XML_1

class ValidatorConstructor_XML(ValidatorConstructor):
    
    def __init__(self) -> None:
        super().__init__()
        
        
    def construct(self):    
        parser_xml = Parser_XML()
        validator_xml = Validator_XML(parser_xml)
        
        # TODO instantiate all rules
        ruleValidatorXML_1 = RuleValidator_XML_1()
        self.rule_validator_arr.append(ruleValidatorXML_1)
        # self.rule_validator_arr.append(ruleValidatorXML_2)
        
        return validator_xml