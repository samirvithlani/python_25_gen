# file = open("./th.txt","r")
# #data = file.read()
# data = file.readlines()
# print(data)
# file.close()


file = open("./th.txt","r")
#data = file.read()

for i in file.readlines():
    print(i,end="")

file.close()
