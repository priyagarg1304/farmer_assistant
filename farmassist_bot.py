from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from keras.models import load_model
import numpy as np
import pandas
# creating a new chatbot
data = pandas.read_csv('crop_production.csv')

crops = np.unique(data['Crop'])
states = np.unique(data['State_Name'])
districts = np.unique(data['District_Name'])
chatbot = ChatBot('caht')
trainer = ListTrainer(chatbot)
# some training data that will initiate the talk
trainer.train(
    ['What are you', 'I am a computer', 'What are you doing', 'Replying you   :D', 'How are you', 'I am always good'])

model= load_model("proj1.h5")
#response = chatbot.get_response("how r u")
#print(response)

import requests
import random
from datetime import datetime


def pred_season(state):
    # url for weather of current state
    wiki = "https://www.google.com/search?q=weather%20prediction%20" + state

    import time
    page = requests.get(wiki).text

    # Beautifulsoup is used for parsing the html document
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    # div storing the current temperature of the state accordin to google
    div = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'})
    # print(div)

    temp = div.get_text()
    print(temp)
    temp = int(temp.translate({ord(i): None for i in '°C'}))

    # current date and time
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")

    season = 0
    month = int(month)
    if (temp > 68 and temp < 80):
        print('Rabi')
        season = 2
    elif (temp > 60 and temp < 68 and month > 5 and month < 7):
        print('kharif')
        season = 1
    elif month <= 12 and month >= 9:
        print('Autumn')
        season = 0
    elif month <= 8 and month >= 5:
        print('Summer')
        season = 3
    elif month in [1, 12]:
        print('Winter')
        season = 5
    else:
        print('Whole Year')
        season = 4
    return season


def crops_pred(state, district, season):
    l1 = list()
    l2 = list()
    l3 = list()
    l4 = list()

    # total 124 crops are there and we predict the production with all the crops to determoine the highest production crops that the farmer should sow
    for i in range(124):
        inp = np.array([[state, district, season, i]])
        k = model.predict(inp)
        k = k[0][0]
        if (k == 4):
            l4.append(i)
        elif (k == 3):
            l3.append(i)
        elif (k == 2):
            l2.append(i)
        elif (k == 1):
            l1.append(i)
    cnt = 0
    random.shuffle(l4)
    random.shuffle(l3)
    random.shuffle(l2)
    random.shuffle(l1)
    for i in l4:
        cnt += 1
        if cnt <= 5:
            print(one_hot_crop(i))
    for i in l3:
        cnt += 1
        if cnt <= 5:
            print(one_hot_crop(i))
    for i in l2:
        cnt += 1
        if cnt <= 5:
            print(one_hot_crop(i))
    for i in l1:
        cnt += 1
        if cnt <= 5:
            print(one_hot_crop(i))

def get_one_hotSTATE(state):
  state= np.where(states==state)
  return state[0][0]
def get_one_hotDISTRICT(district):
  dist = np.where(districts==district)
  return dist[0][0]
def one_hot_crop(crop):
  return crops[crop]

resp=''
cnt=0
while(resp!='quit' and cnt<=1):
  cnt+=1
  resp=input('>>>')
  if(resp!='quit'):
    response = chatbot.get_response(resp)
    print(response)
if(resp!=quit):
  print('In which state do you live')
  state=input('>>>')
  print('In which disrict do you live')
  district=input('>>>')
  season = pred_season(state)
  print(" is your season.\n")
  state = get_one_hotSTATE(state)
  district = get_one_hotDISTRICT(district)
  print("You can grow the following crops according to your information and current weather updates:\n")
  crops_pred(state,district,season)
  print("Do you want to know more ?")
string="I want to know about "
while(resp!='quit' ):
  resp=input('>>>')
  if string in resp:
    resp=resp.replace(string,'')
    resp=resp.replace("Yes ",'')
    respon=resp.replace(' ',"%20")
    wiki = "https://www.google.com/search?q="+respon
    print("Ya sure! The following link can help you know about ",resp,"\n\n", wiki,'\n')
  elif(resp!='quit'):
    response = chatbot.get_response(resp)
    print(response)
    

