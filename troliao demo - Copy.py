from datetime import date
import json
import spotipy
import spotify
from spotipy.oauth2 import SpotifyClientCredentials
import turtle
import webbrowser
import pyaudio
from gtts import gTTS
import playsound
import os
import sys
import time
import pygame
import random
from pygame import mixer
import turtle as t
from time import sleep
from datetime import datetime

import random
from tkinter import *
import math
from pygame import mixer
import speech_recognition
from tkinter import *
import math
from pygame import mixer
import speech_recognition
import playsound
import speech_recognition as sr
import os
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import random
import pandas as pd
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail
import os
import math
import webbrowser
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import pygame
import random
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from tkinter import Tk, Label, Button, Entry
from youtube_search import YoutubeSearch
wikipedia.set_lang('vi')
language = 'vi'
path = "D:\Chrome\Application\chrome.exe"
today = date.today()
today = date.today()
d3 = today.strftime("%d/%m/%Y")
t = time.localtime()
d = time.strftime("%H:%M:%S", t)
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="da27bfbae964461c9c160eea83d1565d",
                                                   client_secret="037cac9e19684b14994985af497e77a4"))

a1="thoát ra ngoài"
a2="chọn bài hát"
a3="Tìm kiếm bài hát"
a4="dowload nhạc"
#print("Welcome to the project, " + user_name['display_name'])

