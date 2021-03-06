# You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
#
# A valid credit card from ABCD Bank has the following characteristics:
#
# ► It must start with a ,  or .
# ► It must contain exactly  digits.
# ► It must only consist of digits (-).
# ► It may have digits in groups of , separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have  or more consecutive repeated digits.
#
# Examples:
#
# Valid Credit Card Numbers
#
# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214
# Invalid Credit Card Numbers
#
# 42536258796157867       #17 digits in card number → Invalid
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
# Input Format
#
# The first line of input contains an integer .
# The next  lines contain credit card numbers.
#
# Constraints
#
#
# Output Format
#
# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.
#
# Sample Input
#
# 6
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456
# Sample Output
#
# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid

import re


def valid_number(num):
    if not re.search(r'^[456]', num):
        return 'Invalid'
    else:
        digit_and_sep = re.match(r"(-?\d{4}){4}$",num)
        consecutive = re.search(r"(.)(-?\1){3,}",num)
        if digit_and_sep and not consecutive:
            return 'Valid'
        else:
            return 'Invalid'


for _ in range(int(input())):
    print(valid_number(input()))
