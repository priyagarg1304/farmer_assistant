# FARMASSIST
A virtual assistant for farmers

A chatbot - FARMASSIST which helps the farmer in selecting the appropriate crops for their sowing season depending on various attributes like season,weather,temperature,location(state and district) .

The bot is trained using publically avalilable datasets on crop production patterns across different astates in India using Deep Learning model to determine the top yielding crops for the current season for the farmer.

The bot takes real weather updates of the farmer’s location from Internet through web scraping.The bot is interactive and user -friendly using a public Python Repository-ChatterBot.

# How to use :
1) Clone the directory in your desktop
2) Run the farmassist_model.py file -> A proj.h5 must be created
3) Run the farmassist_bot.py that is the main chatbot for farmers.

=> proj.h5 file has been included in the directory itself so you can directly run the farmassist_bot as well.

If error occurs  in finding proj.h5 file kindly copy the location of this file and change it in the farmassist_bot.py file for its smooth usage .

The following image shows how it looks like: 
![Chatbot view](https://github.com/priyagarg1304/farmer_assistant/blob/master/Screenshots/final%20reuslts.PNG)
