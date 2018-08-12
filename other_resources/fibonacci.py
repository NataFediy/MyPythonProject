#! fibonacci
def fibo_element(n):
    array = []
    a = 0
    a1 = 1
    for i in range(n + 1):
        array.append(a)
        a = a + a1
        a1 = a - a1
    return array


def fib(n):
    fibonacci = []
    a = 0
    b = 1
    for i in range(n+1):
        fibonacci.append(a)
        a, b = b, a + b

    return fibonacci


print(fib(6))
print(fibo_element(6))
