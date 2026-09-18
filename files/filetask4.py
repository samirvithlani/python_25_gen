file = open("./demo1.txt","r")

# palindoromelist =[]
# for i in file.readlines():
#     words = i.split()
#     #print(words)
#     for x in words:
#         if(x == x[::-1]):
#             palindoromelist.append(x)

# print(palindoromelist)            

data = file.read()
x = data.split()
p1 = [i for i in x if i==i[::-1]]
print(p1)

