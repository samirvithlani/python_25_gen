# #read
# #file must be there to read..
# file = open("./demo1.txt","r")
# #data = file.read()
# data = file.read(1)
# print(data)
# file.close()


#read
#file must be there to read..
# file = open("./th.txt","r")
# #data = file.read()
# data = file.readline()
# print(data)
# file.close()

count =0
file = open("./th.txt","r")
#data = file.read()

while True:
    data = file.readline()
    print(data)
    count+=1
    if not data:
        break

file.close()

print(count)