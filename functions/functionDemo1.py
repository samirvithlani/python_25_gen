def test():
    print("test called...")

test()    

def add(a,b):
    print("add called..")
    return a+b

x = add(10,20)
print(x)
print(add(10,2000))