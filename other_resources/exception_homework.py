#Task 1
#Handle the exception thrown by the code below by using try and except blocks.

def exc_example(arr):
    n = 0
    for i in arr:
        try:
            n = i ** 2
        except TypeError as err:
            print(err.__class__.__name__)
            print(err)
        else:
            continue
    return n

print(f"Result is {exc_example(['a', 'b', 'c'])}")
print("Result is {}".format(exc_example([1, 2, 3])))
print("Result is", exc_example([1, 2, 3]))

print('--'*21)

#Task 2
#Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError as err:
    print("The action is impossible: ".format(err))
finally:
    print('All Done.')

print('--'*21)

#Task 3
#Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            n = int(input('Input an integer:'))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print('Input an integer: {}'.format(n))
            print('Your number squared is :', n**2)
            break
        finally:
            print('Thank you!')

ask()