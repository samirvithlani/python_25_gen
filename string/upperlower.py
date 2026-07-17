data = "Amit"
upperData =""
#a -->A
#97 --> - 32 = 65 -->A

for i in data:
    #print(chr((ord(i)-32)))
    if ord(i) >=97 and ord(i)<=122:
        upperData = upperData + chr(ord(i)-32)
    else:
        upperData = upperData+i    

print(upperData)    