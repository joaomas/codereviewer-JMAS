
from Validator import Validator


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
        
        str_checks = ''
        xml = self.parser_xml.parse()
        
         
        # TODO get code from QA
        # from.....
        # ...
        # Inicio do processo com a análise das subrotinas
        # Percorre a árvore para as declarações de subrotina
        # for sub in root.iter("subroutine"):
        #    print("\n\nInspecionando a subrotina",sub.get("name"))
        # ....
            
        # subroutines
        # Test rule camel case
        
        # TODO
        word = 'TODO from xml'
        rule_snake = self.rule_validator_dic['snake_case']
        str_checks =  rule_snake.check(word)
        # Test rule implicit none 
        str_errors='' 
        
        
        
            
        return str_errors
        
        

        
        
        
