a, b = map(int, input().split())
sum_odd=0
if b>a:
    temp = a
    a = b
    b = temp
for i in range(b,a):
    if i%2!=0:
        sum_odd = sum_odd + i
print(sum_odd)


