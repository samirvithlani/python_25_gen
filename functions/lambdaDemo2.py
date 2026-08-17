#lambda with if

findmax = lambda a,b: a if a > b else b
print(findmax(100,20))

#pass 1 param and data type of param msut be stirng if yes return trur or false

flag = lambda x: True if type(x)== str else False
print(flag("java"))
print(flag(12))

#pass number in param check no is pos neg or zero return as string
#1-pos
#-1 -neg
#0 zero

cehckno = lambda no : "pos" if no>0 else("zero" if no==0 else "neg")
print(cehckno(-1))
print(cehckno(0))

#create funcion which will take string as argument retun false if string is "" empty
#else return in upper case 

data = lambda name : False if not name else name.upper()
print(data(""))
print(data("jay"))

#create lambda function take args as argument and return first element