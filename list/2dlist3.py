sales = [[12,30],[23,67],[30,90]]
sales1d =[]
for i in sales:
    sales1d.extend(i)
    # for j in i:
    #     sales1d.append(j)

print(sales1d)        

#[1,2,3,0,2,3,6,7,3,0,9,0]        
sales2=[]
for i in sales:
    for j in i:
        for k in str(j):
            sales2.append(int(k))

print(sales2)            

#flattn list
#data = [1,[2,[3,[4,[5]]]]]       

#[1,2,3,0,2,3,6,7,3,0,9,0]   :in          
#op:[[12,30],[23,67],[30,90]]