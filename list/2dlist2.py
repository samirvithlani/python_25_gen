sales = [[12,30],[23,67],[30,90]]
#sales = [["MON",12,30],["TUE",23,67],["WED",30,90]]
#sales1 = [,,]
totalSales=[]
sum=0
for i in sales:
    for j in i:
        sum = sum+j
    totalSales.append(sum)
    sum=0

print(totalSales)    


sales = [["MON",12,30],["TUE",23,167],["WED",30,90]]
#TUE
max =0
day = None
for i in sales:
    #["MON,12,30]
    #["MON,23,167]
    #["WED",30,90]
    for j in i[1:]: #[12,30] [23,167] [30,90]
        print(j,end=" ")
        sum = sum +j #[12+30] [23+167] [120]
    print("sum = ",sum)   #42
    if(sum>max):
        max = sum #max= 24 max = 190
        day = i[0] #day =MON # TUE
    sum=0
    

print(max)    
print(day)
    
    
    
    

