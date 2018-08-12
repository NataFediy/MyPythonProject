#! Task from http://codingbat.com:
# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars
# before small bars. Return -1 if it can't be done.
#
# Examples:
# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2


def make_chocolate(small, big, goal):
    if goal // 5 == big:
        num = goal - (goal // 5) * 5
        if num == goal:
            return 0
        else:
            if num <= small:
                return num
            else:
                return -1

    elif goal // 5 < big:
        n = goal - (goal // 5) * 5
        if n < small:
            return n
        elif n == small:
            return small
        else:
            return -1

    elif goal // 5 > big:
        new_n = big * 5
        if goal - new_n <= small:
            return goal - new_n
        else:
            return -1


print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
print(make_chocolate(6, 2, 7))
print(make_chocolate(4, 1, 5))
print(make_chocolate(4, 1, 4))
print(make_chocolate(5, 4, 9))
print(make_chocolate(9, 3, 18))
print(make_chocolate(3, 1, 9))
print(make_chocolate(1, 2, 7))
print(make_chocolate(1, 2, 6))
print(make_chocolate(1, 2, 5))
print(make_chocolate(6, 1, 10))
print(make_chocolate(6, 1, 11))
print(make_chocolate(6, 1, 12))
print(make_chocolate(6, 1, 13))
print(make_chocolate(6, 2, 10))
print(make_chocolate(6, 2, 11))
print(make_chocolate(6, 2, 12))
print(make_chocolate(60, 100, 550))
print(make_chocolate(1000, 1000000, 5000006))
print(make_chocolate(7, 1, 12))
print(make_chocolate(7, 1, 13))
print(make_chocolate(7, 2, 13))
