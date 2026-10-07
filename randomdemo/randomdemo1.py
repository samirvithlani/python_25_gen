import random

# print(random.random()) # 0 to 1
# print(random.randint(1,10))
print(random.randrange(1,100,10))
print(random.uniform(1,20))

colors = ["red","green","yellow","blue","pink","white"]
print(random.choice(colors))
print(random.choices(colors,k=2))
print(random.sample(colors,k=1))

#playlist

random.shuffle(colors)
print(colors)


random.seed(42)
x = random.randint(1,1001)
print(x)

