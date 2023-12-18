from src.Parser import Parser
import subprocess
import xml.etree.ElementTree as ET
import open_fortran_parser as ofp


class Parser_XML(Parser):

    def __init__(self) -> None:
        self.xml_struct = None


    def parse(self, file_f90): # TODO create XML_struct to return:
        
        self.xml_struct = ofp.parse(file_f90, verbosity=0)
        return self.xml_struct
        
