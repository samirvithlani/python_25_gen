data= {"Guj":"GNR","Mah":"Mumbai","Goa":"Panji","Guj":"Ahm"}
print(data)

data["punjab"] = "chandigadh"
print(data)
data.update({"up":"lucknow","mp":"bhopal"})
print(data)


#key-->value remove
removedElm = data.pop("Goa")
print("removing...",removedElm)
print(data)

remvoed = data.popitem() #last key value pair..
print("removing..",remvoed)
print(data)