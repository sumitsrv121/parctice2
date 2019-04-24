def fibonacci_series(limit):
    a,b = 0,1
    for x in range(0,limit,1):
        print(a,end=' ')
        sum = a+b
        a = b
        b = sum

fibonacci_series(100)