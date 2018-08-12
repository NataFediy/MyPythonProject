# Task:
# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
#
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.
#
# Input Format:
# The first line contains the number of items, N.
# The next N lines contains the item's name and price, separated by a space.
#
# Output Format:
# Print the item_name and net_price in order of its first occurrence.
#
# Sample Input:
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
#
# Sample Output:
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20
#
# Explanation:
# BANANA FRIES: Quantity bought: 1, Price: 12
# Net Price: 12
# POTATO CHIPS: Quantity bought: 2, Price: 30
# Net Price:
# APPLE JUICE: Quantity bought: 2, Price: 10
# Net Price:
# CANDY: Quantity bought: 4, Price: 5
# Net Price: 20
#
# >>> ordinary_dictionary = {}
# >>> ordinary_dictionary['a'] = 1
# >>> ordinary_dictionary['b'] = 2
# >>> ordinary_dictionary['c'] = 3
# >>> ordinary_dictionary['d'] = 4
# >>> ordinary_dictionary['e'] = 5
# >>>
# >>> print ordinary_dictionary
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# >>>
# >>> ordered_dictionary = OrderedDict()
# >>> ordered_dictionary['a'] = 1
# >>> ordered_dictionary['b'] = 2
# >>> ordered_dictionary['c'] = 3
# >>> ordered_dictionary['d'] = 4
# >>> ordered_dictionary['e'] = 5
# >>>
# >>> print ordered_dictionary
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

from collections import OrderedDict, Counter


n = int(input())
dic_ordered = OrderedDict()
arr = []
for i in range(n):
    temp_arr = list(input().split())
    price = int(temp_arr.pop())
    item = ' '.join(temp_arr)
    arr.append(item)
    dic_ordered[item] = price

for i, j in zip(dic_ordered.keys(), dic_ordered.values()):
    print(i + " " + str(dic_ordered.get(i)*Counter(arr).get(i)))