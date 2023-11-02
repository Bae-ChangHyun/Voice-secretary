import time
import sys
from urllib.parse import quote

# personal function
import variable_storage as var_s

import voice_module.tts_module as tts_model
import voice_module.stt_module as sst_model

from utils.genie_conversation import get_conversation
from utils.weather2 import get_weather

def system_order(user_input):
    if '날씨' in user_input:
        user_input = quote(user_input, safe='')
        print(user_input)
        get_weather(user_input)
        time.sleep(1)
        return 1
    else: return 0

if __name__ == '__main__':

    # 서버에서 받아온 모델,타입을 설정해줌.
    sst_model.init(sys.argv[1], sys.argv[2])
    
    while(1):
        print(var_s.context, var_s.context_utt_label)
        user_input = sst_model.load_stt_model()
        if('비서야' in user_input):
            tts_model.speak("안녕하세요, 무엇을 도와드릴까요?")
            while(1):
                user_input = sst_model.load_stt_model()
                # 현재 날씨 기능을 제외하고는 지니 일상대화 api 이용.
                if(user_input==0):break
                if system_order(user_input) != 1: get_conversation(user_input)        
        if(user_input==0):break


