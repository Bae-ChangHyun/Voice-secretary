import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# personal function
import variable_sotrage as var_s
from genie_api import giga_genie
from voice_module.tts import speak
from voice_module.stt_speech_recognition import module1
from voice_module.stt_etri import module2
from voice_module.stt_whisper import module3

from utils.weather import weather_info

def system_order(user_input):
    if('날씨' in user_input):
        weather_info()
        time.sleep(1)
        return 1
    else:return 0

def select_module(stt_type):
    whisper_type=None
    if(stt_type==1):recorder=module1
    elif(stt_type==2):recorder=module2
    elif(stt_type==3):
        recorder=module3
        print("medium이상을 권장합니다.")
        whisper_type=input("SELECT TYPE: tiny / base / small / medium / large: ")
    return recorder,whisper_type

var_s.stt_recorder,var_s.type = select_module(stt_type=int(input("1. speech_recognition / 2. etri / 3. whisper 중 선택하세요: ")))
        
speak("안녕하세요, 무엇을 도와드릴까요?")
while True:
    user_input = var_s.stt_recorder(type)
    if('종료' in user_input):
        speak("다음에 또 뵙겠습니다.")
        break
    #context.append(user_input)
    var_s.context_utt_label.append('user')
    if(system_order(user_input)!=1):giga_genie(user_input)