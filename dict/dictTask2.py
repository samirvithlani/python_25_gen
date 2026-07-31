data= {1:"naman",2:"raj",3:"bob",4:"jay"}

data1={}
#palindrom name 
#op
#data = {1:"naman",3:"bob"}

for i,j in data.items():
    if j == j[::-1]:
        data1[i]=j
print(data1)        

data = {1:"amit",2:22,3:33,4:"raj",5:None,6:["parth","sumit"],7:89}
#value data int float 

data ={2:22,3:33,7:89}