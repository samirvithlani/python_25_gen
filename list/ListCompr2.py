sales = [1,2,45,6,89,12,4,56,78,90,65,33,3,56,7,5,23]
evensales = [i for i in sales if i %2==0]

# for i in sales:
#     if i %2==0:
#         evensales.append(i)

print(evensales)    

data = ["naman","jay","racecar","a","bob","jay","madam"]

palindromnames = [i for i  in data if i == i[::-1]]    
print(palindromnames)

filtdata = [i for i in data if len(i)>4]
print(filtdata)


students = ["neha","shivani","priya","amita","krish","jwala","mukhi"]
#students1 = [i for i in students if i[-1]=="a"]
#students1 = [i for i in students if i.endswith("a")]
#print(students1)
students2 = [i for i in students if "i" in i]
print(students2)
