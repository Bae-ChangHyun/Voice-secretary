import urllib3
import json
import base64
import torch 
import whisper
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch.functional")
import speech_recognition as sr

# personal function
import variable_storage as var_s 
import voice_module.stt_module as sst_model
import voice_module.tts_module as tts_model
from utils.api_token_list import etri_accessKey
from utils.make_db import shutdown

# 음성을 sst 모델에 넣기위하여 wav 파일로 저장
# 각 모델마다 지원형식(mp3,wav..)가 다르지만, wav는 모두 지원.
def record():
  recognizer = sr.Recognizer()
  microphone = sr.Microphone()
  with microphone as source:
      print("인식중...")
      recognizer.adjust_for_ambient_noise(source)
      audio = recognizer.listen(source, timeout=30)
      print("녹음이 완료되었습니다.")
      with open("./mp3/tmp.wav", "wb") as f:
          f.write(audio.get_wav_data())
  return recognizer,audio
     
# speech_recognition 라이브러리의 다양한 api들을 지원.
# google cloud, openai는 사전 api 발급이 필요
# os.environ['OPENAI_API_KEY'] = 'API_KEY_HERE'
# r(audio, model="small", language="chinese", **self.WHISPER_CONFIG)
# vosk, whisper은 사전 설치가 필요
# google은 기본적으로 사용 가능
# GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
#r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
def stt_speech_recognition():
  recognizer,audio = record()
  if(var_s.model_type=='google'):recognizers=recognizer.recognize_google
  elif(var_s.model_type=='Google_cloud_api'):recognizers=recognizer.recognize_google_cloud
  elif(var_s.model_type=='Vosk'):recognizers= recognizer.recognize_vosk
  elif(var_s.model_type=='whisper_local'):recognizers= recognizer.recognize_whisper
  elif(var_s.model_type=='Whisper_api'):recognizers= recognizer.recognize_whisper_api
  text = recognizers(audio, language="ko-KR")
  return text
  
# ETRI api 발급 필요 
def stt_etri_api():
  record()
  file = open("./mp3/tmp.wav", "rb")
  audioContents = base64.b64encode(file.read()).decode("utf8")
  file.close()
  requestJson = {"argument": {"language_code": "korean","audio": audioContents }} 
  http = urllib3.PoolManager()
  response = http.request(
        "POST",
        "http://aiopen.etri.re.kr:8000/WiseASR/Recognition",
        headers={"Content-Type": "application/json; charset=UTF-8","Authorization": etri_accessKey},
        body=json.dumps(requestJson)
    )
  text = json.loads(response.data.decode("utf-8", errors='ignore'))['return_object']['recognized']
  return text
  
# local에 설치된 whisper 필요(speech_regonition에 있는 whisper과 다르게 모델 타입 선택 가능)
def stt_whisper():
  record()
  model = whisper.load_model(var_s.model_type)
  result = model.transcribe("./mp3/tmp.wav",fp16=False)
  text=result["text"]
  return text
  
# sst모델을 사용하기 위한 초기설정 한번만 실행되면 됨.
# variable_storage에 영구적으로 sst모델과 타입이 저장됨.
def init(selected_model,select_type):
  if(selected_model=='Speech recognition'): var_s.stt_model=stt_speech_recognition
  elif(selected_model=='ETRI'): var_s.stt_model=stt_etri_api
  elif(selected_model=='Whisper'): var_s.stt_model=stt_whisper
  var_s.model_type=select_type
  return 0
  
def load_stt_model():
  # 선택한 모델에 따라 sst 진행
  try:
    text = var_s.stt_model()
    # 인식된 음성을 출력
    print(f"인식된 음성 명령: {text}")
    # 대화기록에 내용, 발화자 추가(genie 대화에)
    var_s.context.append(text)
    var_s.context_utt_label.append('user')
    if('종료' in text): 
      shutdown()
      tts_model.speak("프로그램을 종료합니다.")
      return 0
    else: return text
  except:
    return load_stt_model()