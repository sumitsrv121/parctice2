from functools import wraps


def decorator_function(find_sum):
    wraps(find_sum)
    def wrapper_function(*args,**kwargs):
         return find_sum(*args,**kwargs) if all([True if(type(item) == int in args) else False for item in args]) else print("Inavlid Format")
    return wrapper_function


@decorator_function
def find_sum(*args):
    sum = 0
    for i in args:
        print(type(i))
        sum += i
    return sum

print(find_sum(20,30,40,50))
