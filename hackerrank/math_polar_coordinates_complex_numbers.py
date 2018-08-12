# Task:
# You are given a complex Z. Your task is to convert it to polar coordinates.
#
# Input Format:
# A single line containing the complex number Z.
# Note: complex() function can be used in python to convert
# the input as a complex number.
#
# Output Format:
# Output two lines:
# The first line should contain the value of R(radius).
# The second line should contain the value of G(phase angle).
#
# Sample Input:
# 1+2j
# Sample Output:
# 2.23606797749979
# 1.1071487177940904
#
# Note: The output should be correct up to 3 decimal places.

import cmath


z = complex(input())
print('%.3f' % cmath.polar(z)[0])
print('%.3f' % cmath.polar(z)[1])
