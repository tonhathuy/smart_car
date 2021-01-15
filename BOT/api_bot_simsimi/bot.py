import requests
import sys
# sys.path.insert(0, 'C:/Users/nguye/Downloads/SMART_CAR/SMART_CAR/BOT/api_stt')
# from stt import stt

import json
import time

def bot(text):
    t1 = time.time()
    #text = stt()

    url = "https://sim.cunnobi.xyz/api?text={}&format=JSON".format(text)

    querystring = {"text":"hi","lc":"en","ft":"0.0"}

    headers = {
        'x-rapidapi-key': "SIGN-UP-FOR-KEY",
        'x-rapidapi-host': "simsimi.p.rapidapi.com"
        }

    response = requests.request("GET", url)
    # print(response.text.splitlines()[-2].replace('</body>',''))
    t2 = time.time()
    dict_responce = json.loads(response.text.splitlines()[-2].replace('</body>',''))    
    print('Time bot:',t2-t1)
    print('bot response:',dict_responce['text'])
    return dict_responce['text']

if __name__ == "__main__":
    print(bot(stt()))