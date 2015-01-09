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

    @patch('src.function.logging')
    def test_split_function_two(self, mock_logging):
        result = function.split_some_parts('test.some')
        self.assertEqual(result, 2)
        self.assertTrue(mock_logging.info.called)

    @patch('src.function.logging')
    def test_split_function_three(self, mock_logging):
        result = function.split_some_parts('test.some.more')
        self.assertEqual(result, 3)
        self.assertTrue(mock_logging.info.called)

    @patch('src.function.logging')
    def test_split_function_moar(self, mock_logging):
        result = function.split_some_parts('test.some.more.content')
        self.assertEqual(result, 1)
        self.assertTrue(mock_logging.warn.called)