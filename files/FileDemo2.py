# file =  open("./users.txt","a")
# file.write("hi 1")
# file.close()

name = "raj"
age = 23

file = open("./users.txt","a")
file.write(f"name = {name} age = {age}\n")
file.close()

file2 = open("./files/employee.txt","a")
file2.write("hello")
file2.close()