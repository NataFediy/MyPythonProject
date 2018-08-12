#Print the palindromic triangle of size N as explained above.
# 1
# 121
# 12321
# 1234321
# 123454321
# Note:
# Using anything related to strings will give a score of 0.
# Using more than one for-statement will give a score of 0.
# Sample Input:
# 5
# Sample Output:
# 1
# 121
# 12321
# 1234321
# 123454321

for i in range(1,int(input())+1):
    print((10**i//9)**2)