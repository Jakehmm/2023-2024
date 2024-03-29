# 3rd Grading PETA for Computer, Math, and Science
# G10A
# Group: Jake Jiekai Zhang, Junky Xavier Go, Kenneth Seco, Lawrence Xeno Wu
import math
import sys


# Keeps on asking the user until he/she typed '5'
while True:
    print('''Options:
1. Arc Length
2. Area of Sector
3. Lens Equation
4. Sum of Numbers
5. Exit''')
    option = input("Enter the number of your choice: ").strip()

    # Compute for arc length in cm
    if option == '1':
        x = int(input("Enter the radius(cm): "))
        y = int(input("Enter the central angle in degrees: "))
        print(f"Arc Length: {(x*math.pi) * (y/180)}cm")

    # Compute for area of sector in cm^2
    elif option == '2':
        x = int(input("Enter the radius(cm): "))
        y = int(input("Enter the central angle in degrees: "))
        print(f"Area of Sector: {(x*x*math.pi) * (y/360)}cm^2")

    # Compute for image distance in cm
    elif option == '3':
        x = int(input("Enter the Focal Length(cm): "))
        y = int(input("Enter the Object Distance(cm): "))

        # If the object is at the focal length, no image is formed
        if y == x:
            print("Image Distance: No image is formed.")
        else:
            print(f"Image Distance: {1 / ((1/x) - (1/y))}cm")
            print("(The answer might not be precise due to the \"floating point imprecision\" of computers)")

    # Compute for sum of numbers up to x
    elif option == '4':
        x = int(input("Enter a positive integer: "))
        y = 0

        # Summation of numbers from 0 to x
        for i in range(x + 1):
            y = y + i

        print(f"Sum of Numbers: {y}")

    # Exit the program
    elif option == '5':
        sys.exit("Thank you for using this program!")

    # Let the user to type again
    else:
        print("Invalid option. Please try again.")

    # Print a new line to separate the result of current loop 
    # and the options of next loop
    print()
    