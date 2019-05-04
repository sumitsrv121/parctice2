def operation(*args,**kwargs):
    return [i[::-1].title() if (kwargs.get('reverse_string') == True)  else i.title() for i in args ]
    return [i.title() if (reverse_str == False) else i[::-1].title() for i in lis]

l = ['mohit','rohit','ankit']
print(operation(*l,reverse_string=False))