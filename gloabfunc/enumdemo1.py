names =["raj","parth","jay"]

#rnage
for i in range(0,len(names)):
    print("index",i,"elm",names[i])
    
for i in names:
    print(i)    
    
#enumrate

for index,elm in enumerate(names,start=1001):
    print("index ",index,"elm",elm)    
    