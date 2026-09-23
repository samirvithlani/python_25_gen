import os
import shutil

#copy file

#if src file exists
#and at dest folder file must not exists..
#shutil.copy("users.txt","./files/userscopy.txt")


#move
#shutil.move("users.txt","./files/moveuser.txt")

#copy folder

#shutil.copytree("doc","./files/doc")
#shutil.move("doc","./files/doc1")


#list all items

items = os.listdir("basics")
print(items)
