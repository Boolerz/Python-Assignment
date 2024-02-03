def isPowerGreaterThan_5000(base, exponent):
    result = base ** exponent
    return result > 5000
# Example usage
base_number = 10
exponent_number = 10

if isPowerGreaterThan_5000(base_number, exponent_number):
    print(f"{base_number} raised to the power of {exponent_number} is greater than 5000.")
else:
    print(f"{base_number} raised to the power of {exponent_number} is not greater than 5000.")
    
def is_divisible_by_ten(number):
    return number % 10 == 0
# Example usage
num = 45

if is_divisible_by_ten(num):
    print(f"{num} is divisible by ten.")
else:
    print(f"{num} is not divisible by ten.")
    
def outer_fun(a, b):
  return inner_fun(a, b)

def inner_fun(c, d):

    return c + d

res = outer_fun(5, 10)

print(res)


def display(**kwargs):
    for i in kwargs:
        print(i)
display(emp="Kelly", salary=9000)