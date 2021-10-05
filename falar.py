#coding: utf-8
from chatterbot import ChatBot #pip install chatterbot || pip install --upgrade chatterbot_corpus
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
from chatterbot.trainers import ListTrainer
#ouvir
frase=''
questao = ''
def ouve():
    microfone = sr.Recognizer()
    with sr.Microphone() as ouvir:
        microfone.adjust_for_ambient_noise(ouvir)
        print('diga alguma coisa')
        audio = microfone.listen(ouvir)
    try:
        global frase
        frase = microfone.recognize_google(audio, language = 'pt-BR')
        return frase
    except:
        print("Não entendi")

#falar

def fala(questao):
    voices = fala.getProperty('voices')
    voz =  53
    fala.setProperty('voice', voices[voz].id)
    fala.say(frase)
    fala.runAndWait()

    fala.stop()
fala(frase)

