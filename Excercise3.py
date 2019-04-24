def reverse_string(arr):
    new_list = []
    for x in arr:
        new_list.append(x[::-1])
    return new_list


fruits = ['apple','mango','orange','pears','guava','pomegranate','raspberry pie']
print(reverse_string(fruits))