import unittest
from calculator import StringCalculator, NegativeNumberException

class TestStringCalculator(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.calc = StringCalculator()

  def test_add_empty_string(self):
    self.assertEqual(self.calc.add(""), 0)
  
  def test_add_single_number(self):
    self.assertEqual(self.calc.add("10"), 10)
  
  def test_add_multiple_numbers(self):
    self.assertEqual(self.calc.add("1,2,5,6,3"), 17)
  
  def test_add_negative_number_exception(self):
    with self.assertRaises(NegativeNumberException) as context:
        self.calc.add("-1,-2,-3")
    self.assertTrue("negative numbers not allowed: -1,-2,-3" in str(context.exception))

  def test_add_new_lines_multiple_numbers(self):
    self.assertEqual(self.calc.add("1,2\n5\n3"), 11)

  def test_custom_delimiters(self):
    self.assertEqual(self.calc.add("""//[;]
              1,2\n3;4;5
              """),
          15)

  def test_custom_multiple_delimiters(self):
    self.assertEqual(self.calc.add("""//[;][%]
              1;2;3;4%5
              """),
          15)

  def test_custom_multichar_delimiters(self):
    self.assertEqual(self.calc.add("""//[****]
              1****2****3****4****5
              """),
          15)

  def test_custom_multiple_multichar_delimiters(self):
    self.assertEqual(self.calc.add("""//[****][%%%%]
              1****2****3****4%%%%5
              """),
          15)

  def test_get_called_count(self):
    self.assertEqual(self.calc.getCalledCount(), 9)

if __name__ == "__main_":
  unittest.main()