#args

def getUsers(*args):
    print(args) #tuple
    #print(x)

#getUsers(123,23,45,x=10)    
getUsers(123,23)
    

def getSum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum    
        

x = getSum(10,20,30,40,50)
print(x)




def checkData(*args):
    flag = True
    for i in args:
        if type(i)!=int:
            flag = False
            break
    return flag    

x  =checkData(10,20,30,40,50)
print(x)


def checkDataAndsum(*args):
    flag= True
    sum=0
    for i in args:
        if type(i)!= int:
            flag = False
            break
        else:
            sum+=i
    if flag==True:
        return sum
    else:
        return flag        

x =checkDataAndsum(10,20,"ok",30)        
print(x)



# def getUpperList(*args):
#     upperlist =[]
#     for i in args:
#         upperlist.append(i.upper())
    
#     return upperlist        

# def getUpperList(*args):
#     return [i.upper() for i in args]

def getUpperList(*args):
    return [i.upper() for i in args if type(i)==str]


x = getUpperList("ram","amit","sumit",12)
print(x)
#["RAM","AMIT","SUMIT"]


def getPalindromes(*args):
    return [i for i in args if str(i) == str(i)[::-1]]


x = getPalindromes("naman",121,"raj","bob",22,23,"jay")
print(x)

                