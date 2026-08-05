#set comprehen

#{1,20}
x = {i for i in range(1,21)}
print(x)

#india ->remove duplicate caht using set com
#inda

data= "india"
#x = {i for i in data}
#print(x)
#x = "".join({"i","n","d","i","a"})
x = "".join({i for i in data})
print(x)


users = ["amit","sumit","raj","neha","amita","sumit","kunal"]
print(set(users))

#set = {"tima","timus",...} #comprehension

x1 = {i[::-1] for i in users}
print(x1)


#1 to 100  end 7

x3 = {i for i in range(1,101) if str(i).endswith("7")}
print(x3)


sent = ["hello world","programming language"]

sent1 = {i.replace(" ","") for i in sent}
print(sent1)

#["python","java","cpp"]



no = 25
print((int(no**0.5)**2) == no)

#(4**0.5)**2

x = {i for i in range(1,101) if (int(i**0.5)**2)==i}
print(x)