#find lcm of 2 numbers
#10 15 = 30
no1 = 10
no2 = 15
if no1>no2:
    i =no1
else:
    i = no2    
while(True):
    #1 % 10 == 0  1 % 15 = 0
    #2 % 10
    #10 % 10 == 0 and 10 % 15 ==0
    #15 % 10 ==0 and 15 % 15 ==0 
    if i % no1 ==0 and i % no2  ==0:
        break
    i+=1

print(i)    
        
    
    