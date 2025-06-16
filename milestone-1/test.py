#!/usr/bin/env python3
"""
Unit tests for Hello World CLI tool.
Generated with SoloPilot real-time linting validation.
"""

import unittest
import sys
from unittest.mock import patch
from io import StringIO

from implementation import hello_world, main


class TestHelloWorld(unittest.TestCase):
    """Test cases for Hello World CLI functionality."""
    
    def test_hello_world_function(self):
        """Test the basic hello_world function."""
        result = hello_world()
        self.assertEqual(result, "Hello, World!")
        self.assertIsInstance(result, str)
    
    def test_main_function_success(self):
        """Test main function with successful execution."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exit_code = main([])
            self.assertEqual(exit_code, 0)
            self.assertIn("Hello, World!", fake_out.getvalue())
    
    def test_main_function_with_args(self):
        """Test main function with command line arguments."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            exit_code = main(['--test'])
            self.assertEqual(exit_code, 0)
            self.assertIn("Hello, World!", fake_out.getvalue())


if __name__ == "__main__":
    unittest.main()