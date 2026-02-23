#AI chatbot

import datetime
import time

name=input("Welcome,Enter you name:")
presentHour=datetime.datetime.now().hour
if 5<=presentHour<=11:
    print("Good Morning",name)
elif 11<=presentHour<=17:
    print("Good Afternoon",name)
elif 17<=presentHour<=20:
    print("Good Evening",name)
else:
    print("Good Night",name)


print("Hello!,Welcome to Your AI ChatBot")
print("You can ask me basic question,Type 'bye' to exit from bot")

#Chatbot Memory creation {dictionary of responses}
responses = {
    "hello":"Hi,welcome.How can i help you?",
    "hii":"Hi,welcome.How can i help you?",
    "how are you":"I am very fine.Thankyou",
    "who are you":"I am Smart AI ChatBot",
    "motivate me":"Keep going,Every bug of your project makes you a better developer.",
    "happy":"Great to hear that."
}
#method/function to get response of chatbot
def getResponsesOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]


    return "I am not able to tell that yet.:("


#take user input
while True:
   userInput=input("Please ask your question:")
   if 'bye' in userInput.lower():
       break
   reply=getResponsesOfBot(userInput)
   print("Bot Response: ",reply)

   
