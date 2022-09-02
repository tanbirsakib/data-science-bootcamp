# Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places after the comma, according to the formula:

# Distance = root_over((x1-x2)(x1-x2) - (y1-y2)(y1-y2))

# Input
# The input file contains two lines of data. The first one contains two double values: x1 y1 and the second one also contains two double values with one digit after the decimal point: x2 y2.

# Output
# Calculate and print the distance value using the provided formula, with 4 digits after the decimal point.
import math

X1,Y1=list(map(float,input().split()))
X2,Y2=list(map(float,input().split()))
Distance = math.sqrt(pow(X2-X1,2)+pow(Y2-Y1,2))
print("%0.4f"%Distance)