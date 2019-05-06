import math
class Laptop:
    discount = 10
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = self.brand_name+" "+self.model_name

    def apply_discount(self):
        return math.ceil(self.price - (self.discount*self.price)/100)

l1 = Laptop('HP','G70',99990)
print(l1.model_name)
print(l1.brand_name)
print(l1.price)
print(l1.laptop_name)
l1.discount = 50

print(l1.apply_discount())