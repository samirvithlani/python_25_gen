sent = "hi this is india and india is my country"
words  = sent.split()
print(words)

count={} #{}
for i in words:
    #i = hi
    #{hi:1...,india,india}
    count[i]=count.get(i,0)+1

print(count)    