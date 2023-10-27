import torch 
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="torch.functional")
import whisper
import speech_recognition as sr


def module3(whisper_type='medium'):
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("말하세요:")
        audio = recognizer.listen(source, timeout=30)
        print("음성 녹음이 완료되었습니다.")
        with open("tmp.wav", "wb") as f:
            f.write(audio.get_wav_data())
    
    model = whisper.load_model(whisper_type)
    result = model.transcribe("tmp.wav",fp16=False)
    text=result["text"]
    return text
