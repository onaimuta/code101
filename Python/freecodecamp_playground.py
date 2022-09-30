# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return "Its is certain"
#     elif answerNumber == 2:
#         return "Its is decidedly so"
#     elif answerNumber == 3:
#         return "Yes"
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
#     elif answerNumber == None:
#         return "Spam"

# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)
import sys
feline = ["cats", "lions", "cheetahs", "leopards", "jaguars", "tigers"]
bovine = ["cattle", "bisons", "cape buffalos", "water buffalos", "spiral-horned antelopes"]
#print (feline [0])
print ("The " + feline [1] + " ate the " +bovine [2])
print (bovine.index ("water buffalos"))
bovine.insert (0, "eland")
# if "water buffalos" in bovine:
#     print("The " + bovine[0] + " are eaten by "+ feline[1]+".")
#    sys.exit()
del feline [0]
del bovine [5]
    # print ("Thats it!")
bovine.sort()
feline.sort()
# for a in range(5):
#     print(a)

print (bovine)
print (feline)





