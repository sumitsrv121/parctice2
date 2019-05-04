def to_power(x):
    def calculate_power(n):
        return n**x
    return calculate_power

var = to_power(2)
print(var(9))