# ead three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

# Input
# The input contains three integer numbers.

# Output
# Present the output as requested above.

x, y, z = map(int, input().split())
ascending = [x, y, z]
if x<y and x<z:
    ascending[0] = x
    if y<z:
        ascending[1] = y
        ascending[2] = z
    else:
        ascending[1] = z
        ascending[2] = y    
if y<x and y<z:
    ascending[0] = y
    if x<z:
        ascending[1] = x
        ascending[2] = z
    else:
        ascending[1] = z
        ascending[2] =x
if z<x and z<y:
    ascending[0] = z
    if x<y:
        ascending[1] = x
        ascending[2] = y
    else:
        ascending[1] = y
        ascending[2] = x

print(f"{ascending[0]}\n{ascending[1]}\n{ascending[2]}")
print(f"\n{x}\n{y}\n{z}")


# print(ascending)