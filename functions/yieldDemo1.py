# def demo():
#     return "hello"
#     return "hi"

# d = demo()
# print(d)
def demo():
    yield 1
    yield 2
    yield 3

d = demo()
#print(d)    
# print(next(d))
# print(next(d))
# print(next(d))

for i in d:
    print(i)

#1,100,10
def getData(start,end,batch_size):
    #1<=100
    while start<=end:
        #91+10-1 = 100
        #101
        batch_end = start+batch_size-1
        #100>100
        if(batch_end>end):
            batch_end = end

        yield range(start,batch_end+1)
        start = batch_end +1 #91,101

# d = getData(1,100,10)
# print(list(next(d)))
# print(list(next(d)))

d = getData(1,100,10)
for i in d:
    print(list(i))
    
  