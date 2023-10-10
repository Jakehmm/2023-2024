# Get the input from the user
number = int(input("Type an integer: "))

# Determine if the number is divisible by both 2 and 3
if number % 2 == 0 and number % 3 == 0:
    print(f"The number {number} is divisible by both 2 and 3.")
else:
    print(f"The number {number} is not divisible by both 2 and 3.")