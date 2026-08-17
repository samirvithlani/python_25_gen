
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


def mul(*args):
    sum=1
    for i in args:
        sum*=i
    return sum


def sub(*args):
    sum=0
    for i in args:
        sum-=i
    return sum    


def calc(func,*args):
    ans = func(*args) #add(*args)
    print("ans",ans)

op = "+"
#match cas if else
match op:
    case "+":
        calc(add,1,2,3,4,5)
    case "*":
        calc(mul,1,2,3,4,5) 
    case "-":
        calc(sub,1,2,3,4,5)
                
            
            