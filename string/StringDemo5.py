data = "java is programming Lang"

#v ==index???
index = -1

for i in range(0,len(data)):
    # i =0 data [0] = j
    #  data[0] == "v" =>FALSE
    #  data[1] == "v" -->FALSE
    #  data[2] == "v" -->TRUE
    if data[i]=="a":
        #index = 2
        index =i
        

print(index)        