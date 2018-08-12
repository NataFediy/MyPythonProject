#! Find max and sort array
def max_value(array):
    arr = sorted(array)
    return arr[len(arr) - 1]


def sort_array(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array


array = [-17, 2, 5, 3, 2, 0]
print(array)
print(sort_array(array))
print(max_value(array))
