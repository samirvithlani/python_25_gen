#lambda function

#withou return type without argumen
# def test():
#     print("test")
# test()    

test = lambda :print("test")
test()

#with arg no return type..
# def add(a,b):
#     print(a+b)
# add(10,20)    

add = lambda a,b:print(a+b)
add(100,200)

#with argument with return type
# def fullname(fname,lname):
#     return f"{fname}  {lname}"

# x = fullname("virat","kohli")
# print(x)

fullname = lambda fname,lname : f"{fname} {lname}"
x = fullname("ms","dhoni")
print(x)
print(fullname("rohit","sharma"))


