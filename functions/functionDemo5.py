# def getusers(*args):
#     print(args)

# getusers(name="raj")    


#kwargs
# def getuserdetail(name,email):
#     print("name = ",name)
#     print("email = ",email)

# #getuserdetail("raj","raj@gmail.com")    
# getuserdetail(name="raj",email="raj@gmail.com")
    
def getuserdetails(**kwargs):
    print(kwargs)    

getuserdetails(name="amit",email="amit@gmail.com",age=24)    


#def getempdetail(**emps,*args): error
#    print()

def getEmpDetails(*args,**kwargs):
    print(kwargs)

getEmpDetails(12,22,33,"java",x="preeti")    


#create a function accept kwargs as argument, return only keys and print it

def demo(**kwargs):
    return kwargs.keys()

print(demo(x='a',y="b"))



#create function which will accept args as argument return true if all params are string else false

def checckData(*args):
    for i in args:
        if type(i)!=str:
            return False
    return True    

print(checckData("raj","parth","jay"))        
    


#create function which will accept kwarg as arhument return sum of all values check all valus must be int then sum
#if no  int return 0    

def getSum(**kwargs):
    sum=0
    for i,j in kwargs.items():
        if type(j)!= int:
            return 0
        else:
            sum = sum+j
    
    return sum


print(getSum(a=1,b=2,c=100,javaa=100,python='ok')) 


#create function accept args as argument return all param in upper cas use comprehension       

def getUsers1(*args):
    return [i.upper() for i in args]

print(getUsers1("ram","shyam"))
            
    

