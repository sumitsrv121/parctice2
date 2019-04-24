def odd_even_list(num):
    odd = []
    even = []
    new_num = []
    for x in num:
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    new_num.append(odd)
    new_num.append(even)
    return new_num


number = list(range(1,21))
print(odd_even_list(number))