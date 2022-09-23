#Python Functions

sentence = input ("Enter Sentence: ")
longest = max (sentence.split(), key=len)
print (longest)
print (len(longest))

sentence = input ("Enter Sentence: ")
shortest = min (sentence.split(), key=len)
print (shortest)
print (len(shortest))

