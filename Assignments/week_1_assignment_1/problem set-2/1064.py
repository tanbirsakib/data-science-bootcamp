counters = 0
sum_positive = 0
for i in range(6):
    num = float(input())
    if num>0:
        counters+=1
        sum_positive = sum_positive+ num
avg = sum_positive/counters
print("%d valores positivos"%counters)
print(f"{avg:0.1f}")