#! Task:
# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay X(i) amount
# of money only if they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.
# Sample Input:
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output
#
# 200
# Explanation
#
# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.
#
# Total money earned = 55 + 45 + 40 + 60 = 200
#
# mylist = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
# number_of_shoes = 10
# number_of_customers = 6
# shoes_dic = Counter(mylist)
# print(shoes_dic)
#
# num_cusomers = int(input('Input number of customers: '))
# n = int(input('Input number of shoes in stock: '))
# my_list = []
# for item in range(1, n+1):
#     my_list[item] = int(input('Input size of the shoes in stock: '))

from collections import Counter

x = int(input())
shoe_size = list(map(int, input().split()))
shoes_in_stock = Counter(shoe_size)
n = int(input())
income = 0

for i in range(0, n):
    key_size, price = map(int, input().split())
    if key_size in shoes_in_stock.keys():
        if shoes_in_stock[key_size] > 0:
            income += price
            shoes_in_stock[key_size] -= 1

print(income)
