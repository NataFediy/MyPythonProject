# Task
# Given 2 sets of integers, M and N,
# print their symmetric difference in ascending order.
# The term symmetric difference indicates those values
# that exist in either M or N but do not exist in both.
#
# Input Format:
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.
#
# Output Format:
# Output the symmetric difference integers in ascending order, one per line.
#
# Sample Input:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output:
# 4
# 5
# 7
# 9
# 10
# 11
# 21
# 55

m = int(input())
m_arr = set([item for item in input().split()])
n = int(input())
n_arr = set([item for item in input().split()])
n_arr.symmetric_difference_update(m_arr)
diff_arr = map(int, list(n_arr))
for item in sorted(diff_arr):
    print(item)