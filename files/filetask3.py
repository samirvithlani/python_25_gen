file = open("./demo1.txt","r")
count=0
for i in file.readlines():
    words = i.split(" ")
    print(words)
    count+=len(words)

print(count)    
    
    
