sales = [100,200,300,400]

salesgt250 = [i for i in sales if i>250]
print(salesgt250)

salesgt251 = filter(lambda x:x>251,sales)
print(list(salesgt251))

names = ["rama","rekha","jaya","sushma","nirma"]

rnames = list(filter(lambda x: "r" in x,names))
print(rnames)

#numbsers list
#palindrone numberes