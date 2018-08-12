#! FazzBizz game:
def fazz_bizz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FazzBizz'
    elif num % 3 == 0:
        return 'Fazz'
    elif num % 5 == 0:
        return 'Bizz'
    else:
        return num


for i in range(51):
    print(fazz_bizz(i))
