# ABCXYZ company has up to  employees.
# The company decides to create a unique identification number (UID) for each
# of its employees.
# The company has assigned you the task of validating all the randomly generated
# UIDs.
#
# A valid UID must follow the rules below:
#
# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0 - 9).
# It should only contain alphanumeric characters (a-z, A - Z & 0 - 9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.
#
# Input Format:
#
# The first line contains an integer N, the number of test cases.
# The next N lines contains an employee's UID.
#
# Output Format:
#
# For each test case, print 'Valid' if the UID is valid. Otherwise, print
# 'Invalid', on separate lines. Do not print the quotation marks.
#
# Sample Input:
#
# 2
# B1CD102354
# B1CDEF2354
# Sample Output:
#
# Invalid
# Valid
# Explanation
#
# B1CD102354:  is repeating → Invalid
# B1CDEF2354: Valid
import re


def valid(uid):
    if len(uid) > 10:
        return 'Invalid'
    else:
        if not re.search(r'([A-Z].*){2}', uid):
            return 'Invalid'
        if not re.search(r'(\d.*){3}', uid):
            return 'Invalid'
        if not re.search(r'[a-zA-Z\d]{10}', uid):
            return 'Invalid'
        if re.search(r'(.).*\1', uid):
            return 'Invalid'
        return 'Valid'


for _ in range(int(input())):
    print(valid(input()))

