# You must make a program that read a float-point number and print a message saying in which of following intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. If the read number is less than zero or greather than 100, the program must print the message “Fora de intervalo” that means "Out of Interval".

# The symbol '(' represents greather than. For example:
# [0,25] indicates numbers between 0 and 25.0000, including both.
# (25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.

# Input
# The input file contains a floating-point number.

# Output
# The output must be a message like following example.

X = float(input())
if X>75 and X<=100:
    print("Intervalo (75,100]")
elif X>50 and X<=75:
    print("Intervalo (50,75]")
elif X>25 and X<=50:
    print("Intervalo (25,50]")
elif X>=0 and X<=25:
    print("Intervalo [0,25]")
else:
    print("Fora de intervalo")