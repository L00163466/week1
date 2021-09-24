# -------------------------------------------
# Math examples.
#
# (C) 2021 Aravind Rajesh Kanna, LYIT
# Available under GNU public license (GPL)
# -------------------------------------------


ans_1 = 6 + 8 / 2 - 1  # Expected ans is 9 because "+ & -" has more precedence than "/"
print(ans_1)
ans_2 = 1 + 1 - 1 + 2 / 2  # Expected ans is 2 because "+ & -" has more precedence than "/"
print(ans_2)
ans_3 = 1.1 + 5 / 2  # Expected ans is 3.6 because "+ & -" has more precedence than "/"
print(ans_3)
ans_4 = 9.2 / 3  # Expected ans is 3.06
print(ans_4)
ans_5 = 9.2 % 3  # Expected ans is 0.2
print(ans_5)
ans_6 = 1 * 2 + 3 * 5 % 4  # Expected ans is 5
print(ans_6)
ans_7 = 1 + 8 % 3 * 2 - 9  # Expected ans is -4
print(ans_7)
ans_8 = 6 + (24 % (16 - 11))  # Expected ans is 10 because bracket has more precedence
print(ans_8)
