from multiprocessing.sharedctypes import Value
from random import choices

#Open a file
myFile = open("qMay-04-2022.txt", 'r')

#Print values
Values = myFile.readlines()

#Grab the question
question = Values[0]
print(question)

#Grab the potential answers into a list
choices = Values[1].split('|')
for i in range(len(choices)):
    print(choices[i])

#Grab the correct answer
correctAnswer = Values[2].strip()
answer = input("Enter the correct value: ")

if(correctAnswer == 'd' and answer == 'd'):
    print("\nCorrect!\n")

if(correctAnswer != answer):
    #Grab the explanation
    explanation = Values[3]
    print("\nWrong!\n" + explanation)