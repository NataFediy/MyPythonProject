#! Find the first index of item in array
def index_of(arr, item):
    if item not in arr:
        return f"{item} is not in {arr}"
    else:
        for i in range(len(arr)):
            if arr[i] == item:
                return i


print(index_of('abcdcba', 'Z'))
print(index_of('abcd', 'A'))
print(index_of('abcd', 'a'))
print(index_of('A man a plan a canal Panama', 'P'))
print(index_of([1, 2, 3], 2))
print(index_of([1, 2, 3], 4))
