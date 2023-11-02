import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# personal function
import variable_storage as var_s
import voice_module.tts_module as tts_model
from utils.api_token_list import certificate

def get_conversation(user_input):
    client_key,signature,timestamp = certificate()
     
    url = "https://aiapi.genielabs.ai/kt/nlp/daily-chat"
    headers = {
        "x-client-key":f"{client_key}",
        "x-client-signature":f"{signature}",
        "x-auth-timestamp":f"{timestamp}",
        "Content-Type": "application/json",
        "charset": "utf-8",
    } 
    # 지금까지 저장된 대화 내용 및 발화자->추후 db 기록
    
    body = json.dumps({"user_id":"User", "context":var_s.context, "context_utt_label":var_s.context_utt_label, "utterance":user_input}) 
    
    response = requests.post(url, data=body, headers=headers,verify=False)
    if response.status_code == 200: tts_model.speak(response.json()['result'])
    else: print(f"response.status_code: {response.status_code}\nresponse.text: {response.text}")