import speech_recognition as sr  # Speech-to-text

import pyttsx3 # Text-to-speech 

from gtts import gTTS # Text-to-speech (google)
from playsound import playsound

from stt_module.stt_speech_recognition import module1
from stt_module.stt_etri import module2
from stt_module.stt_whisper import module3
from genie_api import giga_genie
from context_manager import context,context_utt_label

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
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    context.append(text)
    context_utt_label.append('sys')
    
def record_audio_and_save_wav():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("말하세요:")
        audio = recognizer.listen(source, timeout=10)
        print("음성 녹음이 완료되었습니다.")
        # 음성을 WAV 파일로 저장
        with open("tmp.wav", "wb") as f:
            f.write(audio.get_wav_data())
        response=speach_to_text("tmp.wav")

        return response
        
def select_module(stt_type):
    whisper_type=None
    if(stt_type==1):recorder=module1
    elif(stt_type==2):recorder=module2
    elif(stt_type==3):
        recorder=module3
        print("medium이상을 권장합니다.")
        whisper_type=input("SELECT TYPE: tiny / base / small / medium / large: ")
    return recorder,whisper_type
    
stt_type=int(input("1. speech_recognition / 2. etri / 3. whisper 중 선택하세요: "))
stt_recorder, type=select_module(stt_type)

speak("안녕하세요, 무엇을 도와드릴까요?")

while True:
    user_input = stt_recorder(type)
    if('종료' in user_input):break
    context.append(user_input)
    context_utt_label.append('user')
    giga_genie(user_input)
    
    # if "날씨" in user_input:
    #     speak("어느 지역 날씨를 알려드릴까요?")
    #     user_input = stt_recorder(type)
    #     speak(get_weather(user_input))
    # elif "종료" in user_input:
    #     speak("프로그램을 종료합니다.")
    #     break
    # speak("계속 진행하시겠습니까?")
    