# data = ()
# print(data)
# print(type(data))

data = ("amit","sumit","raj","amit")
print(data)
print(data[0])

#range
# for i in range(0,len(data)):
#     print(data[i],end=" ")

# for i in data:
#     print(i)    

#typeError: 'tuple' object does not support item assignment
#data[0] = "AMITA"


ind =data.index("sumit")
print("index = ",ind)

print(data.count("amit"))
data = ("amit","sumit","raj")
print(data)


marks = (21,22,23,21,20) #001
print(marks)
marksList = list(marks) #002
print(marksList)
marksList[2]=24 #002
marks  = tuple(marksList) #new ref # 003
print(marks)

a = (1,2,3)
b = (4,5,6)

c = a+ b
print(c)