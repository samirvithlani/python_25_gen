#default argument 
def avg(a=0,b=0,c=0):
    print("avg called..")
    print(a)
    print(b)
    print(c)
    return (a + b + c ) / 3

avg()
x = avg(100)
print(x)