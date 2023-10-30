import speech_recognition as sr

def record():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("말하세요:")
        audio = recognizer.listen(source, timeout=30)
        print("녹음이 완료되었습니다.")
        with open("./mp3/tmp.wav", "wb") as f:
            f.write(audio.get_wav_data())
    return recognizer,audio   