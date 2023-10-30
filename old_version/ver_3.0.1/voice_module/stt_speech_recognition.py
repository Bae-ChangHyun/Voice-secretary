import speech_recognition as sr

# personal function
from voice_module.tts import speak
from voice_module.record_voice import record
from variable_storage import context,context_utt_label

def module1(type):
    recognizer, audio = record()
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