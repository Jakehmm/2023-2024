def main():
    # Print a new line, just for aesthetic
    print()
    # Solving 5 polynomial problems
    poly_1()
    poly_2()
    poly_3()
    poly_4()
    poly_5()


# Problem 1
def poly_1():
    # Value of x
    x = 5
    # Answer of the polynomial function when x is 5
    answer = (x ** 2) - (5 * x)

    # Solutions
    print("Question 1: ")
    print(f"x is {x}")
    print("p(x) = x^2 - 5x")
    print(f"p(x) = {x ** 2} - {5 * x}")
    print(f"p(x) = {answer}")
    is_zero(x, answer)


# Problem 2
def poly_2():
    # Value of x
    x = -2
    # Answer of the polynomial function when x is -2
    answer = (-2 * (x ** 3)) - (5 * (x ** 2)) + (3 * x) + 10

    # Solutions
    print("Question 2: ")
    print(f"x is {x}")
    print("p(x) = -2x^3 - 5x^2 + 3x + 10")
    print(f"p(x) = (-2 * {x ** 3}) - (5 * {x ** 2}) + (3 * {x}) + 10")
    print(f"p(x) = {-2 * (x ** 3)} - {5 * (x ** 2)} + {3 * x} + 10")
    print(f"p(x) = {answer}")
    is_zero(x, answer)


# Problem 3
def poly_3():
    # Value of x
    x = -3
    # Answer of the polynomial function when x is -3
    answer = (-1 * (x ** 4)) - (3 * (x ** 3)) - (2 * (x ** 2)) + 18

    # Solutions
    print("Question 3: ")
    print(f"x is {x}")
    print("p(x) = -x^4 - 3x^3 - 2x^2 + 18")
    print(f"p(x) = (-1 * {x ** 4}) - (3 * {x ** 3}) - (2 * {x ** 2}) + 18")
    print(f"p(x) = {-1 * (x ** 4)} - {3 * (x ** 3)} - {2 * (x ** 2)} + 18")
    print(f"p(x) = {answer}")
    is_zero(x, answer)


# Problem 4
def poly_4():
    # Value of x
    x = 4
    # Answer of the polynomial function when x is 4
    answer = (x ** 4) - (x ** 2) - (8 * x) - 16

    # Solutions
    print("Question 4: ")
    print(f"x is {x}")
    print("p(x) = x^4 - x^2 - 8x - 16")
    print(f"p(x) = ({x ** 4}) - ({x ** 2}) - (8 * {x}) - 16")
    print(f"p(x) = ({x ** 4}) - ({x ** 2}) - ({8 * x}) - 16")
    print(f"p(x) = {answer}")
    is_zero(x, answer)


# Problem 5
def poly_5():
    # Value of x
    x = -3
    # Answer of the polynomial function when x is -3
    answer = (x ** 3) + (5 * (x ** 2)) + (2 * x) - 12

    # Solutions
    print("Question 5: ")
    print(f"x is {x}")
    print("p(x) = x^3 + 5x^2 + 2x - 12")
    print(f"p(x) = ({x ** 3}) + (5 * {x ** 2}) + (2 * {x}) - 12")
    print(f"p(x) = ({x ** 3}) + ({5 * (x ** 2)}) + ({2 * x}) - 12")
    print(f"p(x) = {answer}")
    is_zero(x, answer)

# Determine if the number is zero or not; x is used for displaying its value
def is_zero(x, num):
    if num == 0:
        print(f"The answer is zero when x is {x}.\n")
    else:
        print(f"The answer is not zero when x is {x}.\n")


main()
