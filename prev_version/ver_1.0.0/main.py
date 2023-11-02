""" 
단순하 입력받은 음성을 텍스트로 바꾸고,
날씨 단어가 포함되면 크롤링하는 버전
"""
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("말하세요:")
        audio = recognizer.listen(source, timeout=30)
    try:
        text = recognizer.recognize_google(audio, language="ko-KR")  # 한국어 인식
        print(f"인식된 텍스트: {text}")
        return text
    except sr.UnknownValueError:
        speak("죄송합니다. 음성을 인식하지 못했습니다.다시 말해주세요")
        return ""
    except sr.RequestError as e:
        speak("죄송합니다. 음성을 인식하지 못했습니다.다시 말해주세요")
        return ""

def get_weather(user_input):
    # 네이버 날씨 웹페이지에서 날씨 정보 가져오기
    browser = webdriver.Chrome()
    browser.get("https://www.naver.com")
    browser.find_element(By.ID, 'query').click()        # 해당 id 클릭(검색창)
    browser.find_element(By.ID, 'query').send_keys(user_input) # 키보드 입력(날씨)
    browser.find_element(By.ID, 'search-btn').click() # 해당 id 클릭(검색창)
    weather_data = browser.find_element(By.CLASS_NAME, 'summary_list').text
    
    temp = weather_data.split(" ")[1]
    hum = weather_data.split(" ")[3]
    wind = weather_data.split(" ")[5]
    
    return (f"기온은 {temp}이며, 습도는 {hum}이고 바람은 {wind} 입니다.")

engine = None 
speak("안녕하세요, 무엇을 도와드릴까요?")
while True:
    user_input = recognize_speech()
    if "날씨" in user_input:
        speak("어느 지역 날씨를 알려드릴까요?")
        user_input = recognize_speech()
        speak(get_weather(user_input))
    elif "종료" in user_input:
        speak("프로그램을 종료합니다.")
        break