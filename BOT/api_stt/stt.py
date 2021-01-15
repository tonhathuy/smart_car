import sounddevice as sd
from scipy.io.wavfile import write
import time


def stt():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print('Starting recording!')
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file
    print('Recording Saved')
    t1 = time.time()
    import requests

    url = 'https://api.fpt.ai/hmi/asr/general'
    payload = open('output.wav', 'rb').read()
    headers = {
        'api-key': 'UN99X7TICPsd5XhHt9AMDgLloBKSVTMC'
    }

    response = requests.post(url=url, data=payload, headers=headers).json()
    # response = {'status': 0, 'hypotheses': [{'confidence': 36.82841312981603, 'utterance': 'Xin chào . A .'}], 'id': 'tonhathuy97@gmail.com smart_car_1e71a59d-37f0-48fe-bdf0-3d9758b30a8e'}
    print(response)
    t2 = time.time()
    print('Time speech to text:',t2 - t1)
    if response['status'] == 0:
        text = response['hypotheses'][0]['utterance']
        return text
    return ''

if __name__ == "__main__":
    text = stt()
    print(text)