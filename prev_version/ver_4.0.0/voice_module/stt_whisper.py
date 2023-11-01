import torch 
import whisper
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch.functional")

# personal function
from voice_module.record_voice import record
import variable_storage as var_s 

def module3(whisper_type='medium'):
    record()
    model = whisper.load_model(whisper_type)
    result = model.transcribe("./mp3/tmp.wav",fp16=False)
    text=result["text"]
    var_s.context.append(text)
    print(f"인식된 텍스트: {text}")
    return text
