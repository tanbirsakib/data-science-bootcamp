num = int(input())
count = 0
for i in range(num, num+100):
    if i%2!=0:
        print(i)
        count = count+1
    if count>=6:
        break