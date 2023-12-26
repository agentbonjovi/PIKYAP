def print_result(func):
    def wrapper():

        print(func.name)
        func_return = func()
        if type(func_return) == type(dict()):
            for key, value in func_return.items():
                print(key, '=', value)
        elif type(func_return) == type(list()):
            for value in func_return:
                print(value)
        else:
            print(func_return)
    return wrapper

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


if __name__ == 'main':
    test_1()
    test_2()
    test_3()
    test_4()