
products = {"iphone18":200000,"laptop":90000,"table":12000,"bottle":500,"tshirt":600}


# please enter prod name
# if prod is exist: please enter qty:
# bill

pname = input("enter prodName: ")
prod = products.get(pname)
print(prod)
if(prod):
    print("product found")
    qty = int(input("enter qty:"))
    total = prod*qty
    print(total)
    
    