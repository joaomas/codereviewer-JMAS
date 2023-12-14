from Parser import Parser
import subprocess
import xml.etree.ElementTree as ET



class Parser_XML(Parser):

    def __init__(self) -> None:
        self.generate_xml()
        self.xml_struct


    def generate_xml(self):
        # TODO
        # Generate all xmlfiles using open-fortran-parser like createXML.bash
        # open_fortran_parser ./code_under_test/teste.F90 ./xml/saida.xml
        rc = subprocess.call ("/home/klclaudio/Documents/Monan/CodeReview/codereviewer/src/parser.bash")
        #pass
        return rc
        
        
    def parse(self): # TODO create XML_struct to return:
        
        #pass
        # xml_structure = Create struct  = root ?
        # TODO
        # get code from QA
        # ...
        # since main :
        
        # if __name__ == '__main__':
        #
        # read the files and get fields
        #    tree = ET.parse('./xml/saida.xml')
        #    root = tree.getroot() # Pega a raiz do xml
        # ...
        
        xml_struct = ET.parse('../xml/saida.xml')
        root = xml_struct.getroot() # Pega a raiz do xml
        
        return self.xml_struct
        
