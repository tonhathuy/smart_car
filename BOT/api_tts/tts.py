import requests
from unidecode import unidecode
import playsound
import os
import urllib3
import shutil
import sys

# sys.path.insert(0, 'C:/Users/nguye/Downloads/SMART_CAR/SMART_CAR/BOT/api_bot_simsimi')
# sys.path.insert(1, 'C:/Users/nguye/Downloads/SMART_CAR/SMART_CAR/BOT/api_stt')
# from stt import stt
# from bot import bot
import time

OUTPUT_MP3_FOLDER = 'BOT/api_tts/mp3_file/'
API_KEY = 'ANhnbSnpQOrYnu4rQ5PRwYM90BWsjGN4'
# API_KEY = 'UN99X7TICPsd5XhHt9AMDgLloBKSVTMC'

def check_time_sleep(payload):
    len_text = len(payload.split(' '))
    if len_text == 1:
        return int(len_text)
    return int(len_text/2)

def tts(payload):
    t1 = time.time()
    url = 'https://api.fpt.ai/hmi/tts/v5'
    headers = {
        'api-key': API_KEY,
        'speed': '',
        'voice': 'thuminh'
    }


    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers).json()
    # response = {'async': 'https://static.openfpt.vn/text2speech-v5/short/2021-01-15/thuminh.0.b2389f4f086b3c1ae301029eeba0645a.mp3', 'error': 0, 'message': 'The content will be returned after a few seconds under the async link.', 'request_id': '8451557935db92fdf89fe6befe1c2f2f'}
    # print(response)
    try:
        mp3_file = response['async']
        print(mp3_file)
        mp3_file_name_ = unidecode(payload).replace(' ', '_') 
        bad_chars = [';', ':', '!', "*", '(' ,')', '.','{', '}','"','+','-','/','@','#','$','%','^','&','*','|']
        # remove bad_chars
        mp3_file_name = ''.join((filter(lambda i: i not in bad_chars, mp3_file_name_))) + '.mp3'
        output_mp3_file = os.path.join(OUTPUT_MP3_FOLDER, mp3_file_name)

        http = urllib3.PoolManager()
        
        time.sleep(check_time_sleep(payload))
        with open(output_mp3_file, 'wb') as out:
            r = http.request('GET', mp3_file, preload_content=False)
            shutil.copyfileobj(r, out)
        
        playsound.playsound(output_mp3_file)
    except Exception as e:
        print('We cannot convert to speech', e)


    t2 = time.time()
    print('Time text to speech:',t2 - t1)

if __name__ == "__main__":
    tts('text')
    # with open(output_mp3_file, 'wb') as out:
    #         r = http.request('GET', mp3_file, preload_content=False)
    #         shutil.copyfileobj(r, out)
        
    # playsound.playsound(output_mp3_file)