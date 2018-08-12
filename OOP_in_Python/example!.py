class MaxSizeList(object):
    def __init__(self, max):
        self.max_size = max
        self.inner_list = []

    def push(self, obj):
        self.inner_list.append(obj)
        if len(self.inner_list) > self.max_size:
            self.inner_list.pop(0)

    def get_list(self):
        return self.inner_list


a = MaxSizeList(3)
b = MaxSizeList(1)

for i in ["hey", "hi", "let's", "go"]:
    a.push(i)
    b.push(i)

print(a.get_list())
print(b.get_list())
