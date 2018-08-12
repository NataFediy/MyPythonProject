#! Find missing numbers
def find_missing_numbers(array):
    array.sort()
    result = list()
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        if diff > 1:
            for j in range(1, diff):
                result.append(array[i] + j)
    return result


print(find_missing_numbers([]))  # undefined
print(find_missing_numbers([1, 4, 3]))  # 2
print(find_missing_numbers([2, 3, 4]))
print(find_missing_numbers([5, 1, 4, 2]))  # 3
print(find_missing_numbers([1, 11, 3, 4]))  # 2 5 6 7 8 9 10
