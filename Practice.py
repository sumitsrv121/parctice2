def square_list(l):
    square = []
    for x in l:
        square.append(x*x)
    return square


square_arr = list(range(1,11))
print(square_list(square_arr))

