import tkinter as tk
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, subprocess

#api wolframalpha diganti dengan id anda
client = wolframalpha.Client('YKYLKY-9Q5LXPJ3U8')

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
    print('Eurus:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()

#language bisa  diganti dengan bahasa indonesia
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')

class Widget:
    def __init__(self):
        HEIGHT = 500
        WIDTH = 600

        #gambar bisa diganti sesuai dengan tempat penyimpanan anda
        root = tk.Tk()
        root.title('Personal Assistant')
        root.iconbitmap(r'C:\Users\Mara\Documents\Personal assistant2\Personal Assistant\botico.ico')
        root.resizable(0,0)
        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        self.compText = tk.StringVar()
        self.userText = tk.StringVar()
        self.userText.set('Click \'Start Listening\' to Give commands')

        img = ImageTk.PhotoImage(Image.open("mp.png"))
        canvas.create_image(0, 0, image=img, anchor='center')

        frame = tk.Frame(root, bg='#80c1ff', bd=5)
        frame.place(relx=0.5, rely=0.85, relwidth=0.9, relheight=0.1, anchor='n')



        photo=tk.PhotoImage(file = r"C:\Users\Mara\Documents\Personal assistant2\Personal Assistant\mc.png")
        photoimage= photo.subsample(18,18)
        button2 = tk.Button(frame, image=photoimage, command=self.clicked)
        button2.place(relx=0.01, relheight=1, relwidth=0.98)


        upper_frame = tk.Frame(root, bg='#80c1ff', bd=10)
        upper_frame.place(relx=0.5, rely=0.45, relwidth=0.9, relheight=0.4, anchor='n')

        label = tk.Label(upper_frame, textvariable=self.compText, bg='white', wraplength=500)
        label.place(relwidth=1, relheight=1.05)

        upper_frame2 = tk.Frame(root, bg='#80c1ff', bd=10)
        upper_frame2.place(relx=0.5, rely=0.45, relwidth=0.9, relheight=0.4, anchor='s')

        label2 = tk.Label(upper_frame2,textvariable=self.userText, bg='white', wraplength=100)
        label2.place(relwidth=1, relheight=1.1)

        speak('Hello, I am Eurus! What should I do for You?')
        self.compText.set('Hello, I am Eurus! What should I do for You?')

        root.bind("<Return>", self.clicked)  # handle the enter key event of your keyboard
        root.mainloop()

    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        #subprocess sesuai dengan tempat files anda
        if 'open ccleaner' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\CCleaner\CCleaner.exe')

        elif 'open google chrome' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif 'open powerpoint' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE')

        elif 'open youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.google.com')

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()

            if 'me' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Username')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set('Email sent!')
                    speak('Sorry ' + '!, I am unable to send your message at this moment!')
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye, have a good day.')
            speak('Bye, have a good day.')

        elif 'hello' in query:
            self.compText.set('Hello')
            speak('Hello')

        elif 'Thank you' in query:
            self.compText.set('You are welcome')
            speak('You are welcome')

        elif 'bye' in query:
            self.compText.set('Bye ' + ', have a good day.')
            speak('Bye ' + ', have a good day.')

        #music_player ddiganti sesuai dengan tempat penyimpanan anda
        elif 'play music' in query:
            music_folder = 'C:\\Users\\Mara\\Music\\MusicAss\\'
            music = ['alan walker', 'rihanna', 'zendaya', 'kelly']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')

        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    self.compText.set(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    self.compText.set(results)
                    speak(results)

            except:
                self.compText.set('Sorry, I don\'t know, you can search on google')
                speak('Sorry, I dan\'t know, you can search on google')
                webbrowser.open('www.google.com')


if __name__ == '__main__':
    greetMe()
    Widget = Widget()
