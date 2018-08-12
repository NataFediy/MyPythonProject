# One of the built-in functions of Python is divmod, which takes two arguments
# A and B and returns a tuple containing the quotient of A/B first and
# then the remainder A.
#
# For example:
# >>> print divmod(177,10)
# (17, 7)
#
# Here, the integer division is 177/10 => 17
# and the modulo operator is 177%10 => 7.
#
# Task:
# Read in two integers, A and B, and print three lines.
# The first line is the integer division A//B
# (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: A%B.
# The third line prints the divmod of A and B.
#
# Input Format:
# The first line contains the first integer, A,
# and the second line contains the second integer, B.
#
# Output Format:
# Print the result as described above.
# Sample Input:
# 177
# 10
# Sample Output:
# 17
# 7
# (17, 7)


a = int(input())
b = int(input())
print(a // b)
print(a % b)
print(divmod(a, b))
