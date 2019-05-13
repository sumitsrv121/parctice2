def divide_check(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print('The number can\'t be divided by zero')
    except TypeError:
        print('Integers are required only')
    except:
        print('Unexpected error')


divide_check('3',2)