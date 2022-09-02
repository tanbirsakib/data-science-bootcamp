x,y = map(int, input().split())
total_amount = 0

if x==1:
    total_amount = float(4.00) * y
elif x ==2:
    total_amount = float(4.50) * y
elif x ==3:
    total_amount = float(5.00) * y
elif x ==4:
    total_amount = float(2.00) * y
elif x ==5:
    total_amount = float(1.50) * y

print("Total: R$ %0.2f"%total_amount)
