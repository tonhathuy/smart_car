import requests
from unidecode import unidecode
import playsound
import os
import urllib3
import shutil
import sys

sys.path.insert(0, 'C:/Users/nguye/Downloads/SMART_CAR/SMART_CAR/BOT/api_bot_simsimi')
sys.path.insert(1, 'C:/Users/nguye/Downloads/SMART_CAR/SMART_CAR/BOT/api_stt')
from stt import stt
from bot import bot
import time

OUTPUT_MP3_FOLDER = 'BOT/api_tts/mp3_file/'
API_KEY = 'ANhnbSnpQOrYnu4rQ5PRwYM90BWsjGN4'


def tts(payload):
    t1 = time.time()
    url = 'https://api.fpt.ai/hmi/tts/v5'
    headers = {
        'api-key': API_KEY,
        'speed': '',
        'voice': 'thuminh'
    }

    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers).json()

    print(response)
    try:
        mp3_file = response['async']
        mp3_file_name = unidecode(payload).replace(' ', '_') + '.wav'
        output_mp3_file = os.path.join(OUTPUT_MP3_FOLDER, mp3_file_name)

        http = urllib3.PoolManager()
        with open(output_mp3_file, 'wb') as out:
            r = http.request('GET', mp3_file, preload_content=False)

        shutil.copyfileobj(r, out)
        playsound.playsound(output_mp3_file)
    except:
        print('We cannot convert to speech')


    t2 = time.time()
    print('Time text to speech:',t2 - t1)

if __name__ == "__main__":
    tts(bot(stt()))