class Count:
    count_instances = 0
    def __init__(self):
        Count.count_instances += 1


c1 = Count()
c2 = Count()
c3 = Count()
c4 = Count()
c5 = Count()
print(Count.count_instances)