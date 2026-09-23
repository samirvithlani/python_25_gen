import os

foldername = input("enter folder name")

if(os.path.exists("D:/"+foldername)):
    print("folder is exsists enter file name:")
    filename = input("enter file name")
    if(os.path.exists("D:/"+foldername+"/"+filename)):
        os.remove("D:/"+foldername+"/"+filename)
    else:
        print("file not exists.")    
else:
    print("folder is not exists")
    