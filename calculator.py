
class StringCalculator:

  def add(self, numbers):
    """
      Adds the sum of all integers separated by commas in a given string.
      Args:
          numbers (str): A string containing numbers separated by commas.
          
      Returns:
          int: The total sum of all integers in the input string.
    """
    total = 0
    if numbers == "":
      return total
    numbers = numbers.split(",")
    
    for number in numbers:
      total += int(number)
    return total
  
