def power(base, exponent):
    result - 1
    for i in range(exponent):
        result *= base
    return result

base = int(input("enter the base number: "))
exponent = int(input("enter the base number: "))


print("result:", power(base, exponent))