l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

func=lambda *args:list(map(lambda i : sum(i)/len(i), zip(*args)))

print(func(l1,l2,l3))