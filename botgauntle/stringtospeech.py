#!/usr/bin/python3.5


from gtts import gTTS
import os
import requests

url = 'http://18.207.128.175/get/swf/Orders/closed/timed_out/50/50'

def getReq(url):
    r = requests.get(url, auth=('DEMO', 'DEMO'))
    json_resp = r.json()
    status = r.json().get("Status", "")
    if status == "OK": 
        tts = gTTS(text='Hi there, SWF is looking good. No failed workflows so far', lang='en')
        tts.save("hello.mp3")
        os.system("mpg321 hello.mp3")
        os.remove("hello.mp3")
    else : 
        errors = r.json().get("Errors", "")
        orderErr = 0
        priceErr = 0
        lastDate = ""
        for i in range(len(errors)):
            lastDate = errors[i]["StartTime"];
            if errors[i]["Name"] == "Orders":
                orderErr += 1
            else :
                priceErr += 1
            

        tts = gTTS(text='Hi BIG CHEESE. We seem to have ' + str(orderErr) + ' timed out Orders & ' + str(priceErr) + ' timed out Prices in the Inbound domain for  ' + lastDate  , lang='en')
        tts.save("hello.mp3")
        os.system("mpg321 hello.mp3")
        os.remove("hello.mp3")
    return;
getReq(url)
