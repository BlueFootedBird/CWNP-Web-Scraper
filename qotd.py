import requests
from bs4 import BeautifulSoup
from datetime import date

#Grab the current date
today = date.today()
thisdate = today.strftime("%b-%d-%Y")

#Need to submit data to recieve the answer
myData = {'selectAnswer':'yes', 'answer':'a','submitAnswer':'Submit!'}

#Make the request to the website
html = requests.post('https://www.cwnp.com/qotd.php?', data = myData)

#Make soup
soup = BeautifulSoup(html.text, "html.parser")

#QUESTION
for headlines in soup.findAll('h3'):
    question = str(headlines.text.strip())

#CHOICES
form = soup.find('form', {'method':'post'})
inputs = form.findAll('label')
choices = []
for x in inputs:
    choice = str(x.find('input').get('value'))
    name = str((x.text).strip())
    choices.append(choice + ":" + name + "|")

#CORRECT ANSWER
answer = str((soup.find('span', {'class':'choice_correct'})).find('input').get('value'))

#EXPLANATION
for div in soup.findAll('div', {'class': 'answerDiv'}):
    explanation = ((div.text.strip()).split())[3:]
    explanation = " ".join(explanation)

#Write to a file
file1 = open(str(thisdate) + '.txt', 'w')
file1.writelines(question + "\n")
file1.writelines(choices)
file1.writelines("\n" + answer + "\n")
file1.writelines(explanation)




   