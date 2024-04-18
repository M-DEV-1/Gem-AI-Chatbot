from config import key

import requests # web library
from mic_to_test import mic1

def chat1(chat):
    messages = [] #list which contains all the message
    
    system_message = "You are an AI bot, your name is Gem. You were trained by Google and created by M-Dev-1." #first instruction
    
    message = { "role" : "user", "parts": [{"text": system_message+" "+chat}]}  #system message and chat are sent to AI, chat is our input
    
    messages.append(message)
    
    data = { "contents": messages}
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key #url of API + API key
    
    response = requests.post(url,json=data)
    
    t1 = response.json() #json is JavaScript Object Notation. It is a lightweight format for storing and transporting data.
    #print (t1)
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)
    
chat = mic1()
#chat = input("Enter the Query: ")
#chat = "who is MS Dhoni" 

#{'candidates': [{'content': {'parts': [{'text': "Hello, I am Jarvis, your AI assistant"}]}}]}
chat1(chat)


# our prompt is Who is MS Dhoni
# it is sent to function chat1(chat)
# we are sending our request to url and our response is coming in json file in t1 which we are then printing

#Web API offered by Google is stored in url
#think of API as a waiter at a restaurant

#there are some parameters: question and key
#reply is in json format (lightweight)

#content generation and task completion are different, the AI needs to understand it.