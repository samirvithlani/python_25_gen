sp = int(input("enter sp :"))
ep = int(input("enter ep :"))

#sp = 10
#ep = 20

#sp = 20
#ep = 10 #20 19 18n 17 16...10

i=1
# 10<20
if ep<sp:
    i=-1

#10 21 1
#20,10-1,-1
for i in range(sp,ep+i,i):
        print(i)


#sum of numbers        