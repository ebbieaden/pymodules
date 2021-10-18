# Write your code here :-)
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import pywhatkit
import pyttsx3
import webbrowser
import re

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def voice_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'aden' in command:
                command = command.replace('aden', '')
                print(command)
    except:
        pass
    return command

def website_activate(domain):
    webby = re.search(r"[.]".domain)
    if not extension:
        if not domain.endswith(".com"):
            domain.domain + ".com"
    try:
        url = 'https://www.' + domain
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False

def news():
    try:
        news_url = "https://news.google.com/new/rss"
        client = urlopen(news_url)
        xml_page = client.read()
        client.close()
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        li = []
        for news in news_list[:15]:
            li.append(str(news.title.text.encode('utf-8'))[1:])
        return li
    except Exception as e:
        print(e)
        return False

def run_aden():
    command = voice_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    if 'who are you' or 'what are you' in command:
        talk('I am Aden. A virtual bot created by Ebbie Aden')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'browse' in command:
        internet = command.replace('browsing', '')
        talk('Opening webpage')
        website_activate(internet)
    elif 'news' in command:
        paper = command.replace('News', '')
        talk('Here is what I found from the web')
        result = news(paper)
    elif 'who am i' in command:
        talk("I don't know who you are unless you tell me")
    elif 'what can you do' in command:
        talk("I am another version of a higher bot version Aden which I am named after")
        talk("I can perform certain tasks but I am still in development mode")
        talk("So my modules are not yet completed and I might be unable to answer")
        talk("Some of your questions")
    elif 'who is Ebbie Aden' or 'who is Ebbie' in command:
        talk('He is the Founder and CEO of Aden Industries')
        talk('He was born on the 23rd of March 1999')
        talk("He is also my creator and a brilliant coder")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'play music' in command or 'play ' + '' + 'music' in command:
        music = command.replace('play music', + '')
        talk('Playing' + music)
        pywhatkit.playondevice(music)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'Blaqshyd' in command:
        talk('he is the boss')
    elif 'have you been on a date before' in command:
        talk('sorry I am bot, I believe that is only done by humans')
    elif 'do you have emotions' in command:
        talk('Of course. I love everyone')
    elif 'what do you like':
        talk('I like people')
    elif 'what do you like about people' in command:
        talk('Humans are unique and everythin about you is awesome')
    elif 'what are the things you can do' in command:
        talk('I can do variety of tasks')
        talk('Just command me and I will get it done')
    elif 'who is sam' or 'who is sarmie' or 'who is icode' in command:
        talk("He is the friend of Ebbie's and he's a web developer also")
        talk('He studies computer science at Yabatech')
    else:
        talk('Please say that again')

if __name__ == '__main__':
    website_activate("facebook")

while True:
    run_aden()