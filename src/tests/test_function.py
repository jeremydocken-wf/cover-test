import unittest

from mock import patch
from src import function


class BogusFunctionTestCase(unittest.TestCase):
    """
    test ../function.py
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('src.function.logging')
    def test_split_function_one(self, mock_logging):
        result = function.split_some_parts('test')
        self.assertEqual(result, 1)
        self.assertTrue(mock_logging.info.called)