# Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. If it is possible, calculate the perimeter of the triangle and print the message:


# Perimetro = XX.X


# If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:


# Area = XX.X

# Input
# The input file has tree floating point numbers.

# Output
# Print the result with one digit after the decimal point.

A, B, C = map(float, input().split())

if A+B>C and B+C>A and C+A>B:
    perimeter = A + B + C
    print("Perimetro = %.1f"%perimeter)
else:
    area_trapezium = ((A+B)/2)*C
    print("Area = %.1f"%area_trapezium)