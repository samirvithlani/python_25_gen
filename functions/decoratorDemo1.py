#decortators are special python function which will take function as 
# argument and retuen inner function object
#decorators are use for change behaviour of function without changing code

def orderfood(func): #4 func == throw_party()

    def inner(): #7
        print("fun name....",func.__name__) #8
        print("ordering food...")  #9
        func() #10
    
    return inner  #5


@orderfood #3 #6 
def throw_party(): #2
    print("throwing party....") #11

throw_party()  #1



