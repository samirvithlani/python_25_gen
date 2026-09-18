data  = {"id":1,"name":"raj","age":23}

file = open("user1.txt","a")
for i,j in data.items():
    file.write(f"{i} = {j} \n")
file.close()    