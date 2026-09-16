#zip
a = [1,2,3]
b = [11,22,33]
c = [100,200,300]

for i,j,k in zip(a,b,c):
    print(i,j,k)

data = {}
for i,j in zip(a,b):    
    data[i]=j

print(data)    


# data = [5 ,4 ,3,-1,12]

# closest to zero

# ans  = -1


students = [
    ("Rahul", 78),
    ("Amit", 92),
    ("Neha", 85),
    ("Priya", 95),
    ("Raj", 88)
]


print(max(students,key=lambda x:x[1])[0])


nums = [-15, 4, -2, 9, -7, 3]

names = ["Rahul", "Amit", "Neha", "Priya"]
marks = [78, 92, 85, 95]

x =list(zip(names,marks))
print(x)
print(min(x,key=lambda x:x[1])[0])

movie = ["titanic","mirzapur","toxic","dhurandhar","aamir khan"]
prices = [100, 250, 80, 450, 120]
budget = 200

ans = min(prices,key=lambda x:abs(x-budget))
print(ans)


ans2 = min(list(zip(movie,prices)),key=lambda x:abs(x[1]-budget))[0]
print(ans2)


products = [
    ("Laptop", 55000),
    ("Phone", 30000),
    ("Tablet", 20000),
    ("Watch", 15000),
    ("Headphone", 5000)
]

budget = 25000

#budget ke anadr ki most exp porduct

# list comprej

# max

avl = [i for i in products if i[1]<=budget]
print(avl)

avl2 = max(avl,key= lambda x:x[1])
print(avl2)
