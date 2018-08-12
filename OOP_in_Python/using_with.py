class MyClass(object):
    def __enter__(self):
        print('we have entered "with"')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('we are leaving "with"')
        return self

    def sayhi(self):
        print('hi, instance %s' % (id(self)))


with MyClass() as cc:
    cc.sayhi()

print('after thr "with" block')
