import sys


def main():
    while True:
        choice = input("""
Choose what you want for trapezoid
(P = Perimeter,
A = Area,
B = Base,
E = Exit the program): """).strip().upper()
        if choice == 'P':
            p = perimeter()
            print(f"Perimeter = {p} cm")
        elif choice == 'A':
            a = area()
            print(f"Area = {a} cm^2")
        elif choice == 'B':
            b = base()
            print(f"Base = {b} cm")
        elif choice == 'E':
            sys.exit("Thank you for using this program!")
        else:
            print("Invalid. Please try again.")


def perimeter():
    base_1 = float(input("Enter the first base of trapezoid (in cm): "))
    base_2 = float(input("Enter the second base of trapezoid (in cm): "))
    leg_1 = float(input("Enter the first leg of trapezoid (in cm): "))
    leg_2 = float(input("Enter the second leg of trapezoid (in cm): "))
    print("Formula: Perimeter = base 1 + base 2 + leg 1 + leg 2")
    return base_1 + base_2 + leg_1 + leg_2


def area():
    area = lambda a, b, h : ((a+b) / 2) * h 
    a = int(input("Enter first base: "));
    b = int(input("Enter second base: "));
    h = int(input("Enter height: "));
    print("Formula: Area = [(base 1 + base 2) / 2] * height")
    return area(a,b,h)


def base():
    area = float(input("Enter the area of trapezoid (in cm^2): "))
    h = float(input("Enter the height of trapezoid (in cm): "))
    base_1 = float(input("Enter the first base of trapezoid (in cm): "))
    base_2 = 2 * (area / h) - base_1
    print("Formula: Base = 2 * (area / height) - base 1")
    return base_2


main()
