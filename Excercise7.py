
def func(num):
    cubes = {}

    for i in range(1,num+1):
        cubes[i] = i**3

    print(cubes)

func(10)