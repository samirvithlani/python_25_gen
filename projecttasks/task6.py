data = ["raj","jay","parth","kunal"]
data1 = [data[i] for i in range(len(data)-1,-1,-1)]
print(data1)
data1 = [data[i][::-1] for i in range(len(data)-1,-1,-1)]
#data2 = [i[::-1] for i in data1]
print(data1)

users = {"amit":["react","js","java","python"],"kunal":["js","python"]}

#set
print(set(users["amit"])&set(users["kunal"]))