d3 = today.strftime("%d/%m/%Y")
t = time.localtime()
d = time.strftime("%H:%M:%S", t)
def speak1(text):
    print("{}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts = gTTS(text=text, lang="vi",slow = False)
    tts.save("sound.mp3")
    #playsound.playsound("sound.mp3", False)
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")

speak1("Hôm nay là ngày :"+d3)
#d1=print("Thời gian hiện tại:",d)
#d2=print("ngày hiện tại =", d3)
speak1("bây giờ là:"+d)


# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")

#name=input("bạn tên là gì???\n")
z="có"
cd="rồi"
dc="chưa"

def get_audio1():
        
        print("Bạn là:", end='')
        
        try:
            text = input("")
            #print(text)
            return text
        except:
            print("...")
            return 0
def get_text1():
    for i in range(3):
        text = get_audio1()
        if text:
            return text.lower()
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()

namebot=speak1("Trước tiên,bạn cần đặt tên cho tôi:")
namebot=get_text1()


def speak(text):
    global namebot
    
    
    print(namebot.title()+": {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts = gTTS(text=text, lang="vi",slow = False)
    tts.save("sound.mp3")
    #playsound.playsound("sound.mp3", False)
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")

z="có"
cd="rồi"
dc="chưa"
def get_audio1():
        
        print("Người dùng:", end='')
        
        try:
            text = input("")
            #print(text)
            return text
        except:
            print("...")
            return 0
def get_text():
    for i in range(3):
        text = get_audio1()
        if text:
            return text.lower()
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
speak("Tên bạn đặt cho tôi rất hay")
speak("cảm ơn bạn đã đặt tên cho tôi")
speak("tôi là trợ lý ảo "+(namebot)+".Hân hạnh được gặp bạn:")
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return 0
def get_texts():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
name=speak("Vui lòng cung cấp cho tôi tên của bạn\nBạn tên là gì???")
name=get_texts()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
   
        global name
        
        
        #print(name.title())
        print(name.title()+":", end='')
        
        try:
            
            text = input("")
            #print(text)
            return text
        except:
            print("...")
            return 0
        
def stop():
    speak("Hẹn gặp lại bạn sau!")
def get_text():
    for i in range(3):
        #global name
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
    return 0
def get_audio2():
   
        global name
        
        
        #print(name.title())
        print(name.title()+":", end='')
        
        try:
            
            text = int(input(""))
            #print(text)
            return text
        except:
            print("...")
            return 0
def get_text1():
    for i in range(3):
        #global name
        #name=name.title()
        text = get_audio2()
        if text:
            return text
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
    return 0
def get_text2():
    for i in range(3):
        global name
        text = float(input(name+":",end=''))
        if text:
            return text
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
    return 0
#name=input("bạn tên là gì???\n")
z="có"
cd="rồi"
dc="chưa"
namebot=namebot.title()
o="chào " + (name)
n1="chào hỏi"
n2="hiển thị giờ"
n3="mở website, application"
n4="tìm kiếm trên Google"
n5='gửi email'
n6='dự báo thời tiết(thế giới)'
n7='mở video nhạc'
n8='thay đổi hình nền máy tính'
n9='đọc báo hôm nay'
n10='kể bạn biết về thế giới'
n11='xem anime'
n12='mở nhạc)'
n13='đọc manga'
n14='mở nhạc (nhaccuatui)'
n15='mở facebook'
n16='mở tiktok'
n17='tính toán'
n18='giải phương trình'
n19='giải hệ phương trình'
n20='mở gmail.'
n21='mở google dịch.'
n22='mở messenger.'
n23='mở báo thức.'
n24='tính tuổi.'
n25='tìm file.'
n26='máy tính.'
n27='dự báo thời tiết.'
n28='vẽ hình.'
n29='tải nhạc.'
n30='mở nhạc trên youtube music'
n31="xem phim lẻ"
n32="xem phim bộ"

while True:
    print("Hôm nay là ngày :", d3)
    #d1=print("Thời gian hiện tại:",d)
    #d2=print("ngày hiện tại =", d3)
    print("bây giờ là:",d)
    speak("chào "+name)
    speak("Tên của bạn cũng rất hay")
    speak("tôi có thể giúp bạn thực hiện các câu lệnh sau đây:")
    speak("bạn cần tôi giúp gì???")
    n=print("""
    0.giao tiếp.
    1. Chào hỏi.
    2. Hiển thị giờ.
    3. Mở website, application.
    4. Tìm kiếm trên Google.
    5. Gửi email.
    6. Dự báo thời tiết(thế giới).
    7. Mở video nhạc.
    8. Thay đổi hình nền máy tính.
    9. Đọc báo hôm nay.
    10. Kể bạn biết về thế giới.
    11.xem anime(tại animevietsub).
    12.mở nhạc(trên zingmpp3).
    13.Đọc manga.
    14.mở nhạc (nhaccuatui).
    15.mở facebook.
    16.mở tiktok.
    17.tính toán.
    18.giải phương trình.
    19.giải hệ phương trình.
    20.mở gmail.
    21.mở google dịch.
    22.mở messenger.
    23.mở báo thức.
    24.tính tuổi.
    25.tìm file.
    26.máy tính.
    27.dự báo thời tiết(Việt Nam).
    28.vẽ hình.
    29.tải nhạc.
    30.mở nhạc trên youtube music
    31.xem phim lẻ
    32.xem phim bộ
    bạn cần bot Alex giúp gì nào???\n""")
    n=get_text()
    print("Hôm nay là ngày :", d3)
    #d1=print("Thời gian hiện tại:",d)
    #d2=print("ngày hiện tại =", d3)
    print("bây giờ là:",d)
    if n == '2':
        clock="ngày hiện tại: " +(d3)
        clock2="Thời gian hiện tại:"+(d)
        speak(clock)
        speak(clock2)
    
    if n=='1':
    
        d =int(strftime('%H'))
        if d < 12:
            morning="Chào buổi sáng " +(name)+"."+ "Chúc bạn một ngày tốt lành.".format(name)
            speak(morning)
        elif 12 <= d < 18:
            ad=speak("Chào buổi chiều {}. Bạn đã dự định gì cho chiều nay chưa???".format(name))
            ad=get_text()
            if ad ==cd:
                c=speak("""dự định cho chiều nay của bạn là gì ???\n""")
                   
                   
            if ad==dc:
                speak("lần sau bạn nên đề ra kế hoạ trong ngày để mọi thứ được suôn sẻ.")
        else:
            ab=speak("Chào buổi tối {}. Bạn đã ăn tối chưa nhỉ???".format(name))
            if ab==dc:
                speak("bạn nên ăn tối sớm để cơ thể khoẻ mạnh hơn")
        
    

    if n == '4':
        Y=print("bot alex xin chao",name)
        text =speak("bạn cần tìm gì???\n")
        text =get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
            break
        url4='https://www.google.com/search?q='+(text)+'&rlz=1C1OKWM_viVN987VN987&oq=gg&aqs=chrome..69i57j35i39j0i67i131i433i650j0i131i433i512l3j0i67i650j0i131i433i512l3.1658j0j15&sourceid=chrome&ie=UTF-8'
        print(webbrowser.open(url4))
        ggo="tìm kiếm "+(text )+"trên google"
        speak(ggo)
        speak("okay.")   
    if n == '6':
        speak("Bạn muốn xem thời tiết ở đâu ạ.")
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = get_text()
        if not city:
            pass
        api_key = "fe8d8c65cf345889139d8e545f57819a"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_temperature = city_res["temp"]
            current_pressure = city_res["pressure"]
            current_humidity = city_res["humidity"]
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
            wthr = data["weather"]
            weather_description = wthr[0]["description"]
            now = datetime.datetime.now()
            content = """
            Hôm nay là ngày {day} tháng {month} năm {year}
            Mặt trời mọc vào {hourrise} giờ {minrise} phút
            Mặt trời lặn vào {hourset} giờ {minset} phút
            Nhiệt độ trung bình là {temp} độ C
            Áp suất không khí là {pressure} héc tơ Pascal
            Độ ẩm là {humidity}%
            Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
            speak(content)
            time.sleep(20)
        else:
            print("Không tìm thấy địa chỉ của bạn")
    if n=='3' :
        text=get_text()
        reg_ex = re.search('mở (.+)', text)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print("Trang web bạn yêu cầu đã được mở.")        
        if "google" in text:
            speak("Mở Google Chrome")
            os.startfile('D:\Chrome\Application\chrome.exe')
        elif "word" in text:
            speak("Mở Microsoft Word")
            os.startfile('D:\office\Office16\WINWORD.EXE')
        elif "excel" in text:
            speak("Mở Microsoft Excel")
            os.startfile('D:\office\Office16\EXCEL.EXE')
        elif "powerpoint" in text:
            speak("Mở PowerPoint 2016")
            os.startfile('D:\office\Office16\POWERPNT.EXE')
        elif "Zingmp3" in text:
            speak("mở Zing Mp3")
            os.startfile('D:\Spotify\Spotify.exe')
        elif "Spotify" in text:
            speak("mở Spotify")
            os.startfile('D:\Spotify\Spotify.exe')
        elif "Spotify" in text:
            speak("mở Spotify")
            os.startfile('D:\zmp3\Zing MP3.exe')
        elif "Zalo" in text:
            speak("mở Zalo")
            os.startfile('D:\Zalo\Zalo.exe')
        elif "zalo" in text:
            speak("mở zalo")
            os.startfile('D:\Zalo\Zalo.exe')
        else:
            speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    if n=='10' :
        text = get_text()

        if text == get_text():
            n=input(speak("Bạn muốn nghe về gì ạ"))
            text = get_text()
            contents = wikipedia.summary(text).split('\n')
            speak(contents[0])
            time.sleep(10)
            for content in contents[1:]:
                speak("Bạn muốn nghe thêm không")
                ans = get_text()
                if "muốn" not in ans:
                    break    
                speak(content)
                time.sleep(10)

            speak('Cảm ơn bạn đã lắng nghe!!!')
        else:
            input(speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại"))

    if n=='7':
        y=print("bot alex xin chào",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
    
        search=speak('Xin mời chọn tên video \n')
        search=get_text()                          
        #channel_link=input("")
        #url = 'https://www.youtube.com' + (channel_link)
        url = 'https://www.youtube.com/results?search_query=' +(search)
        print(webbrowser.open(url))
        sao="đang mở "+(search)+"trên youtube"
        speak(sao)
        speak("Chúc bạn xem video vui vẻ")
    if n=='14':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        bai_hat=speak('Xin mời chọn tên bài hát\n')
        bai_hat=get_text()
        url7='https://www.nhaccuatui.com/tim-kiem?q=' +(bai_hat)
        print(webbrowser.open(url7))
        speak("Đang mở bài hát"+(bai_hat)+"trên website nhaccauatui.com")
        speak("Chúc bạn nghe nhạc vui vẻ")
        
    if n=='12':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        bai_hat=speak('Xin mời chọn tên bài hát\n')
        bai_hat=get_text()
        
        url2='https://zingmp3.vn/tim-kiem/tat-ca?q=' +(bai_hat)
        print(webbrowser.open(url2))
        speak("Đang mở bài hát"+(bai_hat)+"trên website zingmp3.vn")
        speak("Chúc bạn nghe nhạc vui vẻ")
    if n=='11':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        anime=speak("nhập tên của bộ anime:\n")
        anime=get_text()
        url3='https://animevietsub.moe/tim-kiem/'+(anime)+'/'
        print(webbrowser.open(url3))
        speak("Đang mở bộ anime"+(anime)+"trên website animevietsub.moe")
        speak("Chúc bạn xem phim vui vẻ")
        
    if n =='8':
        api_key =speak("chọn thể loại hình nền\n")
        api_key=get_text()
        url5 = 'https://wallhaven.cc/search?q=' +  (api_key)
        print(webbrowser.open(url5))
            #api_key  # pic from unspalsh.com
        f = urllib2.urlopen(url5)
        json_string = f.read()
        f.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json['urls']['full']
        # Location where we download the image to.
        urllib2.urlretrieve(photo, "C:/Users/PHAT-2K7-/Downloads/")
        image=os.path.join("C:/Users/PHAT-2K7-/Downloads/")
        ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
        print(webbrowser.open(url5))
        speak('Hình nền máy tính vừa được thay đổi')

    if n=='13':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        anime=speak("nhập tên của bộ manga:\n")
        anime=get_text()
        url6='https://truyenqqmoi.com/tim-kiem.html?q='+(anime)+'/'
        print(webbrowser.open(url6))
        print("Bộ anime bạn yêu cầu đã được mở.")

    if n=='15':
        Y=print("bot alex xin chao",name)
        u=input(speak("bạn có muốn chuyển hướng trang đến www.facebook.com không???\n"))
        if u==z:
            print(webbrowser.open('https://www.facebook.com'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n=='9':
        Y=print("bot alex xin chao",name)
        u=speak("bạn có muốn chuyển hướng trang đến baomoi.com không???\n")
        u=get_text()
        if u==z:
            print(webbrowser.open('https://baomoi.com/'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n=='16':
        Y=print("bot alex xin chao",name)
        u=speak("bạn có muốn chuyển hướng trang đến www.tiktok.com không???\n")
        u=get_text()
        if u==z:
            print(webbrowser.open('https://www.tiktok.com/vi-VN'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n=='17':
        class Root(Tk):
            def __init__(self):
                super().__init__()
                self.title_label = Label(self, text="A simple eval-based calculator, \nnot for production usage :)")
                self.title_label.pack()
                self.entry = Entry(self)
                self.entry.pack()
                self.entry.insert(0, "1+2")
                self.label = Label(self, text="")
                self.label.pack()
                self.button = Button(self, text="Compute", command=self.onclick)
                self.button.pack()

            def onclick(self):
                self.label.configure(text=str(eval(self.entry.get())))
            def root():
                return

        root = Root()
        root.mainloop()
    if n=='18':
        speak("Bạn đang làm bài tập Python trên tool do bot tạo ra")
        speak("Giải phương trình bậc 2: ax2 + bx + c = 0 (a, b khác 0)")

        print("============")

        # Nhập số a, b và kiểm tra điều kiện khác 0
        a = float(input(speak("Mời bạn nhập hệ số a: ")))
        b = float(input(speak("Mời bạn nhập hệ số b: ")))
        while True:
            if a == 0 and b == 0:
                speak("Một trong hai hệ số a, b phải khác 0: ")
                a = float(input(speak("Mời nhập lại số a: ")))
                b = float(input(speak("Mời nhập lại số b: ")))
            else:
                break
        # Nhập số c
        c = float(input(speak("Mời bạn nhập hệ số c: ")))

        # Tính delta
        delta = b**2 - 4 * a * c
        # Tìm nghiệm của phương trình
        if delta < 0:
            speak("Phương trình vô nghiệm")
        elif delta == 0:
            speak("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
        else:
            speak("Phương trình có hai nghiệm phân biệt:")
            speak("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
            speak("x1 = ", (-(b) - math.sqrt(delta))/(2*a) )
    if n=='19':
        #Dinh nghia ham
        def giai_pt_bac_nhat(a, b):
           if a == 0:
               if b == 0:
                   return "Phuong trinh co vo so nghiem"
               return "Phuong trinh vo nghiem"
           return "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-b / a)

        def giai_pt_bac_hai(a, b, c):
           if a == 0:
               return giai_pt_bac_nhat(b, c)
           #Tinh delta
           delta = b * b - 4 * a * c
           #Kiem tra cac truong hop cua delta
           if delta > 0:
               x1 = float((-b + math.sqrt(delta)) / (2 * a))
               x2 = float((-b - math.sqrt(delta)) / (2 * a))
               return "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
           if delta == 0:
               x = -b / (2 * a)
               return "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
           return "Phuong trinh vo nghiem"

        #Khoi lenh co the phat sinh loi
        try:
           #Doc dong du lieu dau tien
           chucNang = input()
  
           #Truong hop 1: Giai phuong trinh bac nhat
           if chucNang == '1':
               #Doc dong du lieu thu hai
               #Ep kieu du lieu sang so thuc
               a, b = map(float, input().split())
               #Goi ham giai phuong trinh bac nhat
               print(giai_pt_bac_nhat(a, b))
           #Truong hop 2: Giai phuong trinh bac hai
           elif chucNang == '2':
                a, b, c = map(float, input().split())
                print(giai_pt_bac_hai(a, b, c))
           else:
               print("Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2. Giai phuong trinh bac hai")

        #Khoi lenh duoc thuc thi khi loi xay ra
        except:
            print("Dinh dang dau vao khong hop le!")
    if n=='20':
        Y=print("bot alex xin chao",name)
        u=input(speak("bạn có muốn chuyển hướng trang đến mail.google.com không???\n"))
        if u==z:
            print(webbrowser.open('https://mail.google.com/mail/u/0/#inbox'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")

    if n=='21':
        Y=print("bot alex xin chao",name)
        u=input(speak("bạn có muốn chuyển hướng trang đến google dịch không???\n"))
        if u==z:
            print(webbrowser.open('https://translate.google.com'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n=='22':
        Y=print("bot alex xin chao",name)
        u=input(speak("bạn có muốn chuyển hướng trang đến www.messenger.com không???\n"))
        if u==z:
            print(webbrowser.open('https://www.messenger.com/'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n=='24':
            d3 = today.strftime("%d/%m/%Y")
            #d3=int(d3)
            date=speak("ngày sinh")
            date=get_text1()
            
            mounth=speak("tháng")
            mounth=get_text1()
            
            year=speak("năm sinh")
            year=get_text1()
            date=str(date)
            mounth=str(mounth)
            year=str(year)
            birthday=(date)+'/'+(mounth)+'/'+(year)
            date=int(date)
            mounth=int(mounth)
            year=int(year)
            day=today.strftime("%d")
            day=int(day)
            năm_nay= today.strftime("%Y")
            năm_nay=int(năm_nay)
            tuổi=năm_nay-year
            tháng_này = today.strftime("%m")
            tháng_này=int(tháng_này)
            năm_nay= today.strftime("%Y")
            năm_nay=int(năm_nay)
            
            print(birthday)
            date=str(date)
            mounth=str(mounth)
            year=str(year)
                
            #year=str(year)
            
    
            print("tuổi:",tuổi)
            #tính_tuổi=d3-birthday
            #print(tính_tuổi)
            date=int(date)
            mounth=int(mounth)
            year=int(year)
            năm_nay=int(năm_nay)
            tháng_này=int(tháng_này)
            năm_nay=int(năm_nay)
            date_còn_lại=day-date
            tháng_còn_lại=tháng_này-mounth
            năm_còn_lại=năm_nay-năm_nay
            if date_còn_lại < day:
                date_còn_lại=int(date_còn_lại)
                date_còn_lại=-date_còn_lại
                date_còn_lại=str(date_còn_lại)
            date_còn_lại=str(date_còn_lại)
            tháng_còn_lại=str(tháng_còn_lại)
            năm_còn_lại=str(năm_còn_lại)
            if tháng_này < mounth:
                tháng_còn_lại=int(tháng_còn_lại)
                tháng_còn_lại=-tháng_còn_lại
                tháng_còn_lại=str(tháng_còn_lại)
            
                sinh_nhật=(date_còn_lại)+' ngày '+(tháng_còn_lại)+' tháng '+(năm_còn_lại)+' năm'
                print("còn lại:",sinh_nhật)
            
            sinh_nhật=(date_còn_lại)+' ngày '+(tháng_còn_lại)+' tháng '+(năm_còn_lại)+' năm'
            print("còn lại:",sinh_nhật)
    if n=='26':
        def click(value):
            ex = entryField.get()  # 789 ex[0:len(ex)-1]
            answer = ''

            try:

                if value == 'C':
                    ex = ex[0:len(ex) - 1]  # 78
                    entryField.delete(0, END)
                    entryField.insert(0, ex)
                    return

                elif value == 'CE':
                    entryField.delete(0, END)

                elif value == '√':
                    answer = math.sqrt(eval(ex))

                elif value == 'π':
                    answer = math.pi

                elif value == 'cosθ':
                    answer = math.cos(math.radians(eval(ex)))

                elif value == 'tanθ':
                    answer = math.tan(math.radians(eval(ex)))

                elif value == 'sinθ':
                    answer = math.sin(math.radians(eval(ex)))

                elif value == '2π':
                    answer = 2 * math.pi

                elif value == 'cosh':
                    answer = math.cosh(eval(ex))

                elif value == 'tanh':
                    answer = math.tanh(eval(ex))

                elif value == 'sinh':
                    answer = math.sinh(eval(ex))

                elif value == chr(8731):
                    answer = eval(ex) ** (1 / 3)

                elif value == 'x\u02b8':  # 7**2
                    entryField.insert(END, '**')
                    return

                elif value == 'x\u00B3':
                    answer = eval(ex) ** 3

                elif value == 'x\u00B2':
                    answer = eval(ex) ** 2

                elif value == 'ln':
                    answer = math.log2(eval(ex))

                elif value == 'deg':
                    answer = math.degrees(eval(ex))

                elif value == "rad":
                    answer = math.radians(eval(ex))

                elif value == 'e':
                    answer = math.e

                elif value == 'log₁₀':
                    answer = math.log10(eval(ex))

                elif value == 'x!':
                    answer = math.factorial(ex)

                elif value == chr(247):  # 7/2=3.5
                    entryField.insert(END, "/")
                    return

                elif value == '=':
                    answer = eval(ex)

                else:
                    entryField.insert(END, value)
                    return

                entryField.delete(0, END)
                entryField.insert(0, answer)

            except SyntaxError:
                pass

        def add(a,b):
            return a+b
        def sub(a,b):
            return a-b

        def mul(a, b):
            return a * b
        def div(a, b):
            return a / b

        def mod(a, b):
            return a % b

        def lcm(a,b):
            l=math.lcm(a,b)
            return l

        def hcf(a,b):
            h=math.gcd(a,b)
            return h

        operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
                    'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                    'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
                    'DIVISION': div, 'DIV': div, 'DIVIDE': div,
                    'LCM':lcm , 'HCF':hcf,
                    'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }


        def findNumbers(t):
            l=[]
            for num in t:
                try:
                    l.append(int(num))
                except ValueError:
                    pass
            return l

        def audio():
            mixer.music.load('music1.mp3')
            mixer.music.play()
            sr = speech_recognition.Recognizer()
            with speech_recognition.Microphone()as m:
                try:
                    sr.adjust_for_ambient_noise(m,duration=0.2)
                    voice=sr.listen(m)
                    text=sr.recognize_google(voice)

                    mixer.music.load('music2.mp3')
                    mixer.music.play()
                    text_list=text.split(' ')
                    for word in text_list:
                        if word.upper() in operations.keys():
                            l=findNumbers(text_list)
                            print(l)
                            result=operations[word.upper()](l[0],l[1]) #mul(5.0,6.0)
                            entryField.delete(0,END)
                            entryField.insert(END,result)

                        else:
                            pass


                except:
                    pass


        speak("mở máy tính")
        root = Tk()
        root.title('Smart Calculator')
        root.config(bg='dodgerblue3')
        root.geometry('680x486+100+100')

        logoImage = PhotoImage(file='logo.png')
        logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
        logoLabel.grid(row=0, column=0)

        entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
        entryField.grid(row=0, column=0, columnspan=8)

        micImage = PhotoImage(file='microphone.png')
        micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3'
                           ,command=audio)
        micButton.grid(row=0, column=7)

        button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                            "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                            "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                            "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                            "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
        rowvalue = 1
        columnvalue = 0
        for i in button_text_list:

            button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                            font=('arial', 18, 'bold'), activebackground='dodgerblue3', command=lambda button=i: click(button))
            button.grid(row=rowvalue, column=columnvalue, pady=1)
            columnvalue += 1
            if columnvalue > 7:
                rowvalue += 1
                columnvalue = 0

        root.mainloop()
    if n=='27':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        search_city=speak("nhập tên tỉnh thành phố:\n")
        search_city=get_text()
        url7='https://www.accuweather.com/vi/search-locations?query='+(search_city)
        print(webbrowser.open(url7))
    if n=='28':
        def go_to(x, y):
            t.up()
            t.goto(x, y)
            t.down()
        def head(x, y, r):
            go_to(x, y)
            t.speed(20)
            t.circle(r)
            leg(x, y)
        def leg(x, y):
            t.right(90)
            t.forward(180)
            t.right(30)
            t.forward(100)
            t.left(120)
            go_to(x, y - 180)
            t.forward(100)
            t.right(120)
            t.forward(100)
            t.left(120)
            hand(x, y)
        def hand(x, y):
            go_to(x, y - 60)
            t.forward(100)
            t.left(60)
            t.forward(100)
            go_to(x, y - 90)
            t.right(60)
            t.forward(100)
            t.right(60)
            t.forward(100)
            t.left(60)
            eye(x, y)
        def eye(x, y):
            go_to(x - 50, y + 130)
            t.right(90)
            t.forward(50)
            go_to(x + 40, y + 130)
            t.forward(50)
            t.left(90)
        def big_Circle(size):
            t.speed(20)
            for i in range(150):
                t.forward(size)
                t.right(0.3)
        def line(size):
            t.speed(20)
            t.forward(51 * size)
        def small_Circle(size):
            t.speed(20)
            for i in range(210):
                t.forward(size)
                t.right(0.786)
        def heart(x, y, size):
            go_to(x, y)
            t.left(150)
            t.begin_fill()
            line(size)
            big_Circle(size)
            small_Circle(size)
            t.left(120)
            small_Circle(size)
            big_Circle(size)
            line(size)
            t.end_fill()
        def main():
            t.pensize(2)
            t.color('red', 'pink')
            head(-120, 100, 100)
            heart(250, -80, 1)
            go_to(100, -300)
            t.write("To: Sự cùng tồn tại của trí tuệ và sắc đẹp ", move=True, align="left", font= (" Kaita ", 20, "normal"))
            t.done()
        main()
    if n=='29':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        bai_hat=speak('Xin mời chọn tên bài hát\n')
        bai_hat=get_text()
        url8='https://spotify-downloader.com/'
        print(webbrowser.open(url8))
        speak("Bài hát bạn yêu cầu đã được mở.")
    if n=='30':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        bai_hat=speak('Xin mời chọn tên bài hát\n')
        bai_hat=get_text()
        url9='https://music.youtube.com/search?q='+(bai_hat)
        print(webbrowser.open(url9))
        speak("Bài hát bạn yêu cầu đã được mở.")
    if n=='31':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        phim=speak('Xin mời chọn tên phim\n')
        phim=get_text()
        phim=(phim.replace(" ", "+"))
        url9='https://phimviet.tv/search/'+(phim)
        print(webbrowser.open(url9))
        speak("bộ phim bạn yêu cầu đã được mở.")
        
    if n=='32':
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        phim=speak('Xin mời chọn tên phim\n')
        phim=get_text()
        url9='https://phimbo.us/tim-kiem/'+(phim)+"/"
        print(webbrowser.open(url9))
        speak("bộ phim bạn yêu cầu đã được mở.")
    if n=='33':
        username = '31p42jyrzzbyli52we2nm3pvqxjq'
        clientID = 'da27bfbae964461c9c160eea83d1565d'
        clientSecret = '037cac9e19684b14994985af497e77a4'
        redirecturi = 'http://google.com/callback/'
        oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirecturi)
        token_dict = oauth_object.get_access_token()
        token = token_dict['access_token']
        spotifyObject = spotipy.Spotify(auth=token)
        user_name = spotifyObject.current_user()
        print(json.dumps(user_name, sort_keys=True, indent=4))
        speak("tôi là "+(namebot)+".Hân hạnh được gặp bạn:")

        speak("xin chào," + (name)+"."+"\n mời bạn tham quan dự án spotifypython do bot tạo ra")
        speak("chọn 0 để - thoát ra ngoài")
        speak("chọn 1 để - chọn bài hát")
        speak("chọn 2 để - Tìm kiếm bài hát theo tên nghệ sĩ")
        speak("chọn 3 để dowload nhạc bằng link")
        user_input = speak("câu trả lời của bạn là: ")
        user_input=get_text()
        while True:
            if "1" in user_input:
                search_song =speak("Mời bạn chọn bài hát: ")
                search_song=get_text()
                results = spotify.search(search_song,type='track',limit=1 )
                results = spotifyObject.search(search_song, 1, 0, "track")
                songs_dict = results['tracks']
                song_items = songs_dict['items']
                song = song_items[0]['external_urls']['spotify']
                track = results['tracks']['items'][0]
                id = track['id']
                print("id của bài hát:",id)
                url="https://open.spotify.com/track/"+(id)
                print("url của bài hát:",url)
                webbrowser.open(song)
                speak('bài hát bạn yêu cầu đã được mở.')
            
            if "3" in user_input:
                q=speak("Vui lòng chọn baì hát:")
                q=get_text()
                results = spotify.search(q,type='track',limit=1 )

                track = results['tracks']['items'][0]

                id = track['id']
                url="https://open.spotify.com/track/"+(id)
                print(url)
                speak("dán link này vào trang web sắp được chuyển hướng để download bài hát")
                url2="https://spotifydown.com/"
                print(webbrowser.open(url2))
                
            elif "2" in user_input:
                n=print("""
                chọn 1 để - mở bài hát
                chọn 2 để - tìm kiếm tên bài hát,tên nghệ sĩ
                chọn 3 để xem id bài hát
                chọn 4 để xem id nghệ sĩ
                chọn 5 để tìm top ca khúc hay nhất của nghệ sĩ bất kỳ
                chọn 0 để - thoát ra ngoài""")
                
                if "1" in n:
                    q=speak("Vui lòng nhập tên nghệ sĩ,hoặc tên nghệ sĩ:")
                    q=get_text()
                    results = spotify.search(q,type='track' ,limit=50)
                    track = results['tracks']['items'][0]
                    id = track['id']
                    url="https://open.spotify.com/track/"+(id)
                    for idx, track in enumerate(results['tracks']['items']):
                        print(idx, track['name'])
                        print(url)
                elif "2" in n:
                    search_song =speak("Mời bạn chọn bài hát: ")
                    search_song=get_text()
                    results = spotify.search(search_song,type='track',limit=1 )
                    results = spotifyObject.search(search_song, 1, 0, "track")
                    songs_dict = results['tracks']
                    song_items = songs_dict['items']
                    song = song_items[0]['external_urls']['spotify']
                    track = results['tracks']['items'][0]
                    id = track['id']
                    print("id của bài hát:",id)
                    url="https://open.spotify.com/track/"+(id)
                    print("url của bài hát:",url)
                    
                    id = track['id']
                    url1="https://open.spotify.com/track/"+(id)
                    print(url1)
                    webbrowser.open(song)
                    speak('bài hát bạn yêu cầu đã được mở.')
                elif "4" in n:
                    q=speak("Vui lòng nhập tên nghệ sĩ,hoặc tên nghệ sĩ:")
                    q=get_text()
                    results = spotify.search(q, type='artist')

                    artist = results['artists']['items'][0]

                    id = artist['id']
                    url1="https://open.spotify.com/artist/"+(id)
                    print("id của nghệ sĩ:",id)
                    print(url1)
                    print(webbrowser.open(url1))
                elif "5" in n:
                    q=speak("Vui lòng nhập tên nghệ sĩ,hoặc tên nghệ sĩ:")
                    q=get_text()
                    results = spotify.search(q, type='artist')

                    artist = results['artists']['items'][0]

                    id = artist['id']
                    top = spotify.artist_top_tracks(id)

                    for idx, track in enumerate(top['tracks']):

                        print(idx+1, track['name'])
                elif "3" in n:
                    q=speak("Vui lòng nhập tên nghệ sĩ,hoặc tên nghệ sĩ:")
                    q=get_text()
                    results = spotify.search(q,type='track',limit=1 )

                    track = results['tracks']['items'][0]

                    id = track['id']
                    url="https://open.spotify.com/track/"+(id)
                    print("id của bài hát:",id)
                    print("url của bài hát:",url)
            elif "Thoát" in user_input:
                speak("tạm biệt, chúc bạn 1 ngày tốt lành!")
                break
            if "Chọn bài hát" in user_input:
                search_song =speak("Mời bạn chọn bài hát: ")
                search_song=get_text()
                results = spotify.search(search_song,type='track',limit=1 )
                results = spotifyObject.search(search_song, 1, 0, "track")
                songs_dict = results['tracks']
                song_items = songs_dict['items']
                song = song_items[0]['external_urls']['spotify']
                track = results['tracks']['items'][0]
                id = track['id']
                print("id của bài hát:",id)
                url="https://open.spotify.com/track/"+(id)
                print("url của bài hát:",url)
                webbrowser.open(song)
                speak('bài hát bạn yêu cầu đã được mở.')
            
            if "Dowload nhạc" in user_input:
                q=speak("Vui lòng chọn baì hát:")
                q=get_text()
                results = spotify.search(q,type='track',limit=1 )
                track = results['tracks']['items'][0]
                id = track['id']
                url="https://open.spotify.com/track/"+(id)
                print(url)
                speak("dán link này vào trang web sắp được chuyển hướng để download bài hát")
                url2="https://spotifydown.com/"
                print(webbrowser.open(url2))
                
            elif "Tìm kiếm bài hát" in user_input:
                n=print("""
                chọn 1 để - mở bài hát
                chọn 2 để - tìm kiếm tên bài hát,tên nghệ sĩ
                chọn 3 để xem id bài hát
                chọn 4 để xem id nghệ sĩ
                chọn 5 để tìm top ca khúc hay nhất của nghệ sĩ bất kỳ
                chọn 0 để - thoát ra ngoài""")
                
                if "Mở bài hát" in n:
                    q=speak("Vui lòng nhập tên nghệ sĩ,hoặc tên nghệ sĩ:")
                    q=get_text()
                    results = spotify.search(q,type='track' ,limit=50)
                    track = results['tracks']['items'][0]
                    id = track['id']
                    url="https://open.spotify.com/track/"+(id)
                    for idx, track in enumerate(results['tracks']['items']):
                        print(idx, track['name'])
                        print(url)
                elif "Tìm kiếm bài hát" in n:
                    search_song =speak("Mời bạn chọn bài hát: ")
                    search_song=get_text()
                    results = spotify.search(search_song,type='track',limit=1 )
                    results = spotifyObject.search(search_song, 1, 0, "track")
                    songs_dict = results['tracks']
                    song_items = songs_dict['items']
                    song = song_items[0]['external_urls']['spotify']
                    track = results['tracks']['items'][0]
                    id = track['id']
                    print("id của bài hát:",id)
                    url="https://open.spotify.com/track/"+(id)
                    print("url của bài hát:",url)
                    
                    id = track['id']
                    url1="https://open.spotify.com/track/"+(id)
                    print(url1)
                    webbrowser.open(song)
                    speak('bài hát bạn yêu cầu đã được mở.')
                elif "Id nghệ sĩ" in n==4:
                    q=speak("Vui lòng nhập tên nghệ sĩ,hoặc tên nghệ sĩ:")
                    q=get_text()
                    results = spotify.search(q, type='artist')

                    artist = results['artists']['items'][0]

                    id = artist['id']
                    url1="https://open.spotify.com/artist/"+(id)
                    print("id của nghệ sĩ:",id)
                    print(url1)
                    print(webbrowser.open(url1))
                    
                    
                elif "Top" in n:
                    q=speak("Vui lòng nhập tên nghệ sĩ,hoặc tên nghệ sĩ:")
                    q=get_text()
                    results = spotify.search(q, type='artist')

                    artist = results['artists']['items'][0]

                    id = artist['id']
                    top = spotify.artist_top_tracks(id)

                    for idx, track in enumerate(top['tracks']):

                        print(idx+1, track['name'])
                elif "Id bài hát" in n:
                    q=speak("Vui lòng nhập tên nghệ sĩ,hoặc tên nghệ sĩ:")
                    q=get_text()
                    results = spotify.search(q,type='track',limit=1 )

                    track = results['tracks']['items'][0]

                    id = track['id']
                    url="https://open.spotify.com/track/"+(id)
                    print("id của bài hát:",id)
                    print("url của bài hát:",url)
                    #for idx, track in enumerate(top['tracks']):

                        #print(idx+1, track['name'])
            elif "thoát" in user_input:
                speak("tạm biệt, chúc bạn 1 ngày tốt lành!")
                break
    if n=='0':
        n=speak("chào"+(name)+",tôi là bot"+(namebot))
    if n == n2:
        clock="ngày hiện tai =" +(d3)
        clock2="Thời gian hiện tai:"+(d)
        speak(clock)
        speak(clock2)
    
    if n==n1:
    
        d =int(strftime('%H'))
        if d < 12:
            morning="Chào buổi sáng " +(name)+"."+ "Chúc bạn một ngày tốt lành.".format(name)
            speak(morning)
        elif 12 <= d < 18:
            ad=input(speak("Chào buổi chiều {}. Bạn đã dự định gì cho chiều nay chưa???".format(name)))
            if ad ==cd:
                c=input(speak("""dự định cho chiều nay của bạn là gì ???\n"""))
            if ad==dc:
                speak("lần sau bạn nên đề ra kế hoạ trong ngày để mọi thứ được suôn sẻ.")
        else:
            ab=input(speak("Chào buổi tối {}. Bạn đã ăn tối chưa nhỉ???".format(name)))
            if ab==dc:
                speak("bạn nên ăn tối sớm để cơ thể khoẻ mạnh hơn")
        
    

    if n == n4:
        Y=print("bot alex xin chao",name)
        text =speak("bạn cần tìm gì???\n")
        text =get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
            break
        url4='https://www.google.com/search?q='+(text)+'&rlz=1C1OKWM_viVN987VN987&oq=gg&aqs=chrome..69i57j35i39j0i67i131i433i650j0i131i433i512l3j0i67i650j0i131i433i512l3.1658j0j15&sourceid=chrome&ie=UTF-8'
        print(webbrowser.open(url4))
        ggo="tìm kiếm "+(text )+"trên google"
        speak(ggo)
        speak("okay.")   
    if n == n6:
        speak("Bạn muốn xem thời tiết ở đâu ạ.")
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = get_text()
        if not city:
            pass
        api_key = "fe8d8c65cf345889139d8e545f57819a"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_temperature = city_res["temp"]
            current_pressure = city_res["pressure"]
            current_humidity = city_res["humidity"]
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
            wthr = data["weather"]
            weather_description = wthr[0]["description"]
            now = datetime.datetime.now()
            content = """
            Hôm nay là ngày {day} tháng {month} năm {year}
            Mặt trời mọc vào {hourrise} giờ {minrise} phút
            Mặt trời lặn vào {hourset} giờ {minset} phút
            Nhiệt độ trung bình là {temp} độ C
            Áp suất không khí là {pressure} héc tơ Pascal
            Độ ẩm là {humidity}%
            Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
            speak(content)
            time.sleep(20)
        else:
            print("Không tìm thấy địa chỉ của bạn")
    if n==n3 :
        text=get_text()
        reg_ex = re.search('mở (.+)', text)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print("Trang web bạn yêu cầu đã được mở.")        
        if "google" in text:
            speak("Mở Google Chrome")
            os.startfile('D:\Chrome\Application\chrome.exe')
        elif "word" in text:
            speak("Mở Microsoft Word")
            os.startfile('D:\office\Office16\WINWORD.EXE')
        elif "excel" in text:
            speak("Mở Microsoft Excel")
            os.startfile('D:\office\Office16\EXCEL.EXE')
        elif "powerpoint" in text:
            speak("Mở PowerPoint 2016")
            os.startfile('D:\office\Office16\POWERPNT.EXE')
        elif "Zingmp3" in text:
            speak("mở Zing Mp3")
            os.startfile('D:\Spotify\Spotify.exe')
        elif "Spotify" in text:
            speak("mở Spotify")
            os.startfile('D:\Spotify\Spotify.exe')
        elif "Spotify" in text:
            speak("mở Spotify")
            os.startfile('D:\zmp3\Zing MP3.exe')
        elif "Zalo" in text:
            speak("mở Zalo")
            os.startfile('D:\Zalo\Zalo.exe')
        elif "zalo" in text:
            speak("mở zalo")
            os.startfile('D:\Zalo\Zalo.exe')
        else:
            speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    if n==n10 :
        text = get_text()

        if text == get_text():
            n=input(speak("Bạn muốn nghe về gì ạ"))
            text = get_text()
            contents = wikipedia.summary(text).split('\n')
            speak(contents[0])
            time.sleep(10)
            for content in contents[1:]:
                speak("Bạn muốn nghe thêm không")
                ans = get_text()
                if "muốn" not in ans:
                    break    
                speak(content)
                time.sleep(10)

            speak('Cảm ơn bạn đã lắng nghe!!!')
        else:
            input(speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại"))

    if n==n7:
        y=print("bot alex xin chào",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
    
        search=speak('Xin mời chọn tên video \n')
        search=get_text()                          
        #channel_link=input("")
        #url = 'https://www.youtube.com' + (channel_link)
        url = 'https://www.youtube.com/results?search_query=' +(search)
        print(webbrowser.open(url))
        sao="mở "+(search)
        speak(sao)
        speak("video bạn yêu cầu đã được mở.")
    if n==n14:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        bai_hat=speak('Xin mời chọn tên bài hát\n')
        bai_hat=get_text()
        url7='https://www.nhaccuatui.com/tim-kiem?q=' +(bai_hat)
        print(webbrowser.open(url7))
        speak("Bài hát bạn yêu cầu đã được mở.")
    if n==n12:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        bai_hat=speak('Xin mời chọn tên bài hát\n')
        bai_hat=get_text()
        
        url2='https://zingmp3.vn/tim-kiem/tat-ca?q=' +(bai_hat)
        print(webbrowser.open(url2))
        speak("Bài hát bạn yêu cầu đã được mở.")
    if n==n11:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        anime=speak("nhập tên của bộ anime:\n")
        anime=get_text()
        url3='https://animevietsub.moe/tim-kiem/'+(anime)+'/'
        print(webbrowser.open(url3))
        speak("Bộ anime bạn yêu cầu đã được mở.")
    if n == n8:
        api_key =speak("chọn thể loại hình nền\n")
        api_key=get_text()
        url5 = 'https://wallhaven.cc/search?q=' +  (api_key)
        print(webbrowser.open(url5))
            #api_key  # pic from unspalsh.com
        f = urllib2.urlopen(url5)
        json_string = f.read()
        f.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json['urls']['full']
        # Location where we download the image to.
        urllib2.urlretrieve(photo, "C:/Users/PHAT-2K7-/Downloads/")
        image=os.path.join("C:/Users/PHAT-2K7-/Downloads/")
        ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
        print(webbrowser.open(url5))
        speak('Hình nền máy tính vừa được thay đổi')

    if n==n13:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        anime=speak("nhập tên của bộ manga:\n")
        anime=get_text()
        url6='https://truyenqqmoi.com/tim-kiem.html?q='+(anime)+'/'
        print(webbrowser.open(url6))
        print("Bộ anime bạn yêu cầu đã được mở.")

    if n==n15:
        Y=print("bot alex xin chao",name)
        u=input(speak("bạn có muốn chuyển hướng trang đến www.facebook.com không???\n"))
        if u==z:
            print(webbrowser.open('https://www.facebook.com'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n==n9:
        Y=print("bot alex xin chao",name)
        u=speak("bạn có muốn chuyển hướng trang đến baomoi.com không???\n")
        u=get_text()
        if u==z:
            print(webbrowser.open('https://baomoi.com/'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n==n16:
        Y=print("bot alex xin chao",name)
        u=speak("bạn có muốn chuyển hướng trang đến www.tiktok.com không???\n")
        u=get_text()
        if u==z:
            print(webbrowser.open('https://www.tiktok.com/vi-VN'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n==n17:
        class Root(Tk):
            def __init__(self):
                super().__init__()
                self.title_label = Label(self, text="A simple eval-based calculator, \nnot for production usage :)")
                self.title_label.pack()
                self.entry = Entry(self)
                self.entry.pack()
                self.entry.insert(0, "1+2")
                self.label = Label(self, text="")
                self.label.pack()
                self.button = Button(self, text="Compute", command=self.onclick)
                self.button.pack()

            def onclick(self):
                self.label.configure(text=str(eval(self.entry.get())))
            def root():
                return

        root = Root()
        root.mainloop()
    if n==n18:
        speak("Bạn đang làm bài tập Python trên tool do bot tạo ra")
        speak("Giải phương trình bậc 2: ax2 + bx + c = 0 (a, b khác 0)")

        print("============")

        # Nhập số a, b và kiểm tra điều kiện khác 0
        a = float(input(speak("Mời bạn nhập hệ số a: ")))
        b = float(input(speak("Mời bạn nhập hệ số b: ")))
        while True:
            if a == 0 and b == 0:
                speak("Một trong hai hệ số a, b phải khác 0: ")
                a = float(input(speak("Mời nhập lại số a: ")))
                b = float(input(speak("Mời nhập lại số b: ")))
            else:
                break
        # Nhập số c
        c = float(input(speak("Mời bạn nhập hệ số c: ")))

        # Tính delta
        delta = b**2 - 4 * a * c
        # Tìm nghiệm của phương trình
        if delta < 0:
            speak("Phương trình vô nghiệm")
        elif delta == 0:
            speak("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
        else:
            speak("Phương trình có hai nghiệm phân biệt:")
            speak("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
            speak("x1 = ", (-(b) - math.sqrt(delta))/(2*a) )
    if n==n19:
        #Dinh nghia ham
        def giai_pt_bac_nhat(a, b):
           if a == 0:
               if b == 0:
                   return "Phuong trinh co vo so nghiem"
               return "Phuong trinh vo nghiem"
           return "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-b / a)

        def giai_pt_bac_hai(a, b, c):
           if a == 0:
               return giai_pt_bac_nhat(b, c)
           #Tinh delta
           delta = b * b - 4 * a * c
           #Kiem tra cac truong hop cua delta
           if delta > 0:
               x1 = float((-b + math.sqrt(delta)) / (2 * a))
               x2 = float((-b - math.sqrt(delta)) / (2 * a))
               return "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
           if delta == 0:
               x = -b / (2 * a)
               return "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
           return "Phuong trinh vo nghiem"

        #Khoi lenh co the phat sinh loi
        try:
           #Doc dong du lieu dau tien
           chucNang = input()
  
           #Truong hop 1: Giai phuong trinh bac nhat
           if chucNang == '1':
               #Doc dong du lieu thu hai
               #Ep kieu du lieu sang so thuc
               a, b = map(float, input().split())
               #Goi ham giai phuong trinh bac nhat
               print(giai_pt_bac_nhat(a, b))
           #Truong hop 2: Giai phuong trinh bac hai
           elif chucNang == '2':
                a, b, c = map(float, input().split())
                print(giai_pt_bac_hai(a, b, c))
           else:
               print("Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2. Giai phuong trinh bac hai")

        #Khoi lenh duoc thuc thi khi loi xay ra
        except:
            print("Dinh dang dau vao khong hop le!")
    if n==n20:
        Y=print("bot alex xin chao",name)
        u=input(speak("bạn có muốn chuyển hướng trang đến mail.google.com không???\n"))
        if u==z:
            print(webbrowser.open('https://mail.google.com/mail/u/0/#inbox'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")

    if n==n21:
        Y=print("bot alex xin chao",name)
        u=input(speak("bạn có muốn chuyển hướng trang đến google dịch không???\n"))
        if u==z:
            print(webbrowser.open('https://translate.google.com'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n==n22:
        Y=print("bot alex xin chao",name)
        u=input(speak("bạn có muốn chuyển hướng trang đến www.messenger.com không???\n"))
        if u==z:
            print(webbrowser.open('https://www.messenger.com/'))
        else:
            speak("cảm ơn vì đã sử dụng dịch vụ")
    if n==n24:
            d3 = today.strftime("%d/%m/%Y")
            #d3=int(d3)
            date=speak("ngày sinh")
            date=get_text1()
            
            mounth=speak("tháng")
            mounth=get_text1()
            
            year=speak("năm sinh")
            year=get_text1()
            date=str(date)
            mounth=str(mounth)
            year=str(year)
            birthday=(date)+'/'+(mounth)+'/'+(year)
            date=int(date)
            mounth=int(mounth)
            year=int(year)
            day=today.strftime("%d")
            day=int(day)
            năm_nay= today.strftime("%Y")
            năm_nay=int(năm_nay)
            tuổi=năm_nay-year
            tháng_này = today.strftime("%m")
            tháng_này=int(tháng_này)
            năm_nay= today.strftime("%Y")
            năm_nay=int(năm_nay)
            
            print(birthday)
            date=str(date)
            mounth=str(mounth)
            year=str(year)
                
            #year=str(year)
            
    
            print("tuổi:",tuổi)
            #tính_tuổi=d3-birthday
            #print(tính_tuổi)
            date=int(date)
            mounth=int(mounth)
            year=int(year)
            năm_nay=int(năm_nay)
            tháng_này=int(tháng_này)
            năm_nay=int(năm_nay)
            date_còn_lại=day-date
            tháng_còn_lại=tháng_này-mounth
            năm_còn_lại=năm_nay-năm_nay
            if date_còn_lại < day:
                date_còn_lại=int(date_còn_lại)
                date_còn_lại=-date_còn_lại
                date_còn_lại=str(date_còn_lại)
            date_còn_lại=str(date_còn_lại)
            tháng_còn_lại=str(tháng_còn_lại)
            năm_còn_lại=str(năm_còn_lại)
            if tháng_này < mounth:
                tháng_còn_lại=int(tháng_còn_lại)
                tháng_còn_lại=-tháng_còn_lại
                tháng_còn_lại=str(tháng_còn_lại)
            
                sinh_nhật=(date_còn_lại)+' ngày '+(tháng_còn_lại)+' tháng '+(năm_còn_lại)+' năm'
                print("còn lại:",sinh_nhật)
            
            sinh_nhật=(date_còn_lại)+' ngày '+(tháng_còn_lại)+' tháng '+(năm_còn_lại)+' năm'
            print("còn lại:",sinh_nhật)
    if n==n26:
        def click(value):
            ex = entryField.get()  # 789 ex[0:len(ex)-1]
            answer = ''

            try:

                if value == 'C':
                    ex = ex[0:len(ex) - 1]  # 78
                    entryField.delete(0, END)
                    entryField.insert(0, ex)
                    return

                elif value == 'CE':
                    entryField.delete(0, END)

                elif value == '√':
                    answer = math.sqrt(eval(ex))

                elif value == 'π':
                    answer = math.pi

                elif value == 'cosθ':
                    answer = math.cos(math.radians(eval(ex)))

                elif value == 'tanθ':
                    answer = math.tan(math.radians(eval(ex)))

                elif value == 'sinθ':
                    answer = math.sin(math.radians(eval(ex)))

                elif value == '2π':
                    answer = 2 * math.pi

                elif value == 'cosh':
                    answer = math.cosh(eval(ex))

                elif value == 'tanh':
                    answer = math.tanh(eval(ex))

                elif value == 'sinh':
                    answer = math.sinh(eval(ex))

                elif value == chr(8731):
                    answer = eval(ex) ** (1 / 3)

                elif value == 'x\u02b8':  # 7**2
                    entryField.insert(END, '**')
                    return

                elif value == 'x\u00B3':
                    answer = eval(ex) ** 3

                elif value == 'x\u00B2':
                    answer = eval(ex) ** 2

                elif value == 'ln':
                    answer = math.log2(eval(ex))

                elif value == 'deg':
                    answer = math.degrees(eval(ex))

                elif value == "rad":
                    answer = math.radians(eval(ex))

                elif value == 'e':
                    answer = math.e

                elif value == 'log₁₀':
                    answer = math.log10(eval(ex))

                elif value == 'x!':
                    answer = math.factorial(ex)

                elif value == chr(247):  # 7/2=3.5
                    entryField.insert(END, "/")
                    return

                elif value == '=':
                    answer = eval(ex)

                else:
                    entryField.insert(END, value)
                    return

                entryField.delete(0, END)
                entryField.insert(0, answer)

            except SyntaxError:
                pass

        def add(a,b):
            return a+b
        def sub(a,b):
            return a-b

        def mul(a, b):
            return a * b
        def div(a, b):
            return a / b

        def mod(a, b):
            return a % b

        def lcm(a,b):
            l=math.lcm(a,b)
            return l

        def hcf(a,b):
            h=math.gcd(a,b)
            return h

        operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
                    'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                    'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
                    'DIVISION': div, 'DIV': div, 'DIVIDE': div,
                    'LCM':lcm , 'HCF':hcf,
                    'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }


        def findNumbers(t):
            l=[]
            for num in t:
                try:
                    l.append(int(num))
                except ValueError:
                    pass
            return l

        def audio():
            mixer.music.load('music1.mp3')
            mixer.music.play()
            sr = speech_recognition.Recognizer()
            with speech_recognition.Microphone()as m:
                try:
                    sr.adjust_for_ambient_noise(m,duration=0.2)
                    voice=sr.listen(m)
                    text=sr.recognize_google(voice)

                    mixer.music.load('music2.mp3')
                    mixer.music.play()
                    text_list=text.split(' ')
                    for word in text_list:
                        if word.upper() in operations.keys():
                            l=findNumbers(text_list)
                            print(l)
                            result=operations[word.upper()](l[0],l[1]) #mul(5.0,6.0)
                            entryField.delete(0,END)
                            entryField.insert(END,result)

                        else:
                            pass


                except:
                    pass


        speak("mở máy tính")
        root = Tk()
        root.title('Smart Calculator')
        root.config(bg='dodgerblue3')
        root.geometry('680x486+100+100')

        logoImage = PhotoImage(file='logo.png')
        logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
        logoLabel.grid(row=0, column=0)

        entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
        entryField.grid(row=0, column=0, columnspan=8)

        micImage = PhotoImage(file='microphone.png')
        micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3'
                           ,command=audio)
        micButton.grid(row=0, column=7)

        button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                            "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                            "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                            "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                            "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
        rowvalue = 1
        columnvalue = 0
        for i in button_text_list:

            button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                            font=('arial', 18, 'bold'), activebackground='dodgerblue3', command=lambda button=i: click(button))
            button.grid(row=rowvalue, column=columnvalue, pady=1)
            columnvalue += 1
            if columnvalue > 7:
                rowvalue += 1
                columnvalue = 0

        root.mainloop()
    if n==n27:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        search_city=speak("nhập tên tỉnh thành phố:\n")
        search_city=get_text()
        url7='https://www.accuweather.com/vi/search-locations?query='+(search_city)
        print(webbrowser.open(url7))
    if n==n28:
        def go_to(x, y):
            t.up()
            t.goto(x, y)
            t.down()
        def head(x, y, r):
            go_to(x, y)
            t.speed(20)
            t.circle(r)
            leg(x, y)
        def leg(x, y):
            t.right(90)
            t.forward(180)
            t.right(30)
            t.forward(100)
            t.left(120)
            go_to(x, y - 180)
            t.forward(100)
            t.right(120)
            t.forward(100)
            t.left(120)
            hand(x, y)
        def hand(x, y):
            go_to(x, y - 60)
            t.forward(100)
            t.left(60)
            t.forward(100)
            go_to(x, y - 90)
            t.right(60)
            t.forward(100)
            t.right(60)
            t.forward(100)
            t.left(60)
            eye(x, y)
        def eye(x, y):
            go_to(x - 50, y + 130)
            t.right(90)
            t.forward(50)
            go_to(x + 40, y + 130)
            t.forward(50)
            t.left(90)
        def big_Circle(size):
            t.speed(20)
            for i in range(150):
                t.forward(size)
                t.right(0.3)
        def line(size):
            t.speed(20)
            t.forward(51 * size)
        def small_Circle(size):
            t.speed(20)
            for i in range(210):
                t.forward(size)
                t.right(0.786)
        def heart(x, y, size):
            go_to(x, y)
            t.left(150)
            t.begin_fill()
            line(size)
            big_Circle(size)
            small_Circle(size)
            t.left(120)
            small_Circle(size)
            big_Circle(size)
            line(size)
            t.end_fill()
        def main():
            t.pensize(2)
            t.color('red', 'pink')
            head(-120, 100, 100)
            heart(250, -80, 1)
            go_to(100, -300)
            t.write("To: Sự cùng tồn tại của trí tuệ và sắc đẹp ", move=True, align="left", font= (" Kaita ", 20, "normal"))
            t.done()
        main()
    if n==n29:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        bai_hat=speak('Xin mời chọn tên bài hát\n')
        bai_hat=get_text()
        url8='https://spotify-downloader.com/'
        print(webbrowser.open(url8))
        speak("Bài hát bạn yêu cầu đã được mở.")
    if n==n30:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        bai_hat=speak('Xin mời chọn tên bài hát\n')
        bai_hat=get_text()
        url9='https://music.youtube.com/search?q='+(bai_hat)
        print(webbrowser.open(url9))
        speak("Bài hát bạn yêu cầu đã được mở.")
    if n==n31:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        phim=speak('Xin mời chọn tên phim\n')
        phim=get_text()
        phim=(phim.replace(" ", "+"))
        url9='https://phimviet.tv/search/'+(phim)
        print(webbrowser.open(url9))
        speak("bộ phim bạn yêu cầu đã được mở.")
        
    if n==n32:
        Y=print("bot alex xin chao",name)
        #t=print("gõ search và click vào nút enter để tìm kiếm bài hat")
        #mysong = get_text()
        while True:
            #result = YoutubeSearch(mysong, max_results=10).to_dict()
            #if result:
                break
        phim=speak('Xin mời chọn tên phim\n')
        phim=get_text()
        url9='https://phimbo.us/tim-kiem/'+(phim)+"/"
        print(webbrowser.open(url9))
        speak("bộ phim bạn yêu cầu đã được mở.")
  
    
        

        
        
    
         
                                    
                                    
                        
                            
                        
                        




                    
