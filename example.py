from calculator import StringCalculator

# Creates obj for StringCalculator
calc = StringCalculator()

# Calls add function
output = calc.add("")
print(output)

output = calc.add("1")
print(output)

output = calc.add("1, 2, 1,3 ,4,5")
print(output)

output = calc.add("""//[;]
              1;2\n3;4;5
              """)
print(output)

output = calc.add("""//[****]
              1\n2\n3****4****5
              """)
print(output)
try:
  output = calc.add("-1,-2,-3")
  print(output)
except:
  pass
print(calc.getCalledCount())