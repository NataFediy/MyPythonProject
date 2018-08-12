#! Task:
# There is a horizontal row of n cubes.
# The length of each cube is given. You need to create
# a new vertical pile of cubes. The new pile should follow these directions:
# if cube(i) is on top of cube(j) then sideLength(i) >= sideLength(j).
# When stacking the cubes, you can only pick up either the leftmost or
# the rightmost cube each time.
# Print "Yes" if it is possible to stack the cubes. Otherwise, print "No".
# Do not print the quotation marks.
#
# Input Format:
# The first line contains a single integer T, the number of test cases.
# For each test case, there are 2 lines.
# The first line of each test case contains n, the number of cubes.
# The second line contains n space separated integers,
# denoting the sideLengths of each cube in that order.
#
# Output Format:
# For each test case, output a single line containing either "Yes" or "No"
# without the quotes.
#
# Sample Input:
# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2
# Sample Output:
# Yes
# No
# Explanation:
# In the first test case, pick in this order:
# left - 4, right - 4, left - 3, right - 3, left - 2, right - 1.
# In the second test case, no order gives an appropriate arrangement
# of vertical cubes. 3 will always come after either 1 or 2.

from collections import deque

for _ in range(int(input())):
    cube_number = int(input('input numbers of cube: '))
    cubes = [int(i) for i in input().split()]
    x, y = 0, cube_number - 1
    while x < cube_number - 1 and cubes[x] >= cubes[x + 1]:
        x += 1
    while y > 0 and cubes[y] >= cubes[y - 1]:
        y -= 1
    print('Yes' if x >= y else 'No')

# OR

for _ in range(int(input())):
    _ = input()
    d = deque(map(int, input().split()))
    flag = "Yes"
    for _ in range(len(d) - 1):
        t = max(d[0], d[1], d[-1], d[-2])
        if t == d[0]:
            d.popleft()
        elif t == d[-1]:
            d.pop()
        else:
            flag = "No"
            break
    print(flag)
