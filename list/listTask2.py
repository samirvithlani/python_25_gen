data = ["jay","ajay","raj","jay","parth","amit","parth","kunal"]
uniqueData =[]
duplicate =[]

for i in data:
    if i not in uniqueData:
        uniqueData.append(i)
    else:
        duplicate.append(i)        

print(uniqueData)        
print(duplicate)