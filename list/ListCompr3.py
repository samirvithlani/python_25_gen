no = [1,2,-1,-90,21,100,-76,1,-89]
#["pos","pos","neg"...]
nolab = ["pos" if i>0 else "neg" for i in no]

# for i in no:
#     if i>0:
#         nolab.append("pos")
#     else:
#         nolab.append("neg")    

print(nolab)      


data = ["jay","ajay","raj","jay","parth","amit","parth","kunal"]
datavalid= ["valid" if len(i)>3 else "not valid" for i in data]
print(datavalid)


data = ["naman","jay","racecar","a","bob","jay","madam"]
dtalalb = ["palindrome" if i == i[::-1] else "not plaindrome" for i in data]
print(dtalalb)



no = [1,2,-1,-90,21,0,100,-76,1,-89]

nolab = ["pos" if i>0 else("zero" if i==0 else "neg") for i in no]
print(nolab)
  