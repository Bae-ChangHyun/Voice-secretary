
import pyttsx3 

# personal function
import variable_sotrage as var_s 

def initialize_speech_engine():
    global engine
    engine = None  # 음성 엔진을 전역 변수로 설정
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
    if('죄송' not in text): # 실패한 대화는 대화에 추가하지 않기 위함.
        var_s.context.append(text)
        var_s.context_utt_label.append('sys')