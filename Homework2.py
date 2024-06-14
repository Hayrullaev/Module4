d = 11


def test_function(b):
    d = b ** 2

    def inner_function(b):
        if b % 2 == 0:
            print('Я в области видимости функции test_fuction')
        else:
            print('Я не в области видимости функции test_function')

    inner_function(b)
    return d


print(d)
test_function(d)
# print(inner_function(b) # результат выдает ошибку
