#! Task from http://codingbat.com:
# Given three ints, a b c, return True if one of b or c is "close"
# (differing from a by at most 1), while the other is "far",
# differing from both other values by 2 or more.
# Note: abs(num) computes the absolute value of a number.
#
# Examples:
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True


def close_far(a, b, c):
    if abs(a - b) <= 1 and abs(b - c) > 2:
        return True
    elif abs(a - c) <= 1 and abs(b - c) > 2:
        return True
    elif abs(a - b) > 1 and abs(b - c) >= 2:
        return True
    elif abs(a - c) > 1 and abs(b - c) >= 2:
        return True
    else:
        return False


print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))
print(close_far(4, 5, 3))
print(close_far(4, 3, 5))
print(close_far(-1, 10, 0))
print(close_far(0, -1, 10))
print(close_far(10, 10, 8))
print(close_far(10, 8, 9))
print(close_far(8, 9, 10))
print(close_far(8, 9, 7))
print(close_far(8, 6, 9))
