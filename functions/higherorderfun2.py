def upi(amount):
    print(f"transaction done for amount {amount} with UPI")

def card(amount):
    print(f"transaction done for amount {amount} with CARD")    
    
def wallet(amount):
    print(f"transaction done for amount {amount} with WALLET")    


def payment(func): #func == upi()
    print("payment called...")    
    print(func)
    func(1000)


payment(upi)  
 