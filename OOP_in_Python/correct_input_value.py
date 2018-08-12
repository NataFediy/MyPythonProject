class MyException(Exception):
    def __init__(self, msg_value):
        self.msg = msg_value

    def __str__(self):
        return self.msg


print('Input digital value')
while True:
    x = input('Input value: ')
    if not x.isalnum():
        print(f'{x} is a number')
        break
    else:
        print("It's not a number. Please input a digital value")

try:
    a = 1 / 0
except MyException as err:
    print(err)
    print(err.msg)
