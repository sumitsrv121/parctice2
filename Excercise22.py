class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.count_instance += 1

    @classmethod
    def get_class_instances(cls):
        return f'The {cls.__name__} has {cls.count_instance} instances'

    @property
    def get_details(self):
        return f'The name of person is {self.first_name} {self.last_name} and his age is {self.age}'


p1 = Person('A','B',23)
p2 = Person('c','B',28)
p3 = Person('X','B0',20)

print(Person.get_class_instances())
print(p2.get_details)
print(p2.__dict__)
