def even_number_generator(num):
    for i in range(1,num+1):
        if i%2 == 0:
            yield i
        else:
            continue


for i in even_number_generator(10):
    print(i)