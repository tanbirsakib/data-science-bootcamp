num = int(input())

if num> 5 and num<2000:
    for i in range(1, num+1):
        if i%2==0:
            square = i*i
            print(f"{i}^2 = {square}")