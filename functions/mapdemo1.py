#list
nos = [1,2,3,4,5]
nos2=[]

for i in nos:
    nos2.append(i**2)

print(nos2)    

#compre

nos3 = [i**2 for i in nos]
print(nos3)

#map

x = map(lambda x:x**2,nos)
print(x) #object..
print(list(x))



names = ["raj","parth","amit"]
uppername =[]
for i in names:
    uppername.append(i.upper())
print(uppername)    

#compre
uppername1 = [i.upper() for i in names]
print(uppername1)
#map
uppername2 = map(lambda x:x.upper(),names)
print(tuple(uppername2))

# uppername2 = list(map(lambda x:x.upper(),names))
# print(uppername2)


#sales.
sales = [100,200,300,400]

salesp = [i*1.1 for i in sales]
print(salesp)

salesp1 = map(lambda x:x*1.1,sales)
print(list(salesp1))


