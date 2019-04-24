def func(list1,list2):
    output = []

    for x in list1:
        if x in list2 and (list2.count(x) > 1 or x not in output):
            output.append(x)
        else:
            pass

    return output


new_list1 = [1,2,3,4,1,2]
new_list2 = [1,2,3,4,5,2]

print(func(new_list1,new_list2))

