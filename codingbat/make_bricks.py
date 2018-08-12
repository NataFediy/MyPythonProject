#! Task from http://codingbat.com:
# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks
# (5 inches each). Return True if it is possible to make the goal
# by choosing from the given bricks. This is a little harder than
# it looks and can be done without any loops.
#
# Examples:
# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True


def make_bricks(small, big, goal):
    n = big * 5
    if big > 0:
        if goal - n > small:
            return False
        elif goal % 5 == 0:
            return True
        elif goal % 5 == small:
            return True
        elif goal % 5 < small:
            return True
        elif goal % 5 > small:
            return False
    else:
        if goal - small == 0:
            return True
        elif goal - small < 0:
            return True
        else:
            return False


print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))