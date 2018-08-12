#! Task from http://codingbat.com:
# Given an array of ints length 3, return an array with the elements
# "rotated left" so {1, 2, 3} yields {2, 3, 1}.
#
# Examples:
# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]


def rotate_left3(nums):
    new_nums = []
    for i in range(1,len(nums)):
        new_nums.append(nums[i])
    new_nums.append(nums[0])
    return new_nums


print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))
print(rotate_left3([1, 2, 1]))
print(rotate_left3([0, 0, 1]))
