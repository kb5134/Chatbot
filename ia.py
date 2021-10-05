import pyttsx3 #pip install pyttsx3 #pip install pyaudio
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia #pip install wikipedia
import pywhatkit #pip install pywhatkit
fala = pyttsx3.init()
microfone = sr.Recognizer()

def comunicacao():
    try:
        with sr.Microphone() as ouvir:
            microfone.adjust_for_ambient_noise(ouvir)
            print('diga alguma coisa')
            audio = microfone.listen(ouvir)
            frase = microfone.recognize_google(audio, language = 'pt-BR')
            frase=frase.lower()

            if "hydra" in frase:

                frase = frase.replace('hydra', '')
                print(frase)
                fala.say(frase)
                fala.runAndWait()
    except:
        print("Não entendi")
    return(frase)
def comandos():
    comando = comunicacao()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H %M')
        fala.say('a hora certa' + hora)
        fala.runAndWait()

    if 'pesquise' in comando:
        procurar = comando.replace('pesquise', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        fala.say(resultado)
        fala.runAndWait()

    if 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        fala.say('tocando no youtube' + musica)
        fala.runAndWait()

comandos()