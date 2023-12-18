import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import Parser_XML
import unittest  
import xml.etree.ElementTree as ET

class TestParserXML(unittest.TestCase):
    
    def test_parse_xml_happy_day(self):
        """Generate xml from open_fortran_parser and compares to generated when creating test
        """
        
        # code to generate true files - ran once
        # tree = ET.ElementTree(parser_xml.xml_struct)
        # tree.write('./tests/test_parse_xml_happy_day.xml', encoding='utf-8', xml_declaration=True)
        
        parser_xml = Parser_XML.Parser_XML()
            
        file_f90 = './code_under_test/modConvParGF.F90'
        parser_xml.parse(file_f90)
        tree_test = ET.ElementTree(parser_xml.xml_struct)
        xml_content_test = ET.tostring(tree_test.getroot(), encoding='unicode')

        tree_true = ET.parse('./tests/test_parse_xml_happy_day.xml')
        xml_content_true = ET.tostring(tree_true.getroot(), encoding='unicode')

        # Assert that the XML content of the files is equal
        self.assertEqual(xml_content_true, xml_content_test)

if __name__ == '__main__':
    unittest.main()
