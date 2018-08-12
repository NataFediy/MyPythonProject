#! Nested sorting:
# You are given a string S.
# S contains alphanumeric characters only.
# Your task is to sort the string  in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
#
# Input Format:
# A single line of input contains the string S.
#
# Output Format:
# Output the sorted string S.
#
# Sample Input:
# SEortTing8516234
# Sample Output:
# ginortEST1352468


s = input()
term_result = ''.join(sorted(s))
odd_res = ''
even_res = ''
result = ''
up_res = ''
other = ''
for item in term_result:
    if item.islower():
        result += item
    elif item.isupper():
        up_res += item
    elif item.isdigit():
        if int(item) % 2 == 0:
            odd_res += item
        else:
            even_res += item
    else:
        other += item
result += up_res + even_res + odd_res + other
print(result)
