data = "hi this is ahmedabad"

# #@
# if "a" in data:
#     print("yes")
# else:
#     print("not")    
count=0
# for i in data:
#     if i == "a" or i =="e" or i =="i" or i == "o" or i =="u":
#         count+=1

for i in data:
    #i in "aeiou"
    if i in "aeiouAEIOU":
        count+=1

print(count)        
