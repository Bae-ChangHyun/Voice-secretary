import urllib3
import json
import base64
import json
import speech_recognition as sr
import pyttsx3

# personal function
from api_token_list import etri_accessKey

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def module2(type):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("말하세요:")
        audio = recognizer.listen(source, timeout=30)
        print("음성 녹음이 완료되었습니다.")
        with open("tmp.wav", "wb") as f:
            f.write(audio.get_wav_data())
  
    file = open("tmp.wav", "rb")
    audioContents = base64.b64encode(file.read()).decode("utf8")
    file.close()
    
    requestJson = {    
          "argument": {
              "language_code": "korean",
              "audio": audioContents
          }
      } 
    http = urllib3.PoolManager()
    response = http.request(
          "POST",
          "http://aiopen.etri.re.kr:8000/WiseASR/Recognition",
          headers={"Content-Type": "application/json; charset=UTF-8","Authorization": etri_accessKey},
          body=json.dumps(requestJson)
      )
    try:
      data = json.loads(response.data.decode("utf-8", errors='ignore'))  
      text=  data['return_object']['recognized']
      print(f"인식된 텍스트: {text}")
      return text
    except:
      speak("죄송합니다. 음성을 인식하지 못했습니다.다시 말해주세요")
      return module2()
      
    
    
    


