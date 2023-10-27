import json
import requests
from api_token_list import access_token

def weather_kakako(weather_list):
    
    kcreds = {
    "access_token" : access_token
    }
    kheaders = {
        "Authorization": "Bearer " + kcreds.get('access_token')
    }

    kakaotalk_template_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    weather_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=용인 동백 날씨"

    # 날씨 정보 만들기 
    text = f"""\
    # 동백 날씨 정보
    기온 : {weather_list[0]}
    습도  : {weather_list[1]}
    바람 : {weather_list[2]}
    """

    # 텍스트 템플릿 형식 만들기
    template = {
    "object_type": "text",
    "text": text,
    "link": {
        "web_url": weather_url,
        "mobile_web_url": weather_url
    },
    "button_title": "날씨 상세보기"
    }

    # JSON 형식 -> 문자열 변환
    payload = {
        "template_object" : json.dumps(template)
    }

    # 카카오톡 보내기
    res = requests.post(kakaotalk_template_url, data=payload, headers=kheaders)

    if res.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))