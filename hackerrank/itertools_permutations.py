#! itertools.permutations(iterable[, r])
#
# This tool returns successive r length permutations of elements
# in an iterable.
# If r is not specified or is None, then r defaults to the length of
# the iterable, and all possible full length permutations are generated.
#
# Permutations are printed in a lexicographic sorted order.
# So, if the input iterable is sorted, the permutation tuples will be
# produced in a sorted order.
#
# Task:
# You are given a string S.
# Your task is to print all possible permutations of size k of the string
# in lexicographic sorted order.
#
# Input Format:
# A single line containing the space separated string S and the integer
# value k.
#
# Output Format:
# Print the permutations of the string S on separate lines.
#
# Sample Input:
# HACK 2
# Sample Output:
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
# Explanation:
# All possible size  permutations of the string "HACK" are printed
# in lexicographic sorted order.
import itertools

s, k = input().split(' ')
result = sorted([''.join(i) for i in [*itertools.permutations(s, int(k))]])
print(*result, sep="\n")
