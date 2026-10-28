import zipfile

# with open("user11.txt","r") as file:
#     data = file.read()
#     print(data)
#     #no need close..


with zipfile.ZipFile("notes.zip","w") as z:
    z.write("th.txt")
    z.write("t1.py")

print("zip created..")    