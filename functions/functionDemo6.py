def data():
    print("dataa...")

#data()    
x = data
#x == data()
x()

def add(a,b):
    print("add called..")
    return a+b

y = add #add -->y -->add()
ans = y(10,20)
print(ans)


# create a function whc=ich will take args as argumentand return summ of args 
# store funciton add in variable and call it like above 

def test(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

p = test   
x1 =p(1,2,3,4,5)
print(x1)