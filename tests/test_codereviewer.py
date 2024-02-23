import os
import sys

import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.CodeReviewer import CodeReviewer


class TestCodeReviewer(unittest.TestCase):

    def test_dummyF90_happyday(self):
        """Test Codereviewer class by passing the file dummy.F90
        """
        cr = CodeReviewer()
        str1 = cr.execute_validation('tests/dummy.F90')
        self.assertEqual('', str1)


if __name__ == '__main__':
    unittest.main()
