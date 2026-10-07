import random as r

choice_data = ["rock","paper","scissor"]

user = input('enter your choice :').lower()
comp = r.choice(choice_data)
print("computer choice",comp)
if user == comp:
    print("tie")
elif (comp=="paper" and user =="rock") or (comp=="scissor" and user=="paper")   or  (comp=="rock" and user=="scissor"):
    print("computer win")
else:
    print("user win")    
    

