def multiply_tuple(numbers):
    product = 1
    for num in numbers:
        product *= num
        return product
    
t = (2,3,4,5)

result = multiply_tuple(t)
print("product of tuple elements:",result)

