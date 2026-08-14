# def getUsers(user):
#     print(user)


# getUsers("raj")    
   
#args it is not keyword   
def getUsers(*args):
    print(args)

getUsers("raj","parth")    
getUsers()
getUsers("raj","parth",11,23,[])    

def getemps(*args,x):
    print(args)
    print(x)
#getemps("a","b","c","d",12)    
getemps("a","b","c","d",x=12)    


def getBooks(x,*args):
    print(x)   
    print(args)

getBooks(123,"ok","km")    
getBooks(100)
    