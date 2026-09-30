# Marks Analyzer: Take 5 students' marks in a list.
# Print highest,
# lowest,
# average, 
# and how many passed (marks >= 35)

marks = [45,67,89,32,90]

print(max(marks))
print(min(marks))
print(sum(marks)/len(marks))

count=0
for i in marks:
    if i>35:
        count+=1

print(count)        