import calculator

number1 = input("Please enter first number: ")
number1 = int(number1)
number2 = input("Please enter second number: ")
number2 = int(number2)

calculator_object = calculator.CalculatorClass(number1, number2)
sum = calculator_object.add()
print(f"calculator_object = {calculator_object}")
print("Sum = ", sum)
print(f"Total operations = {calculator.CalculatorClass.op_count}")

sub = calculator_object.sub()
print("Sub = ", sub)
print(f"Total operations = {calculator.CalculatorClass.op_count}")

mul = calculator_object.mul()
print("Mul = ", mul)
print(f"Total operations = {calculator.CalculatorClass.op_count}")

div = calculator_object.div()
print("Div = ", div)
print(f"Total operations = {calculator.CalculatorClass.op_count}")
