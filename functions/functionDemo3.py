def getUserDetail(name,age,salary):
    print(f"age = {age} salary = {salary} name = {name} ")

#getUserDetail("raj",23,34500)    
#getUserDetail(23,34500,"raj")    

#keyword argument...
getUserDetail(age=23,name="raj",salary=34500)
#getUserDetail(age=23,name="raj",34500) #error
#getUserDetail("raj",salary=23000,age=21)
#getUserDetail("raj",age=23,name="ram")