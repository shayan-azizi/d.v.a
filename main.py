import speech_recognition as sr
import webbrowser as wb
from gtts import gTTS
from playsound import playsound

def main_command ():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("I'm listening.... ")
        
        listening_voice = gTTS("I am listening!")
        listening_voice.save("listening_voice.mp3")
        
        playsound("listening_voice.mp3")
        
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print ("Recognizing")
            
            recognizing_voice = gTTS("let me recognize!")
            recognizing_voice.save("recognizing_voice.mp3")
        
            playsound("recognizing_voice.mp3")
            
            query = r.recognize_google(audio, language= 'fa-IR', show_all=False)
            print (f"User said: {query}\n")
        except Exception as e:
            print (e)
            print ("I can not recognize your voice!")
            
            recognizing_voice2 = gTTS("I can not recognize your voice!")
            recognizing_voice2.save("recognizing2_voice.mp3")
        
            playsound("recognizing2_voice.mp3")
            
            return "None"
        
        return query

text = main_command()

if text == "در گوگل جستجو کن":
    print("ok what should i search in Google?")
    
    google_voice1 = gTTS("ok! what should i search in Google?")
    google_voice1.save("google_voice1.mp3")
    
    playsound("google_voice1.mp3")
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:        
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print ("Recognizing")
            
            recognizing_voice3 = gTTS("let me recognize!")
            recognizing_voice3.save("recognizing3_voice.mp3")
        
            playsound("recognizing3_voice.mp3")
            
            query = r.recognize_google(audio, language= 'fa-IR', show_all=False)
            # print(query)

        except Exception as e:
            print (e)
            print ("I can not recognize your voice!")
            
            recognizing_voice2 = gTTS("I can not recognize your voice!")
            recognizing_voice2.save("recognizing2_voice.mp3")

            playsound("recognizing2_voice.mp3")
            
            print ("None") 
        
        print("I searched the entered phrase in Google. look at your browser")
        
        
        browser = gTTS("I searched the entered phrase in Google. look at your browser")
        browser.save("browser.mp3")
    
        playsound("browser.mp3")
        
        wb.open("https://google.com/search?q="+ query)
        
        
        
        
        
        
if text == "در بینگ جستجو کن":
    print("ok what should i search in Bing?")
    
    bing_voice1 = gTTS("ok! what should i search in Bing?")
    bing_voice1.save("bing_voice1.mp3")
    
    playsound("bing_voice1.mp3")
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:        
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print ("Recognizing")
            
            recognizing_voice5 = gTTS("let me recognize!")
            recognizing_voice5.save("recognizing5_voice.mp3")
        
            playsound("recognizing5_voice.mp3")
            
            query = r.recognize_google(audio, language= 'fa-IR', show_all=False)
            # print(query)

        except Exception as e:
            print (e)
            print ("I can not recognize your voice!")
            
            recognizing_voice4 = gTTS("I can not recognize your voice!")
            recognizing_voice4.save("recognizing4_voice.mp3")

            playsound("recognizing4_voice.mp3")
            
            print ("None") 
        
        print("I searched the entered phrase in Bing. look at your browser")
        
        
        browser1 = gTTS("I searched the entered phrase in Bing. look at your browser")
        browser1.save("browser1.mp3")
    
        playsound("browser1.mp3")
        
        wb.open("https://bing.com/search?q="+ query)





if text == "در ویکی پدیا جستجو کن":
    print("ok what should i search in Wikipedia?")
    
    wiki_voice1 = gTTS("ok! what should i search in Wikipedia?")
    wiki_voice1.save("wiki_voice1.mp3")
    
    playsound("wiki_voice1.mp3")
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:        
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print ("Recognizing")
            
            recognizing_voice7 = gTTS("let me recognize!")
            recognizing_voice7.save("recognizing7_voice.mp3")
        
            playsound("recognizing7_voice.mp3")
            
            query = r.recognize_google(audio, language= 'fa-IR', show_all=False)
            # print(query)

        except Exception as e:
            print (e)
            print ("I can not recognize your voice!")
            
            recognizing_voice6 = gTTS("I can not recognize your voice!")
            recognizing_voice6.save("recognizing6_voice.mp3")

            playsound("recognizing6_voice.mp3")
            
            print ("None") 
        
        print("I searched the entered phrase in Wikipedia. look at your browser")
        
        
        browser2 = gTTS("I searched the entered phrase in wikipedia. look at your browser")
        browser2.save("browser2.mp3")
    
        playsound("browser2.mp3")
        
        wb.open("https://fa.wikipedia.org/wiki/"+ query)
        
        
        
        

if text == "در یوتیوب جستجو کن":
    print("ok what should i search in Youtube?")
    
    yt_voice1 = gTTS("ok! what should i search in YouTube?")
    yt_voice1.save("yt_voice1.mp3")
    
    playsound("yt_voice1.mp3")
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:        
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print ("Recognizing")
            
            recognizing_voice9 = gTTS("let me recognize!")
            recognizing_voice9.save("recognizing9_voice.mp3")
        
            playsound("recognizing9_voice.mp3")
            
            query = r.recognize_google(audio, language= 'fa-IR', show_all=False)
            # print(query)

        except Exception as e:
            print (e)
            print ("I can not recognize your voice!")
            
            recognizing_voice8 = gTTS("I can not recognize your voice!")
            recognizing_voice8.save("recognizing8_voice.mp3")

            playsound("recognizing8_voice.mp3")
            
            print ("None") 
        
        print("I searched the entered phrase in YouTube. look at your browser")
        
        
        browser3 = gTTS("I searched the entered phrase in youtube. look at your browser")
        browser3.save("browser3.mp3")
    
        playsound("browser3.mp3")
        
        wb.open("https://youtube.com/search?q="+ query)





if text == "سایت مدرسه را باز کن":
    
    print ("I opened the school website. look at your browser")
    
    browser4 = gTTS("I opened the school website. look at your browser")
    browser4.save("browser4.mp3")

    playsound("browser4.mp3")
    
    wb.open("https://helli1.iranlms.org/login/index.php")
    
    

                
        
    