import os
import shutil

flag = os.path.exists("./th.txt")
print(flag)

#rename..
#os.rename("abcdkk.txt","user11.txt")

#delete..
if(os.path.exists("./files/employee.txt")):
    os.remove("./files/employee.txt")
else:
    print("file is not available...")    

#folder..
#os.mkdir("docs")  
#os.mkdir("./files/docs")  

#delete folder.
#os.rmdir("docs")

#shutil.rmtree("docs")





