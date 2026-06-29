numbers = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in numbers]
cubes = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers]
greater_than_five = [x for x in numbers if x > 5]
double_values = [x * 2 for x in numbers]
half_values = [x / 2 for x in numbers]
print("original:",numbers)
print("squres:",squares)
print("cubes:",cubes)
print("even:",evens)
print("odd:",odds)
print("greater than 5:",greater_than_five)
print("double:", double_values)
print("half:",half_values)
print("total numbers:",len(numbers))
print("done!")