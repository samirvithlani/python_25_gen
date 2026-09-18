#if file opens with w mode and it is not present it will create and write..
#here file is variable not any keyword
file = open("demo1.txt","w")
#write..
file.write("Hello this is from Python")
file.close()

file2 = open("../demo2.txt","w")
file2.writelines(["hi","this","is","india"])
file2.close()
