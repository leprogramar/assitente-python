from gtts import gTTS
from playsound import playsound
import os


def cria_audio():
    tts = gTTS('erro', lang= 'pt-br')
    tts.save('../audio/erro.mp3')
    playsound('../audio/erro.mp3')
    # os.remove('../audio/erro.mp3')

cria_audio()