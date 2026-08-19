def safediv(func):
    
    def inner(no1,no2):
        print("inner called..")
        print("no1 = ",no1)
        print("no2 = ",no2)
        #func(no1,no2) #div()
        #func(100,2)
        #func(no1,no2)
        if(no2==0):
            print("can not divide by zer0")
        else:
            func(no1,no2)
    
    return inner    



@safediv
def div(a,b):
    print(a/b)
div(10,20) 
   