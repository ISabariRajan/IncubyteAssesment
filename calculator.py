class NegativeNumberException(Exception):
    def __init__(self, message="negative numbers not allowed"):
        super().__init__(message)

class StringCalculator:

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
    total = 0
    if numbers == "":
      return total
    numbers = numbers.split(",")

    for number in numbers:
      number = int(number)
      if number < 0:
        raise NegativeNumberException()
      total += number
    return total
  
