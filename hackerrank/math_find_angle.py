#! Find the value of angle in degrees
# Input Format:
# The first line contains the length of side AB.
# The second line contains the length of side BC.
#
# Output Format:
# Output the value of angle in degrees.
#
# Note: Round the angle to the nearest integer.
#
# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.
#
# Sample Input:
# 10
# 10
# Sample Output:
# 45°

import math


AB, BC = int(input()),int(input())
hypotenuse = math.hypot(AB, BC)
angle = round(math.degrees(math.acos(BC/hypotenuse)))
degree_symbol = chr(176)
print(angle, degree_symbol, sep='')