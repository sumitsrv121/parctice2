def func(list1):
    count = 0

    for x in list1:
        if type(x) is list:
            count += 1
    return count


list11 = [1,2,3,[4,5,6],[6,8,9]]

print(func(list11))