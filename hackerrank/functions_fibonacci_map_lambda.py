#! You have to generate a list of the first N fibonacci numbers,
#  0 being the first number.
# Then, apply the map() function and a lambda expression to cube
# each fibonacci number and print the list.
#
# Concept:
# The map() function applies a function to every member of an iterable
# and returns the result. It takes two parameters: first, the function
# that is to be applied and secondly, the iterables.
# Let's say you are given a list of names, and you have to print a list
# that contains the length of each name.
#
# >> print (list(map(len, ['Tina', 'Raj', 'Tom'])))
# [4, 3, 3]
#
# Lambda is a single expression anonymous function often used as an
# inline function. In simple words, it is a function that has only one
# line in its body. It proves very handy in functional and GUI programming.
#
# >> sum = lambda a, b, c: a + b + c
# >> sum(1, 2, 3)
# 6
#
# Input Format:
# One line of input: an integer N.
#
# Output Format:
# A list on a single line containing the cubes of the first N fibonacci
# numbers.
#
# Sample Input:
# 5
# Sample Output:
# [0, 1, 1, 8, 27]
#
# Explanation:
# The first 5 fibonacci numbers are [0,1,1,2,3],
# and their cubes are [0,1,1,8,27].
cube = lambda x: pow(x, 3)


def fibonacci(n):
    fib_num = []
    a = 0
    b = 1
    for _ in range(n):
        fib_num.append(a)
        a, b = b, a + b
    return fib_num


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
    print(list(map(cube, fibonacci(n))))