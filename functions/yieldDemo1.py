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

def getData(1,100,10):
    pass    