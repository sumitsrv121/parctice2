from functools import wraps
import time


def calculate_time(func):

    @wraps(func)
    def wrapper_func(*args,**kwargs):
        t1 = time.time()
        func(*args,**kwargs)
        t2= time.time()
        print(t2-t1)
    return wrapper_func


@calculate_time
def func(n):
    return [i**2 for i in range(1,n+1)]

func(1000)