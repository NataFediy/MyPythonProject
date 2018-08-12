#! Task from http://codingbat.com:
# Return the "centered" average of an array of ints,
# which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array.
# If there are multiple copies of the smallest value, ignore just one copy,
# and likewise for the largest value. Use int division to produce the final
# average. You may assume that the array is length 3 or more.
#
# Examples:
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3


def centered_average(nums):
    num = sorted(nums)
    max_nums = max(nums)
    min_nums = min(nums)
    num.remove(max_nums)
    num.remove(min_nums)
    print(num)

    if len(num) % 2 == 0:
        num_avg = (num[(len(num) // 2) - 1] + num[len(num) // 2]) / 2
    else:
        num_avg = num[len(num) // 2]
    return int(num_avg)


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
print(centered_average([5, 3, 4, 6, 2]))
print(centered_average([5, 3, 4, 0, 100]))
print(centered_average([100, 0, 5, 3, 4]))
print(centered_average([6, 4, 8, 12, 3]))
