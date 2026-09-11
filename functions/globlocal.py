x = 10 #glob vairble

def change():
    global x
    print(x)
    x = 100 #local
    print(x)

print("....",x)    
change()    
print("....",x)    