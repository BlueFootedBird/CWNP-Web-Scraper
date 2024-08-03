# WebScraping
I find wireless technology to be very cool. Back when I was interested in getting the CNWP certification (Certified Wireless Network Professional) I found they had a really cool feature where they'd as a question of the day and provide a word of the day. I found these to be helpful in building a Quizzlet. However, sometimes I'd forget to manually go to the site and copy/paste the answers and solutions. To make sure I wasn't missing out, I scripted a way to parse the QoTD and WoTD and save it to a file.

## WoTD
The word of the day is simple enough to parse, given it's simply raw HTML with a predictable format that hasn't changed since I began this project.

## QoTD
This is a bit trickier - In order to grab the correct answer from the website, you have to guess an answer first. Thus, the QoTD script sends an arbitrary answer to the question and then parses the response and saves it to a file. 

## Quiz
To use the information from the Question of the Day, I made a simple quiz in python that would parse a file, provide the user the question, and report if the answer was correct or false along with the corresponding reason for why. Wasn't fully flushed out, but it was just a fun project to do in my free time.