from calc_package import cal_module


i = 0
while i < 5:
    num1 = int(input("please enter first number: "))
    num2 = int(input("please enter second number: "))

    if num2 == 0:
        print("your second number is a 0 and you cant divide by a 0!")

    else:
        print(cal_module.add(num1, num2))
        print(cal_module.sub(num1, num2))
        print(cal_module.mul(num1, num2))
        print(cal_module.div(num1, num2))
        i += 1

#text = f"(Number1: {num1}) {operation} (Number2: P={num2}) = {result}"
'''
This is a multi line comment
'''
