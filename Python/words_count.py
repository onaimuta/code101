file = open("AIC_Tasks_220922.txt", "r")
read_data = file.read()
#print (read_data) # reads text to terminal
per_word = read_data.split()
#print (per_word)
print ("Word Count:", len(per_word))
#print(len(text.split()))
word_list = (per_word)
#print (word_list)
longest_word = max (word_list, key = len)
print ("The longest word in the document is: " + longest_word)
shortest_word = min (word_list, key = len)
print ("The shortest word in the document is: " + shortest_word)

