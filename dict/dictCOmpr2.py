data = {1:["raj","parth","jay"],2:["amit","sumit","ajit"]}

#data1=  {i+1000:j for i,j in data.items()}
data1=  {i+1000:[k.upper() for k in j] for i,j in data.items()}
print(data1)


data = {1:["raj","bob","jay"],2:["amit","madam","naman"]}

#data2 ={i:j for i,j in data.items()}
data2 ={i:[k for k in j if k==k[::-1]] for i,j in data.items()}
print(data2)