import time
import sys
from urllib.parse import quote

# personal function
import variable_storage as var_s

from voice_module.tts import speak
from voice_module.stt_speech_recognition import module1
from voice_module.stt_etri import module2
from voice_module.stt_whisper import module3

from utils.genie_conversation import get_conversation
from utils.weather2 import get_weather
from utils.make_db import get_db_connection,create_table,add_log

def system_order(user_input):
    if '날씨' in user_input:
        user_input = quote(user_input, safe='')
        print(user_input)
        get_weather(user_input)
        time.sleep(1)
        return 1
    else: return 0

def select_module(selected_model):
    if selected_model == 'speech_recognition':
        recorder = module1
    elif selected_model == 'etri':
        recorder = module2
    elif selected_model == 'whisper':
        recorder = module3
        print("medium 이상을 권장합니다.")
    return recorder

if __name__ == '__main__':
    # 서버에서 클릭한 값들을 받아옴
    if len(sys.argv) == 3:
        selected_model = sys.argv[1]
        model_version = sys.argv[2]

    var_s.stt_recorder= select_module(selected_model)
    var_s.type=model_version

    while True:
        speak("안녕하세요, 무엇을 도와드릴까요?")
        user_input = var_s.stt_recorder(var_s.type)
        if '종료' in user_input:
            var_s.context_utt_label.append('user')
            speak("다음에 또 뵙겠습니다.")
            # db에 대화기록 업데이트
            get_db_connection()
            create_table()
            add_log(var_s.context, var_s.context_utt_label)
            break
        var_s.context_utt_label.append('user')
        # 현재 날씨 기능을 제외하고는 지니 일상대화 api 이용.
        if system_order(user_input) != 1:
            get_conversation(user_input)

