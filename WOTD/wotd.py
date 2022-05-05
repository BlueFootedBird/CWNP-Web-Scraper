import requests
from bs4 import BeautifulSoup
from datetime import date
import re

#Grab the current date
today = date.today()
thisdate = today.strftime("%b-%d-%Y")

#Need to submit data to recieve the answer
myData = {'selectAnswer':'yes', 'answer':'a','submitAnswer':'Submit!'}

#Make the request to the website
html = requests.get('https://www.cwnp.com/wotd.php')

#Make soup
soup = BeautifulSoup(html.text, "html.parser")

#Get the term
for headlines in soup.find('h2'):
    term = headlines.text.strip()

#Get the definition
for div in soup.find('div', {'id': 'content'}):
    definition = str(((div.text).strip()))
    #Get rid of the term showing up in the answer (Gives it away)
    definition = (re.sub(term, '[____]', definition, flags=re.IGNORECASE)).split()

#Clean up the definition
blacklist = {'-', ' '}
while definition[0] in blacklist:
    definition.pop(0)
definition = " ".join(definition)

#Write to a file
wotdFile = open("w" + str(thisdate) + ".txt", 'w')
wotdFile.writelines(term + "\n")
wotdFile.writelines(definition + "\n")
