bal =10000

def checkBal(func): #4 func == placeOrder
    
    def inner(): #7
        print("checking balanace !!!") #8
        if(bal>20000): #9
            func()
        else:#10
            print("not enough balacne..")     #11
    
    return inner #5        
    

@checkBal #3 #6
def placeOrder(): #2
    print("order has been placed..")

placeOrder() #1    