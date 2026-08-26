def getData(**kwargs):
    print(kwargs) #dict


getData()    
getData(name="raj",age=23)


#error
# def getData1(**kwarg,x):
#     print()

def getData2(x,**kwargs):
    print(x)
    print(kwargs)
    
getData2(10,name="raj")    
getData2(x=100,name="java")


def getData3(*args,**kwargs):
    print(args)
    print(kwargs)

getData3(10,20,"java",name="python")    