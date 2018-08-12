# Task:
# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
#
# Input Format:
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s.
# All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands
# followed by their associated value.
#
# Output Format:
# Print the sum of the elements of set s on a single line.
#
# Sample Input:
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5
# Sample Output:
# 4
# Explanation:
# After completing these 10 operations on the set, we get set ([4]).
# Hence, the sum is 4.
#
# Note:
# Convert the elements of set s to integers while you are assigning them.
# To ensure the proper input of the set, we have added the first two
# lines of code to the editor.

n = int(input())
s = set(map(int, input().split()))
num = int(input())
for _ in range(num):
    method = list(input().split())

    if len(s) != 0:
        if len(method) == 1:
            exec('s.{0}()'.format(method[0]))
        else:
            if int(method[1]) in s:
                exec('s.{0}({1})'.format(method[0], int(method[1])))
            else:
                continue

print(sum(s))
