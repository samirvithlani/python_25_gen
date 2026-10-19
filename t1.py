# 5. Unique Hashtag Generator
# Given a sentence, extract all unique words and convert them into lowercase hashtags using a set comprehension.
Example = "Python is fun and Python is powerful"

x = "#".join(set(Example.split(" ")))
print(x)

x = " ".join({'#' + i for i in Example.split(" ")})
print(x)
