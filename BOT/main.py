from api_bot_simsimi.bot import bot
from api_stt.stt import stt
from api_tts.tts import tts 

if __name__ == "__main__":
    tts(bot(stt()))