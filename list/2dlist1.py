sales = [[12,30],[23,67],[30,90]]
print(sales)
print(sales[0])
print(sales[0][1])

# #range loop
# for i in range(0,len(sales)):
#     #print(sales[i]) #list --> nested loop
#     for j in range(0,len(sales[i])):
#         print(sales[i][j],end=" ")
#     print()    
    
    
#for each

# for i in sales:
#     #print(i)  #i =->list
#     for j in i:
#         print(j,end=" ")  
#     print()    

for i,j in sales:
    print(i," ",j)