#! Filter array:
def filter_array(array, condition, num):
    arr = sorted(array)
    result = []
    if arr[0] == num and condition == '<':
        return f"It's impossible find values < {num} because {num} is min"
    elif arr[len(arr) - 1] == num and condition == '>':
        return f"It's impossible find values > {num} because {num} is max"
    elif condition == '<':
        result = [x for x in arr if x < num]
    elif condition == '<=':
        result = [x for x in arr if x <= num]
    elif condition == '>':
        result = [x for x in arr if x > num]
    elif condition == '>=':
        result = [x for x in arr if x >= num]
    elif condition == '==':
        result = [x for x in arr if x == num]
    return result


array = [-17, 0, 2, 2, 3, 5]

print(filter_array(array, '<', 3))
print(filter_array(array, '>=', 2))
print(filter_array(array, '>', 5))
print(filter_array(array, '<', -17))
print(filter_array(array, '==', 2))
