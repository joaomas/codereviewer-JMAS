import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import Parser_XML
import unittest  
import xml.etree.ElementTree as ET


def are_equal_ignore_path(elem1, elem2):
    # Check if tags and text are equal
    if elem1.tag != elem2.tag or elem1.text != elem2.text:
        return False
    
    # Check attributes, ignoring 'path'
    attrs1 = {key: value for key, value in elem1.attrib.items() if key != 'path'}
    attrs2 = {key: value for key, value in elem2.attrib.items() if key != 'path'}

    if attrs1 != attrs2:
        return False

    # Recursively compare children
    return all(are_equal_ignore_path(child1, child2) for child1, child2 in zip(elem1, elem2))



class TestParserXML(unittest.TestCase):
    
    def test_parse_xml_happy_day(self):
        """Generate xml from open_fortran_parser and compares to generated when creating test
        """
                
        parser_xml = Parser_XML.Parser_XML()
            
        file_f90 = './tests/test_parse_xml_happy_day.F90'
        parser_xml.parse(file_f90)
        xml_struct_test = ET.ElementTree(parser_xml.xml_struct)
        
        # code to generate true files - it was ran once
        # xml_struct_test.write('./tests/test_parse_xml_happy_day.xml', encoding='utf-8', xml_declaration=True)
        
        root_test = xml_struct_test.getroot()
        
        xml_struct_true = ET.parse('./tests/test_parse_xml_happy_day.xml')
        root_true = xml_struct_true.getroot()
        self.assertTrue(are_equal_ignore_path(root_test, root_true))
        

if __name__ == '__main__':
    unittest.main()
