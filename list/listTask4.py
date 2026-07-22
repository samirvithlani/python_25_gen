data = ["naman","jay","racecar","a","bob","jay","madam"]
palindromlist =[]

for i in data:
    if i == i[::-1]:
        palindromlist.append(i)

print(palindromlist)        

no =[1,2,3,4,5,6]
k =3
# print(no[-2:])
# print(no[:-2])
# print(no[-k:])
# print(no[:-k])
x = no[-k:]+no[:-k]
print(x)
#[5,6,1,2,3,4]
#k=3
#[4,5,6,1,2,3]


# a=[1,2,3]
# b = [4,5,6]

# x = a + b
# print(x)
