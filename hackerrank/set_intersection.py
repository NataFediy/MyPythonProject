#    A.intersection(B) or A&B as an intersection
#
# Task:
# The students of District College have subscriptions to English and French
#  newspapers. Some students have subscribed only to English,
# some have subscribed only to French, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers.
# One set has subscribed to the English newspaper,
# one set has subscribed to the French newspaper.
# Your task is to find the total number of students who have subscribed to
# both newspapers.
#
# Input Format:
# The first line contains N, the number of students who have subscribed to
# the English newspaper.
# The second line contains N space separated roll numbers of those students.
# The third line contains B, the number of students who have subscribed to
# the French newspaper.
# The fourth line contains B space separated roll numbers of those students.
#
# Output Format:
# Output the total number of students
# who have subscriptions to both English and French newspapers.
#
# Sample Input:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output:
# 5
#
# Explanation:
# The roll numbers of students who have both subscriptions:
# 1,2,3,6 and 8.
# Hence, the total is 5 students.

n = int(input())
n_en = set(map(int, input().split()))
b = int(input())
b_fr = set(map(int, input().split()))
# both = n_en.intersection(b_fr)
# print(len(both))
print(len(n_en.intersection(b_fr)))