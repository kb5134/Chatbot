#coding: utf-8
from chatterbot import ChatBot #pip install chatterbot
import pyttsx3
import speech_recognition as sr
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
    def falar(texto):
        fala = pyttsx3.init()
        fala.say(texto)
        fala.runAndWait()
        fala.stop()
    falar(questao)
fala(questao)

#chatbot
def chat(): 
    bot = ChatBot('c3pO')
    questao = ListTrainer(bot)
    #you can add a archive from your computer 
    #arq = open('C:/Users/KB/Documents/test.txt')
    #ler = arq.read()
    #troca = ler.replace('\n', ',')
    questao.train(['Oi', 'Olá', 'Tudo bem?',
             'Tudo ótimo', 'qual é o seu nome?, meu nome é c3pO, e o seu?, legal'])

    while True:
        
        resposta = bot.get_response(ouve())
        print('eu:', frase)
        print('bot: ',resposta)
        fala(resposta)

chat()