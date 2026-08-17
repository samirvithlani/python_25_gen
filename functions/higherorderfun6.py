

def insta(**kwargs):
    print("insta login..",kwargs)

def snap(**kwargs):
    print("snap login..",kwargs)    

def facebook(**kwargs):
    print("facebook login..",kwargs)



def social(func,**kwargs):
    func(**kwargs)


social(snap,username="abcd",password="@123")    
social(facebook,email="whatever.com",password="abcd")