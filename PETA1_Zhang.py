# Zhang, Jake Jiekai
# G10A
# Group 3

# Try to get 2 operands from the user and convert them into integer, if the user doesn't type an integer, display error message.
try:
    first_operand = int(input("Enter first operand (integer only): "))
    second_operand = int(input("Enter second operand (integer only): "))
except ValueError:
    print("Invalid operand.")

# Let the user case-insensitively choose operation.
operation = input("Enter desired operation (A = Addition, S = Subtraction, M = Multiplication, D = Division): ").strip().upper()

# Different cases of operations, if the user typed other things, display error message.
if operation == 'A':
    print(f"The sum of {first_operand} and {second_operand} is {first_operand + second_operand}")
elif operation == 'S':
    print(f"The difference of {first_operand} and {second_operand} is {first_operand - second_operand}")
elif operation == 'M':
    print(f"The product of {first_operand} and {second_operand} is {first_operand * second_operand}")
elif operation == 'D':
    print(f"The quotient of {first_operand} and {second_operand} is {first_operand / second_operand}")
else:
    print("Invalid operation.")