try:
    num1, num2 = eval(input("enter two numbers, separated by coma: "))
    result = num1 / num2
    print("result is",result)
#using multiple except block for different type errr

except ZeroDivisionError:
    print("division by error is error")

except SyntaxError:
    print("coma is missing")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what happend")