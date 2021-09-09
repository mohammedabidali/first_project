
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
    num1 = int(input("please enter first number: "))
    num2 = int(input("please enter second number: "))

    if num2 == 0:
        print("your second number is a 0 and you cant divide by a 0!")
    else:
        print(add(num1, num2))
        print(sub(num1, num2))
        print(mul(num1, num2))
        print(div(num1, num2))
        i += 1
    f = open("results.txt", "a")
    f.write(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)) + "\n")
    f.write(str(num1) + " - " + str(num2) + " = " + str(sub(num1, num2)) + "\n")
    f.write(str(num1) + " * " + str(num2) + " = " + str(mul(num1, num2)) + "\n")
    f.write(str(num1) + " / " + str(num2) + " = " + str(div(num1, num2)) + "\n")
    f.close()
#text = f"(Number1: {num1}) {operation} (Number2: P={num2}) = {result}"
