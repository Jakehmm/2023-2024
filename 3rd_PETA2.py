# 3rd Grading PETA for Computer, Math, and Science
# G10A
# Group: Jake Jiekai Zhang, Junky Xavier Go, Kenneth Seco, Lawrence Xeno Wu
import math
import sys


# Keeps on asking the user until he/she typed '4'
while True:
    print('''Options:
1. Arc Length
2. Lens Equation
3. Sum of Numbers
4. Exit''')
    option = input("Enter the number of your choice: ").strip()

    # Compute for arc length in cm
    if option == '1':
        x = int(input("Enter the radius(cm): "))
        y = int(input("Enter the angle in degrees: "))
        print(f"Arc Length: {(x*math.pi) * (y/180)}cm")

    # Compute for image distance in cm
    elif option == '2':
        x = int(input("Enter the Focal Length(cm): "))
        y = int(input("Enter the Object Distance(cm): "))

        # If the object is at the focal length, no image is formed
        if x == y:
            print("Image Distance: No image is formed.")
        else:
            print(f"Image Distance: {1 / ((1/x) - (1/y))}cm (The answer might not be precise due to the \"floating point imprecision\" of computers)")

    # Compute for sum of numbers up to x
    elif option == '3':
        x = int(input("Enter a positive integer: "))
        y = 0

        # Summation of numbers from 0 to x
        for i in range(x + 1):
            y = y + i

        print(f"Sum of Numbers: {y}")

    # Exit the program
    elif option == '4':
        sys.exit("Thank you for using this program!")

    # Let the user to type again
    else:
        print("Invalid option. Please try again.")

    # Print a new line to separate the result and the options of next loop
    print()