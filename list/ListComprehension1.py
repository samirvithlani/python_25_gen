#[1,2,3,4,5]
data =[]

for i in range(1,6):
    data.append(i)

print(data)    

data1 = [i for i in range(1,6)]
print(data1)

marks = [21,22,23,19,18,24]
#updmarks =[]

# for i in marks:
#     updmarks.append(i+1)
# print(updmarks)    

updmarks = [i+1 for i in marks]
print(updmarks)

sales = [100,200,300,400,500]
salesp = [i*1.1 for i in sales]
print(salesp)

users = ["raj","jay","parth","neha","kunal"]
usersint=[]

for i in users:
    usersint.append(i[0])
print(usersint)    

usersint1 = [i[0] for i in users]
print(usersint1)