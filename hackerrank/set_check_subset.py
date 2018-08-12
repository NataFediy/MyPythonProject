# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
#
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.
#
# Input Format:
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.
#
# Output Format:
# Output True or False for each test case on separate lines.
for _ in range(int(input())):
    num_a = int(input())
    a = set(map(int, input().split()))
    num_b = int(input())
    b = set(map(int, input().split()))
    print('True' if a.issubset(b) else 'False')