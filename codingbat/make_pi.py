#! Task from http://codingbat.com:
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
#
# Example:
# make_pi() → [3, 1, 4]


def make_pi():
    pi = {0:3, 1:1, 2:4}
    str_pi = []
    for i in range(len(pi)):
        str_pi.append(pi[i])
    return str_pi


print(make_pi())
