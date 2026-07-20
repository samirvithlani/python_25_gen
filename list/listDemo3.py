numbers = [100,234,569,900,213,754,1000,1,90]
print(numbers)

#pop
removedElm = numbers.pop()
print("removing...",removedElm)
print(numbers)

#pop(index)
removedElm = numbers.pop(3)
print("removing...",removedElm)
print(numbers)

#remove

numbers.remove(213) #ValueError: list.remove(x): x not in list
print(numbers)

r = 10000
if r in numbers:
    numbers.remove(r)
else:
    print(f"{r} is not present..")    

print(numbers)    