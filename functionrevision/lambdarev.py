#single line function lamba

x = lambda:print("hello")
x()

x1 = lambda a,b:print(f"a = {a} b = {b}")
x1(100,"java")

x3 = lambda a:a**2
ans = x3(10)
print(ans)
print(x3(9))


x4 = lambda name1,name2 : name1 + " "+ name2
print(x4("virat","kohli"))

#if else

x5 = lambda no : "even" if no %2 ==0 else "odd"
print(x5(101))


x6 = lambda name: name if name ==name[::-1] else None
print(x6("naman"))
