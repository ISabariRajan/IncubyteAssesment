import re

class NegativeNumberException(Exception):
    def __init__(self, number):
        super().__init__(f"negative numbers not allowed: {number}")

class InvalidDelimiterException(Exception):
  def __init__(self, delimiter="-"):
    super().__init__(f"Delimiter {delimiter} is not allowed")


class StringCalculator:

  def handle_delimiters_and_clean_numbers(self, numbers):
    """
    Extracts the delimiters and cleans the numbers from the input string 'numbers'.
    Args:
      numbers (str): The string containing delimiters and numbers.

    Returns:
      str: A cleaned string containing only the numbers separated by commas.

    Raises:
      InvalidDelimiterException: If any delimiter contains a hyphen (-) character.
    """

    delimiters = re.findall(r"\[(.*?)\]", numbers)
    numbers = re.split("\n", numbers, 1)[1] # remove delimiter part from numbers
    for delimiter in delimiters:
      numbers = numbers.replace(delimiter, ",")
      if "-" == delimiter:
        raise InvalidDelimiterException()

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
    numbers = numbers.strip()
    if numbers == "":
      return 0

    if numbers.startswith("//"):
      numbers = self.handle_delimiters_and_clean_numbers(numbers)
    
    numbers = numbers.replace("\n", ",").split(",")

    positive_number = []
    negative_numbers = []
    for number in numbers:
      number = int(number.strip())
      if number < 0:
        negative_numbers.append(number)
      elif number <= 1000:
        positive_number.append(number)

    if len(negative_numbers) > 0:
      raise NegativeNumberException(",".join(map(str, negative_numbers)))

    return sum(positive_number)