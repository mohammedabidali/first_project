import json

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as exception_zer:
        return none
    else:
        print("The division was perfomed successfully")
    finally:
        print("This is the final block of code")
    return result

i = 0
f = open("results.txt", "w")
while i < 2:

    data_dict = {"number1": None, "number2" : None, "sum": None, "sub": None, "mul": None, "div": None}

    num1 = int(input("please enter first number: "))
    data_dict["number1"] = num1
    num2 = int(input("please enter second number: "))
    data_dict["number2"] = num2

    sum = add(num1, num2)
    data_dict["sum"] = sum
    sub = sub(num1, num2)
    data_dict["sub"] = sub
    mul = mul(num1, num2)
    data_dict["mul"] = mul
    div = div(num1, num2)
    data_dict["div"] = div

    print(sum)
    print(sub)
    print(mul)
    print(div)



    #results = {"sum ": sum, "sub ": sub, "mul ": mul, "div ": div}

    #with open("calculator.json", "a") as file:
        #json.dump(results, file)  # use json load
    i += 1
with open("calculator.json", "a") as file:
    json.dump(data_dict, file)  # use json load
