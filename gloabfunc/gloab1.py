nums = [11,-22,34,1,-678,9]
print(min(nums))
print(max(nums))

#ignore ng
print(min(nums,key=abs))
print(max(nums,key=abs))


#string
names= ["raj","zara","amit","parth","sumit"]
print(min(names))
print(max(names))

print(min(names,key=len))
print(max(names,key=len))

#users = [("Sam",23),("Raj",25),("Jay",26),("Amit",28)]
users = [(29,"Sam"),(25,"Raj"),(26,"Jay"),(28,"Amit")]
print(min(users))

#target pther index apart from default 0

ans = min(users,key=lambda x:x[1])
print(ans)
