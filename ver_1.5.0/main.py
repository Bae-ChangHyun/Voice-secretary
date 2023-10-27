import speech_recognition as sr  # Speech-to-text

import pyttsx3 # Text-to-speech 

from gtts import gTTS # Text-to-speech (google)
from playsound import playsound

from stt_module.stt_speech_recognition import module1
from stt_module.stt_etri import module2
from stt_module.stt_whisper import module3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

engine = None  # 음성 엔진을 전역 변수로 설정

def initialize_speech_engine():
    global engine
    if engine is None:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            if "Microsoft David Desktop - English (United States)" in voice.name:
                engine.setProperty('voice', voice.id)
                break

def speak(text):
    initialize_speech_engine()  # 음성 엔진 초기화
    engine.say(text)
    engine.runAndWait()


def get_weather(user_input):
    # 네이버 날씨 웹페이지에서 날씨 정보 가져오기
    browser = webdriver.Chrome()
    browser.get("https://www.naver.com")
    browser.find_element(By.ID, 'query').click()        # 해당 id 클릭(검색창)
    browser.find_element(By.ID, 'query').send_keys(user_input) # 키보드 입력(날씨)
    browser.find_element(By.ID, 'search-btn').click() # 해당 id 클릭(검색창)
    try:
        weather_data = browser.find_element(By.CLASS_NAME, 'summary_list').text
        
        temp = weather_data.split(" ")[1]
        hum = weather_data.split(" ")[3]
        wind = weather_data.split(" ")[5]
        
        return (f"기온은 {temp}이며, 습도는 {hum}이고 바람은 {wind} 입니다.")
    except:
        speak("제가 잘못된 정보를 찾은 것 같습니다. 다시 한번 말씀해주세요.")
        user_input = stt_recorder(type)
        return speak(get_weather(user_input))
        
    
def stt_module(stt_type):
    whisper_type=None
    if(stt_type==1):recorder=module1
    elif(stt_type==2):recorder=module2
    elif(stt_type==3):
        recorder=module3
        print("medium이상을 권장합니다.")
        whisper_type=input("SELECT TYPE: tiny / base / small / medium / large: ")
    return recorder,whisper_type
    
stt_type=int(input("1. speech_recognition / 2. etri / 3. whisper 중 선택하세요: "))
stt_recorder, type=stt_module(stt_type)
speak("안녕하세요, 무엇을 도와드릴까요?")
while True:
    user_input = stt_recorder(type)
    print(user_input)
    if "날씨" in user_input:
        speak("어느 지역 날씨를 알려드릴까요?")
        user_input = stt_recorder(type)
        speak(get_weather(user_input))
    elif "종료" in user_input:
        speak("프로그램을 종료합니다.")
        break
    speak("계속 진행하시겠습니까?")
    