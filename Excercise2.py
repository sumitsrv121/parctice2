def reverse_list(arr):
    reverse = []

    while len(arr) > 0:
        reverse.append(arr.pop())
    return reverse


new_arr = list(range(1,11))
# print(reverse_list(new_arr))

new_arr.reverse()
print(new_arr)