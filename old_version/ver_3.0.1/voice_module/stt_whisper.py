import torch 
import whisper
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch.functional")

# personal function
from voice_module.record_voice import record

def module3(whisper_type='medium'):
    record()
    model = whisper.load_model(whisper_type)
    result = model.transcribe("./mp3/tmp.wav",fp16=False)
    text=result["text"]
    print(f"인식된 텍스트: {text}")
    return text
