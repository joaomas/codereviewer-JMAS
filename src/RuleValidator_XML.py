
from abc import *
from src.RuleValidator import RuleValidator


# TODO - review its purpose - is it necessary ?
class RuleValidator_XML(RuleValidator):
    """_summary_
    Class for validating XML structure parsed from Fortran code
    """
    
    def __init__(self, description_in, code, points, mandatory) -> None:
        super().__init__(description_in, code, points, mandatory)
        
    @abstractmethod
    def check():
        pass
        

# all rules
# TODO - review points for each rule
    
class RuleValidator_XML_1(RuleValidator_XML):
    
    def __init__(self) -> None:
        super().__init__('snake case', '4.7', 1, True )
    
    def check(self, word) -> str:

        ret = ''
        ret_bool = True
        # def is_snake_case(word):
        if not word:
            ret_bool = False
        if not word[0].isalpha():
            ret_bool = False
        for char in word[0:]:
            if not char.isalpha() and not char.isdigit() and not char=="_":
                ret_bool = False
        for char in word[0:]:
            if char.isupper():
                ret_bool = False

        if not ret_bool:
        #           if not is_camel_case(sub.get("name")): #4.8 camelCase
        # ret =  print("Rule 4.8 : camelCase : Linhas",sub.get("line_begin"), sub.get("line_end"))
        #  points = points + 1.0
            ret = 'Error rule' + self.description()
          
        return ret  
        
class RuleValidator_XML_2(RuleValidator_XML):
    
    def __init__(self) -> None:
        super().__init__('verify_file_ext', '4.52', 10, True )
    
    def check (self, file_name):
        ret = ''
        if file_name.find(".F90") == -1:
            
            ret = 'Error Rule' + self.description () # print("Rule 4.52 file extention - .F90")
            #points = points
        return ret



# other rules ...
# class RuleValidator_XML_2(RuleValidator_XML)
# class RuleValidator_XML_3(RuleValidator_XML)
