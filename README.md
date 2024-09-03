# String Calculator

# Requirement

1. Create a simple String calculator with a method signature like this:

    ```python
     int add(string numbers)
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

      - To change the delimiter, the beginning of the string will contain a separate line that looks like this: "//[delimiter]\n[numbers…]". For example, "//;\n1;2" where the delimiter is ";" should return 3.

5. Calling add with a negative number will throw an exception: "negative numbers not allowed <negative_number>".

      -  If there are multiple negative numbers, show all of them in the exception message, separated by commas.


# Installation, Usage and Test Suite

This repository contains an implementation of a string calculator, along with a test suite that checks its functionality. The calculator is designed to handle addition operations on numbers separated by commas.

## Installation

1. Clone the repository:

    > git clone https://github.com/ISabariRajan/StringCalculator.git
2. Change to the project directory:
    ```bash
    cd StringCalculator
    ```

## Usage

  I will update this once I create an example python file or something

## Test Suite

1. The repository also includes a test suite using the unittest module to verify the correctness of the String Calculator implementation. To run the tests, follow these steps:

2. Open a terminal or command prompt and navigate to the project directory (e.g., cd StringCalculator).
Run the following command to execute the test suite:

  ```bash
  python -m unittest test_string_calculator.py
  ```

## License
No License