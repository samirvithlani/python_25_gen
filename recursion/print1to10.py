# def printno(n):
#     if n==0:
#         return
    
#     printno(n-1)
#     print(n)

# printno(10)    
    
# def countdigit(no):
#     if no==0:
#         return 0
#     return 1+countdigit(no//10)

# print(countdigit(123))


def sumofdigit(no):
    if no==0:
        return 0
    
    return no%10 + sumofdigit(no//10)

print(sumofdigit(123))