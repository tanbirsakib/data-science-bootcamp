# Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

# Input
# The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

# Output
# Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example

val = float(input())
notes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')

for n in notes:
    quotient = int((val / n))
    print(f'{quotient} nota(s) de R$ {n:.2f}')
    remainder = val % n
    val = remainder
print('MOEDAS:')
for m in coins:
    quotient = int(round(val,2) / m)
    print(f'{quotient} moeda(s) de R$ {m:.2f}')
    remainder = round(val,2) % m
    val = remainder