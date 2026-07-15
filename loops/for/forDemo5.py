#0  1  1  2 3 5 8 13

a=0
b=1
sum=0
print(f"{a} {b}",end=" ")

for i in range(1,11):
    #    0 + 1
    #    1 + 1
    #    1 + 2
    #    2 + 3
    sum = a + b
    print(f"{sum}",end= " ") # 0 1 1 2 3 5
    #a = 1
    #a = 1
    #a=2
    a = b
    #b=1
    #b=2
    #b=3
    b = sum