from functools import reduce

numbsers = [1,2,3,4,5]

ans = reduce(lambda x,y:x+y,numbsers)
print(ans)