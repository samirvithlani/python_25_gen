nums = [11,-22,34,1,-678,9]
print(min(nums))
print(max(nums))

#ignore ng
print(min(nums,key=abs))
print(max(nums,key=abs))


#string
names= ["raj","zara","amit","parth","sumit"]
#print(min(names))
#print(max(names))

#print(min(names,key=len))
#print(max(names,key=len))

#users = [("Sam",23),("Raj",25),("Jay",26),("Amit",28)]
users = [(29,"Sam"),(25,"Raj"),(26,"Jay"),(28,"Amit")]
#print(min(users))

#target pther index apart from default 0

ans = min(users,key=lambda x:x[1])
#print(ans)


#sum
nums = [1,2,3,4,5]
print("sumn....",sum(nums))

#sum func
#do sum of only evn no:

evnsum = sum(i for i in nums if i %2 ==0)
print(evnsum)


sales = [100,200,23,400,50,67,900]

sum300 = sum(i for i in sales if i>300)
print(sum300)

#square of sum
data = [1,2,3,4,5]
sqsum = sum(i**2 for i in data)
print(sqsum)

#cube sum

data= [1,5,3]
cubesum = sum(i**3 for i in data)
print(cubesum)


#
data = ["raj","parth","ok"]

charsum = sum(len(i) for i in data)
print(charsum)

#dict:
students = [
    {"id":1,"name":"raj","marks":23},
    {"id":2,"name":"jay","marks":25},
    {"id":3,"name":"parth","marks":20}
]

#res = sum(i["name"] for i in students)
res = sum(i["id"] for i in students)
print("marks",res)
