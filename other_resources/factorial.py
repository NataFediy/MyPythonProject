#! factorial via recursion:
def fact(num):
    if num < 0:
        return -1
    elif num == 0:
        return 1
    else:
        return num * fact(num - 1)


print(fact(5))
for i in range(6):
    print(fact(i))
