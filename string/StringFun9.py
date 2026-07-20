fruits = "apple,banana,mango"
x = fruits.split(",")
print(x)

data = "a-b-c-d"
print(data.rsplit("-",2))

#join
print(",".join(x)) #string return 

email = "samir@gmail@.com"
print(email.partition("@"))
print(email.rpartition("@"))

text ="hi\nthis\nis\npython"
print(text.splitlines())
