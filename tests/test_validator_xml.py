import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from src import Parser_XML
import unittest
# import xml.etree.ElementTree as ET
from src.Validator_XML import Validator_XML
from src.ValidatorConstructor_XML import ValidatorConstructor_XML


class TestValidator_XML(unittest.TestCase):

    def test_dummyF90_happyday(self):
        """Test validator on empty F90 file by the same path of main Codereviewer
        """
        validator_constructor_xml = ValidatorConstructor_XML()
        validator_xml = validator_constructor_xml.construct()
        str1          = validator_xml.run_validator('tests/dummy.F90')
        self.assertEqual('', str1)


    def test_validator_XML_rule_verify_file_ext_fail(self):
        """Test the validator using a dummy.f90 file, and check that the assertion
        is equals the error of method check of the class RuleValidator_XML_2
        """
        validator_constructor_xml = ValidatorConstructor_XML()
        validator_xml = validator_constructor_xml.construct()
        str1          = validator_xml.run_validator('tests/test_validator_xml_rule_verify_file_ext_fail.F90')
        self.assertEqual(str1, 'Error Rule verify_file_ext \n')


    def test_validator_XML_rule_verify_module_name_fail(self):
        """Test the validator using a mod file, and check that the assertion
        is equals the error of method check of the class RuleValidator_XML_3
        """
        validator_constructor_xml = ValidatorConstructor_XML()
        validator_xml = validator_constructor_xml.construct()
        str1          = validator_xml.run_validator('tests/test_module_name_fail.f90')
        self.assertEqual(str1, 'Error Rule verify_module_name \n')

    def test_validator_XML_snake_case_fail(self):
        """Test the validator using a mod file, and check that the assertion
        is equals the error of method check of the class RuleValidator_XML_3
        """
        #TODO
        # validator_constructor_xml = ValidatorConstructor_XML()
        # validator_xml = validator_constructor_xml.construct()
        # str1          = validator_xml.run_validator('tests/test_module_name_fail.f90')
        # self.assertEqual(str1, 'Error Rule verify_module_name \n')


if __name__ == '__main__':
    unittest.main()
