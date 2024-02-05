import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from src import Parser_XML
import unittest
# import xml.etree.ElementTree as ET
from src.RuleValidator_XML import RuleValidator_XML_2
from src.RuleValidator_XML import RuleValidator_XML_3



class TestRuleValidator_XML(unittest.TestCase):

    def test_verify_file_ext(self):
        """Test rule 2
        """

        rule2 = RuleValidator_XML_2()
        ret = rule2.check('test_parse_xml_happy_day.F90')
        self.assertEqual('', ret)
        self.assertEqual('verify_file_ext', rule2.description)
        self.assertEqual('4.52', rule2.code)
        self.assertEqual(True, rule2.mandatory)
        self.assertEqual(10, rule2.points, 'wrong points')

    def test_verify_module_name(self):
        """Test rule 3
        """

        rule3 = RuleValidator_XML_3()
        ret = rule3.check('modteste.F90')
        self.assertEqual('', ret)
        self.assertEqual('verify_module_name', rule3.description)
        self.assertEqual('4.31', rule3.code)
        self.assertEqual(True, rule3.mandatory)
        self.assertEqual(10, rule3.points, 'wrong points')


if __name__ == '__main__':
    unittest.main()
