# Calculator
# r -> raw string - keep \ / * symbols literal
print(r"""  
   /=================================\
   |   PY🐍THON   CALCULATOR          |
   |---------------------------------|
   |  7   8   9   +   \              |
   |  4   5   6   -   /              |
   |  1   2   3   *   \              |
   |  0   .   =   ÷   /              |
   \=================================/
""")

first_num = float(input("What is the first number?\n"))
operation = input("Pick an operation? (+, -, *, \)\n").strip()
second_num = float(input("What is the next number?\n"))
