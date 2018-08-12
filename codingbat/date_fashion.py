#! Task from http://codingbat.com:
# You and your date are trying to get a table at a restaurant.
# The parameter "you" is the stylishness of your clothes, in the range 0..10,
# and "date" is the stylishness of your date's clothes. The result getting
# the table is encoded as an int value with 0=no, 1=maybe, 2=yes.
# If either of you is very stylish, 8 or more, then the result is 2 (yes).
# With the exception that if either of you has style of 2 or less,
# then the result is 0 (no). Otherwise the result is 1 (maybe).
#
# Examples:
# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1


def date_fashion(you, date):
    if 3 <= you and 8 <= date <= 10:
        return 2
    elif 8 <= you <= 10 and 3 <= date:
        return 2
    elif you <= 2 or date <= 2:
        return 0
    else:
        return 1


print(date_fashion(5, 10))  # → 2   OK
print(date_fashion(5, 2))  # → 0	OK
print(date_fashion(5, 5))  # → 1	OK
print(date_fashion(3, 3))  # → 1	OK
print(date_fashion(10, 2))  # → 0	OK
print(date_fashion(2, 9))  # → 0	OK
print(date_fashion(9, 9))  # → 2	OK
print(date_fashion(10, 5))  # → 2	OK
print(date_fashion(2, 2))  # → 0	OK
print(date_fashion(3, 7))  # → 1	OK
print(date_fashion(2, 7))  # → 0	OK
