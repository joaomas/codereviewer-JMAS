import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from src import Parser_XML
import unittest  
# import xml.etree.ElementTree as ET
from src.Validator_XML import Validator_XML
from src.ValidatorConstructor_XML import ValidatorConstructor_XML


class TestValidator_XML(unittest.TestCase):
    
    def test_dummyF90(self):
        """Test validator on empty F90 file
        """
        validator_constructor_xml = ValidatorConstructor_XML()
        validator_xml = validator_constructor_xml.construct()
        str1 = validator_xml.run_validator('tests/dummy.F90')
        self.assertEqual('', str1)
        

if __name__ == '__main__':
    unittest.main()
