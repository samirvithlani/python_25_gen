set1 = {"ram","lakshman","seeta","krishna",}
set2 ={"krishna","arjun","sahdev","ram",}

x = set1.union(set2)
print(x)
x = set1 | set2
print(x)

x1= set1.intersection(set2)
print(x1)
x1 = set1 & set2
print(x1)

x2 = set1.difference(set2)
print(x2)
x2 = set2  - set1
print(x2)

x3 = set1.symmetric_difference(set2)
print(x3)

#boolean

flag = set1.issubset(set2)
print(flag)

flag = set1.issuperset(set2)
print(flag)


goa = {"amit","sumit","raj","kunal"}
mumbai = {"sumit","jay","neha","amit"}
pune = {"prit","sneha","amit","jay","kunal"}

#find person who have attended all cities ...,....
#find person who have  "" in mumbai and pune both but not goa
#find person who have  "" in pune and goa but not in mumbai