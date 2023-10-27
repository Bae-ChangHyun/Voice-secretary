import json
import requests
from datetime import datetime
import hmac, hashlib
from pytz import timezone
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# personal function
import variable_sotrage as var_s
from voice_module.tts import speak
from api_token_list import client_id,client_secret,client_key

def certificate():
    # timestamp 생성
    timestamp = datetime.now(timezone("Asia/Seoul")).strftime("%Y%m%d%H%M%S%f")[:-3] 
    # HMAC 기반 signature 생성
    signature = hmac.new(
        key=client_secret.encode("UTF-8"), msg= f"{client_id}:{timestamp}".encode("UTF-8"), digestmod=hashlib.sha256
    ).hexdigest()
    
    return client_key,signature,timestamp

def giga_genie(user_input):
    client_key,signature,timestamp = certificate()
     
    url = "https://aiapi.genielabs.ai/kt/nlp/daily-chat"
    headers = {
        "x-client-key":f"{client_key}",
        "x-client-signature":f"{signature}",
        "x-auth-timestamp":f"{timestamp}",
        "Content-Type": "application/json",
        "charset": "utf-8",
    } 
    print(var_s.context, var_s.context_utt_label)
    
    body = json.dumps({"user_id":"Chang hyun", "context":var_s.context, "context_utt_label":var_s.context_utt_label, "utterance":user_input}) 
    
    response = requests.post(url, data=body, headers=headers, verify=False)
    if response.status_code == 200:
        try:
            print(response.json())
            speak(response.json()['result'])
        except json.decoder.JSONDecodeError:
            print(f'json.decoder.JSONDecodeError occured.\nresponse.text: "{response.text}"')
    else:
        print(f"response.status_code: {response.status_code}\nresponse.text: {response.text}")