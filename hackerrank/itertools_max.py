#! You are given a function f(x) = x**2. You are also given K lists.
# The list consists of n elements.
# You have to pick one element from each list so that the value
# from the equation below is maximized:
# S = (f(x1) + ... + f(xk))%M
# Note that you need to take exactly one element from each list,
# not necessarily the largest element. You add the squares of the chosen
# elements and perform the modulo operation. The maximum value that you
# can obtain, will be the answer to the problem.
#
# Input Format:
# The first line contains 2 space separated integers K and M.
# The next K lines each contains an integer Ni, denoting the number of
# elements in the i-th list, followed by Ni space separated integers
# denoting the elements in the list.
#
# Output Format:
# Output a single integer denoting the value Smax.
#
# Sample Input:
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
# Sample Output:
# 206

# Explanation:
# Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list
# gives the maximum S value equal to (5**2 + 9**2 + 10**2)%1000 = 206.

from itertools import product

n, m = map(int, input().split(' '))
l = []
for _ in range(n):
    l.append(list(map(int, input().split(' '))))
result = []
for i in list(product(*l)):
    result.append(sum(list(pow(j, 2) for j in list(i))))
print(max(result) % m)

# OR

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i ** 2 for i in x) % M, product(*N))
print(max(results))
