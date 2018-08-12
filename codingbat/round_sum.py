#! Task from http://codingbat.com:
# For this problem, we'll round an int value up to the next multiple of 10
# if its rightmost digit is 5 or more, so 15 rounds up to 20.
# Alternately, round down to the previous multiple of 10 if its rightmost
# digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c,
# return the sum of their rounded values. To avoid code repetition,
# write a separate helper "def round10(num):" and call it 3 times.
# Write the helper entirely below and at the same indent level as round_sum().
#
# Examples:
# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10


def round_sum(a, b, c):
    def round10(num):
        if 10 <= num:
            n = num%10
            if 0 <= n < 5:
                num = (num//10) * 10
            else:
                num = (num//10 + 1) * 10
        else:
            if 0 <= num < 5:
                num = 0
            else:
                num = 10
        return num

    new_a = round10(a)
    new_b = round10(b)
    new_c = round10(c)
    return new_a + new_b + new_c


print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))
