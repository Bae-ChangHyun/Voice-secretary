import pyttsx3 

# personal function
import variable_storage as var_s 

def initialize_speech_engine():
    global engine
    engine = None  # 음성 엔진을 전역 변수로 설정
    if engine is None:
        engine = pyttsx3.init()
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    engine.say(text)
    engine.runAndWait()
    var_s.context.append(text)
    var_s.context_utt_label.append('sys')