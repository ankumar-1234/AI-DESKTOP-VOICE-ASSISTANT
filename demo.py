import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
from ecapture import ecapture as ec
from requests import get, request
import sys
import time
import pyjokes
import wolframalpha
import json
import pyautogui
import requests

#text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#wish me function
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good morning, its {tt}")
    elif hour > 12 and hour < 18:
        speak(f"Good evening, its {tt}")

    else:
        speak(f"Good evening, its {tt}")
    speak("hello mam , i am your persnal voice asssistant and sir i can perform multiple task like open all software programs and closing all software programs,predict time,take a photo,search wikipedia,predict weather in different cities , get top headline news from times of india and you can ask me computational or geographical questions, and open multiple webbrowser task like open google , open youtube , open multiple websites like leetcode, hackerrank, stackoverflow and os related task can perform like shutdown, restart,and sleep the system  and sir multiple task i can perform find my location and find my ipaddress and  play music and i can perform multiple operation you can choose anyone oparation who you like it thats all about me sir how can i help you sir, thank you")

# voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=7)

    try:
        print("Recognition...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        

    except Exception as e:
        #speak("Sorry, I could not understand. Could you please say that again")
        return "none"
    query = query.lower()
    return query


if __name__ == "__main__":
    wish()
    while True:
    
        query = takecommand()

        # logic building for tasks
        
        if "hello jarvis" in query:
            speak("hello sir,  how are you")

        elif"i am good and you" in query:
            speak("i am also good sir  please tell me how can i help you")

        elif"what about you" in query:
            speak("hello sir, i am your persnal voice asssistant and sir i can perform multiple task like open all software programs and closing all software programs,predict time,take a photo,search wikipedia,predict weather in different cities , get top headline news from times of india and you can ask me computational or geographical questions, and open multiple webbrowser task like open google , open youtube , open multiple websites like leetcode, hackerrank, stackoverflow and os related task can perform like shutdown, restart,and sleep the system  and sir multiple task i can perform find my location and find my ipaddress and  play music thats all about me sir , thank you ")

        elif "thank you" in query:
            speak("welcome sir ,  please tell me how can i help you ")

        elif "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            speak("ok sir i am opening the notepad for u")
            os.startfile(npath)
        
        elif "closing notepad" in query:
            speak("okay sir, i am closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            speak("okay sir opening command promt now")
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "E:\\music"
            speak("ok sir play a music")
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "camera" in query:
            ec.capture(0, "robo camera", "img.jpg")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takecommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif "open youtube" in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif "open google" in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif "open gmail" in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("opening facebook now")
            time.sleep(5)

        elif "open hackerrank" in query:
            webbrowser.open("www.hackerrank.com")
            speak("opening the website hackerrank now ")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        

        elif 'who made you' in query or 'who created you' in query or 'who discovered you' in query:   
            speak("I was built by Ankit Kumar")
            print("I was built by Ankit Kumar")


        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        
        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)
        
        elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takecommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif "Ok you can sleep" in query or "ok bye" in query or "stop" in query:
            speak("thanks for using me sir, i am going to sleep now")
            sys.exit() 

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("restart /s /t 5")

        elif "sleep the system" in query:
            speak("ok sir i am going to sleeping now")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

###############################################################################################
#....................To find my location using IP Address 

        elif "where i am" in query or "where we are" in query:
            speak("wait sir ,let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure , but i think we are in {city} city of {state} state of {country} in country")
            except Exception as e:
                speak("sorry sir, due to network issues i am not able to find where we are")
                pass
        
#.................................to take a screenshot...................

        elif"take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save("f{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder now i am ready for next command")




   