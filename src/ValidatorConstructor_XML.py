from src.ValidatorConstructor import ValidatorConstructor
from src.Parser_XML import Parser_XML
from src.Validator_XML import Validator_XML
from src.RuleValidator_XML import *

class ValidatorConstructor_XML(ValidatorConstructor):
    
    def __init__(self) -> None:
        super().__init__()
        
        
    def construct(self):    
        parser_xml    = Parser_XML()
        validator_xml = Validator_XML(parser_xml)
        
        # TODO instantiate all rules here ?
        ruleValidatorXML_1 = RuleValidator_XML_1()
        ruleValidatorXML_2 = RuleValidator_XML_2()
        ruleValidatorXML_3 = RuleValidator_XML_3()
        
        validator_xml.rule_validator_dic['snake_case']         = ruleValidatorXML_1
        validator_xml.rule_validator_dic['verify_file_ext']    = ruleValidatorXML_2
        validator_xml.rule_validator_dic['verify_module_name'] = ruleValidatorXML_3


        # ...
        # ...
        
        return validator_xml