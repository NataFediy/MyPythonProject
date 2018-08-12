#! Task from http://codingbat.com:
# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers
# that come immediately after a 13 also do not count.
#
# Examples:
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6


def sum13(nums):
    result = 0
    if len(nums) == 0:
        return 0
    else:
        i = 0
        while i < len(nums):
            if nums[i] != 13:
                result = result + nums[i]
                i = i + 1
            else:
                i = i + 2

    return result


print(sum13([1, 2, 13, 2, 1, 13]))  # 4
print(sum13([13, 1, 2, 13, 2, 1, 13]))  # 3
print(sum13([13, 1, 13]))  # 0
print(sum13([5, 13, 2]))  # 5
