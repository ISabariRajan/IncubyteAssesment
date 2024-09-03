import unittest
from calculator import StringCalculator, NegativeNumberException

class TestStringCalculator(unittest.TestCase):
  
  def setUp(self):
    self.calc = StringCalculator()

  def test_add_empty_string(self):
    self.assertEqual(self.calc.add(""), 0)
  
  def test_add_single_number(self):
    self.assertEqual(self.calc.add("10"), 10)
  
  def test_add_multiple_numbers(self):
    self.assertEqual(self.calc.add("1,2,5,6,3"), 17)
  
  def test_negative_number_exception(self):
    with self.assertRaises(NegativeNumberException) as context:
        self.calc.add("-1,-2,-3")
    self.assertTrue("negative numbers not allowed" in str(context.exception))
  

if __name__ == "__main_":
  unittest.main()