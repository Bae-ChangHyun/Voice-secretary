from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# personal function
from voice_module.tts import speak
import variable_storage as var_s
from utils.kakao_message_friend import weather_kakako

def get_weather(user_input):
    while(1):
        browser = webdriver.Chrome()
        browser.get("https://www.naver.com")
        browser.find_element(By.ID, 'query').click()       
        browser.find_element(By.ID, 'query').send_keys(user_input) # 키보드 입력(날씨)
        browser.find_element(By.ID, 'search-btn').click() 
        try:
            weather_data = browser.find_element(By.CLASS_NAME, 'summary_list').text  
            temp = weather_data.split(" ")[1]
            hum = weather_data.split(" ")[3]
            wind = weather_data.split(" ")[5][:-1]
            speak(f"오늘 기온은 {temp}이며, 습도는 {hum}이고 바람은 {wind} 입니다.")
            var_s.context.append(user_input)
            var_s.context_utt_label.append('user')
            try:
                weather_kakako([temp,hum,wind])
            except:return
            break
        except:
            speak("죄송합니다. 제가 잘못된 정보를 찾은 것 같습니다. 다시 한번 말씀해주세요.")
            user_input = var_s.stt_recorder(type)
        

def weather_info():
    speak("어느 지역 날씨를 알려드릴까요?")
    user_input = var_s.stt_recorder(type)
    get_weather(user_input)
    