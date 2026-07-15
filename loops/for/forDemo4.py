no = int(input("enter no :"))
fact=1
for i in range(no,0,-1):
    fact = fact*i
    print(f"{i} *",end=" ")

print(f" = {fact}")    
    