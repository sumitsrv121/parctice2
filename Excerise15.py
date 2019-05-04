from functools import wraps

def decorator_function(func):
    @wraps(func)
    def wrapper_funtion(*args,**kwargs):
        """this is wrapper function"""
        print(f'you are calling {func.__name__} function')
        print(f'{func.__doc__}')
        return func(*args,**kwargs)
    return wrapper_funtion

@decorator_function
def add(a,b):
    """This function takes two arguments and return their sum"""
    return a+b

print(add(2,3))


