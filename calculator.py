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

    delimiters = re.search(r"[\D]", numbers).group()
    numbers = re.split("\n", numbers, 1)[1]
    if "-" == delimiters:
      raise InvalidDelimiterException()
    numbers = numbers.replace(delimiters, ",")
    return numbers

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

    # Get delimiter and numbers if it has delimiter
    if numbers.startswith("//"):
      numbers = numbers.strip("//")
      numbers = self.get_delimiters_and_numbers(numbers)

    numbers = numbers.replace("\n", ",").split(",")
    for number in numbers:
      number = int(number.strip())
      if number < 0:
        raise NegativeNumberException(number)
      total += number
    return total