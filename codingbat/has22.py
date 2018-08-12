#! Task from http://codingbat.com:
# Given an array of ints, return True if the array contains a 2 next
# to a 2 somewhere.
#
# Examples:
# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False


def has22(nums):
    if len(nums) <= 1:
        return False
    else:
        num_str = ''
        for i in nums:
            num_str = num_str + str(i)
        num_str_arr = num_str.split('22')
        if len(num_str_arr) > 1:
            return True
        else:
            return False


print(has22([1, 2, 2]))  # → True
print(has22([1, 2, 1, 2]))  # → False
print(has22([2, 1, 2]))  # → False)
