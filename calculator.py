import re

class NegativeNumberException(Exception):
    def __init__(self, number):
        super().__init__(f"negative numbers not allowed {number}")

class InvalidDelimiterException(Exception):
  def __init__(self, delimiter="-"):
    super().__init__(f"Delimiter {delimiter} is not allowed")


class StringCalculator:

  def get_delimiters_and_numbers(self, numbers):
    """
    Extracts the delimiters and numbers from the input string 'numbers'.
      Args:
        numbers (str): The string containing delimiters and numbers.
      
      Returns:
        tuple: A tuple containing the extracted delimiters and numbers.
      
      Raises:
        InvalidDelimiterException: If the delimiters contain a hyphen (-) character.
    """

    delimiters = re.search(r"//[\D]+\n", numbers).group()
    if "-" in delimiters:
      raise InvalidDelimiterException()
    numbers = numbers.replace(delimiters, "")
    return delimiters, numbers

  def split_numbers_with_delimiters(self, delimiters, numbers):
    """
    Splits the input string 'numbers' using the specified 'delimiters' as a delimiter.
      Args:
        delimiters (str): The character or sequence of characters to use as a delimiter.
        numbers (str): The string containing numbers separated by the specified delimiters.
      
      Returns:
        list: A list of strings, where each string contains a number and its surrounding delimiters.
    """

    return re.split(
       r'[' + re.escape(delimiters) + r']',
       numbers
    )

  def add(self, numbers):
    """
    Adds the sum of all positive integers separated by commas in a given string.
      Args:
        numbers (str): A string containing numbers separated by commas
          
      Returns:
        int: The total sum of all positive integers in the input string.
          
      Raises:
          NegativeNumberException: If any number in the input string is negative.
    """

    # remove empty spaces and check empty string
    total = 0
    numbers = numbers.strip()
    if numbers == "":
      return total

    # Use comma(,) as a default delimiter
    delimiters = ","
    # Get delimiter and numbers if it has delimiter
    if numbers.startswith("//"):
      delimiters, numbers = self.get_delimiters_and_numbers(numbers)

    numbers = self.split_numbers_with_delimiters(delimiters, numbers)
    for number in numbers:
      number = int(number.strip())
      if number < 0:
        raise NegativeNumberException(number)
      total += number
    return total