#! Identify whether the number is prime or not
def isprime(num):
    if num < 2:
        return False
    else:
        for n in range(2, num):
            if num%n == 0:
                return False
        return True


print(isprime(0))       # false
print(isprime(2))       # true
print(isprime(212))     # false
print(isprime(23))      # true
print(isprime(2361))    # false