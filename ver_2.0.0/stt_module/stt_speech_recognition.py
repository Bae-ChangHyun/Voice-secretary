import speech_recognition as sr
import pyttsx3
from context_manager import context,context_utt_label

context=[]

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    context.append(text)
    context_utt_label.append('sys')

def module1(type):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("말하세요:")
        audio = recognizer.listen(source, timeout=30)
    try:
        text = recognizer.recognize_google(audio, language="ko-KR")  # 한국어 인식
        context.append(text)
        print(f"인식된 텍스트: {text}")
        return text
    except sr.UnknownValueError:
        speak("죄송합니다. 음성을 인식하지 못했습니다.다시 말해주세요")
        return module1(type)
    except sr.RequestError as e:
        speak("죄송합니다. 음성을 인식하지 못했습니다.다시 말해주세요")
        return module1(type)