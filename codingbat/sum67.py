#! Task from http://codingbat.com:
# Return the sum of the numbers in the array, except ignore sections
# of numbers starting with a 6 and extending to the next 7
# (every 6 will be followed by at least one 7). Return 0 for no numbers.
#
# Examples:
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4


def sum67(nums):
    result = 0
    if len(nums) == 0:
        return 0
    else:
        i = 0
        while i < len(nums):
            if nums[i] != 6:
                result = result + nums[i]
                i = i + 1
            else:
                j = i
                while j < len(nums):
                    if nums[j] != 7:
                        j = j + 1
                    else:
                        i = j + 1
                        break
        return result


print(sum67([1, 2, 2]))  # → 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))  # → 5
print(sum67([1, 1, 6, 7, 2]))  # → 4
