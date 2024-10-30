def print_result(func):
    def dec(*args, **kwargs):
        s = func(*args, **kwargs)
        print(f"{func.__name__}")
        return s
    return dec

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    print(test_1())
    print(test_2())
    print(test_3())
    print(test_4())
