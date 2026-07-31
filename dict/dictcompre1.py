#{1:1,2:2,3:3,4:4,5:5}
# data ={} #empty dict

# # for i in range(1,6):
# #     data[i]=i

# # print(data)    

#compre

data ={i:i for i in range(1,6)}
print(data)

#compr
#{1:1,2:4,3:9,4:16,5:25}
data = {i:i**2 for i in range(1,6)}
print(data)

data = ["amit","raj","parth","jay","amita","sumita"]
#without compre
datalen = {i:len(i) for i in data} #empty dict

# for i in data:
#     datalen[i] = len(i)

print(datalen)    


data = ["amit","raj","parth","jay","amita","sumita"]
#{a:"amit",r:"raj..."}

#datawithinit={} #empty dict
datawithinit={i[0]:i for i in data} 
# for i in data:
#     datawithinit[i[0]]=i

print(datawithinit)    



