data= {"Guj":"Ahm","Mah":"Mumbai","Goa":"Panji"}
print(data)

#key --> value..
print(data["Guj"]) #error if key is not there
print(data.get("Goaa")) #if key is not present it will return None

k = data.keys()
print(k)
v = data.values()
print(v)

kv = data.items()
print(kv)

for i,j in data.items():
    print(i,"",j )
