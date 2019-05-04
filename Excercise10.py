# def func(a,*args):
#     if not args:
#         return "You don't pass any args"
#     else:
#         return [i**a for i in args]
#
# nums = [i for i in range(1,11)]
# print(func(2,*nums))

def func(name,*args,age=24,**kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)

func('sumit',1,2,3,age=22,hobby='cricket')