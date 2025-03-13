
import unittest
from ..reverse_string import reverse_string



class TestReverseString(unittest.TestCase):
  '''
  Test suite for the reverse_string function.
    
    Tests cover basic functionality, edge cases, and error handling for the
    reverse_string function.
  '''

  def test_reverse_string(self):
    ''' test case for the basic functionaliy of the function '''
    self.assertEqual(reverse_string('Karime'),'emiraK')

  def test_reverse_empty_str(self):
    '''
    test case for empty string
    '''
    self.assertEqual(reverse_string(''),'')

  def test_userinput_type(self):
    '''
    test case for checking user_input type
    '''
    with self.assertRaises(TypeError):
            reverse_string(12)
