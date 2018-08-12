class MyClass:
    x = 10
    def __init__(self):
        self.y = 20

c1 = MyClass()
c2 = MyClass()
print(c1.x, c2.x)
print(c1.y, c2.y)