file = open("th.txt","r")
data = file.readline()
print(data)
file.close()

words = data.split(" ")
print(words)
print(len(words))