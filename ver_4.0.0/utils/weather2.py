import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# personal function
from voice_module.tts import speak
import variable_storage as var_s
from utils.kakao_message_friend import weather_kakao

def driver_inits():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
    options.add_argument("no-sandbox")
    options.add_argument("disable-gpu")
    options.add_argument("--lang=ko_KR")
    return options

def get_weather(user_input):
    if '내일' in user_input:
        date = '내일'
    elif '모레' in user_input:
        date = '모레'
    else:
        date = '오늘'

    now = datetime.datetime.now()
    nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 기준')
    
    options=driver_inits()
    driver = webdriver.Chrome(options=options)
    while(1):
        try:
            # Open the Naver search page
            driver.get(f'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query={user_input}')
            
            driver.implicitly_wait(1)

            loc = driver.find_element(By.CLASS_NAME, 'title')
            temps = driver.find_element(By.CLASS_NAME, 'temperature_text')
            min_temps = driver.find_element(By.CLASS_NAME, 'lowest')
            max_temps = driver.find_element(By.CLASS_NAME, 'highest')
            am_rains = driver.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[5]/div[1]/div/div[2]/ul/li[1]/div/div[2]/span[1]/span/span')
            pm_rains = driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[5]/div[1]/div/div[2]/ul/li[1]/div/div[2]/span[2]/span/span')
            dusts = driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/ul/li[1]/a/span')
            summary = driver.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/p/span[1]')

            speak(f"{nowDate} {loc.text}의  기상정보입니다. {min_temps.text[5:]} {max_temps.text[5:]}이며, {temps.text[6:]}입니다. 오전 강수확률은 {am_rains.text}이고, 오후 강수확률은 {pm_rains.text}이며 미세먼지는 {dusts.text}입니다. 전체적으로 어제보다 {summary.text[:-2]}습니다.")
            weather_list=[loc.text, min_temps.text[5:], max_temps.text[5:],temps.text[6:],am_rains.text,pm_rains.text,dusts.text]
            try:
                weather_kakao(weather_list)
                return
            except:
                return
        except:
            speak("죄송합니다. 제가 잘못된 정보를 찾은 것 같습니다. 다시 한번 말씀해주세요.")
            user_input = var_s.stt_recorder(type)
            if('종료' in user_input):exit()
