# String Calculator
This repository contains an implementation of a string calculator, along with a test suite that checks its functionality. The calculator is designed to handle addition operations on numbers separated by delimiters or new lines, while ignoring negative numbers.
- The default delimiter is comma (,)
- You can also use any custom delimiter by adding '//<delimiter>\n' before the numbers (eg: //[;]\n1;2;3)
- You can also use multiple delimiters (eg: //[;][,]\n1,2,3;4;4)
- You cannot use '-' as delimiter, A custom exception `InvalidDelimiterException` has been defined for handling this case
- A custom exception `NegativeNumberException` has been defined for handling cases when negative numbers are encountered during the calculation.
- The calculator will skip numbers bigger than 1000, based on https://osherove.com/tdd-kata-1/
# Requirement

1. Create a simple String calculator with a method signature like this:

    ```python
    def add(numbers)
    ```

      - Input: a string of comma-separated numbers
      - Output: an integer, sum of the numbers

      **Examples**:

      - Input: “”, Output: 0
      - Input: “1”, Output: 1
      - Input: “1,5”, Output: 6

2. Allow the add method to handle any amount of numbers.

3. Allow the add method to handle new lines between numbers (instead of commas). ("1\n2,3" should return 6)

4. Support different delimiters:

      - To change the delimiter, the beginning of the string will contain a separate line that looks like this: "//[delimiter]\n<numbers…>". For example, "//[;]\n1;2" where the delimiter is ";" should return 3.

5. Calling add with a negative number will throw an exception: "negative numbers not allowed <negative_number>".

      -  If there are multiple negative numbers, show all of them in the exception message, separated by commas.


# Installation, Usage and Test Suite

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ISabariRajan/StringCalculator.git
    ```
2. Change to the project directory:
    ```bash
    cd StringCalculator
    ```

## Usage

  To use the String Calculator, create a Python file (e.g., example.py) and import the necessary functions from the string_calculator.py module:

  ```python
    from string_calculator import StringCalculator

    # Create an instance of the StringCalculator class
    calc = StringCalculator()

    # Perform addition operations on numbers separated by commas or new lines
    result = calc.add("1,5,10")  # Output: 16
    print(result)

  ```

  I have also created a example.py file
  Open a terminal or command prompt and navigate to the project directory (e.g., cd StringCalculator). Run the following command to execute the example file:

  ```bash
  python example.py
  ```

## Test Suite

1. The repository also includes a test suite using the unittest module to verify the correctness of the String Calculator implementation. To run the tests, follow these steps:

2. Open a terminal or command prompt and navigate to the project directory (e.g., cd StringCalculator).
Run the following command to execute the test suite:

  ```bash
  python -m unittest test_string_calculator.py
  ```

## License
No License