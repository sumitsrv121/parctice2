class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

l1 = Laptop('HP','G70',90000)
print(l1.model_name)
print(l1.brand_name)
print(l1.price)