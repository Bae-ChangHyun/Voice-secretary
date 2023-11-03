import json
import requests
from utils.api_token_list import refresh_token
from utils.api_token_list import get_new_token

def get_friend_info(kheaders):
    url = "https://kapi.kakao.com/v1/api/talk/friends?limit=3&order=asc" #친구 목록 가져오기
    result = json.loads(requests.get(url, headers=kheaders).text)
    friends_list = result.get("elements")
    freind_names=[i.get('profile_nickname') for i in friends_list]
    friend_ids=[i.get('uuid') for i in friends_list]
    return freind_names,friend_ids
    
def weather_kakao(weather_list):
    
    access_token=get_new_token(refresh_token)
   
    kcreds = {"access_token" : access_token}
    kheaders = {"Authorization": "Bearer " + kcreds.get('access_token')}

    url_mine = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    url_friend ="https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    weather_url = f"https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query={weather_list[0]} 날씨"

    friend_names,friend_ids = get_friend_info(kheaders)

    # 메세지 내용
    text = f"""\
    # {weather_list[0]} 날씨 정보
    현재 기온: {weather_list[3]}
    최저,최고 기온: {weather_list[1]}, {weather_list[2]}
    오전,오후 강수확률:{weather_list[4]}, {weather_list[5]}
    미세먼지 : {weather_list[6]}
    """
    template = {"object_type": "text","text": text,
                "link": {"web_url": weather_url,"mobile_web_url": weather_url},
                "button_title": "날씨 상세보기"}
    
    data_mine = {"template_object" : json.dumps(template)}
    res = requests.post(url_mine, data=data_mine, headers=kheaders)
    if res.json().get('result_code') == 0: print('나에게 전송 성공.')
    else: print('나에게 전송 실패. Error : ' + str(res.json()))
    
    data_friend = {'receiver_uuids': json.dumps(friend_ids) , "template_object" : json.dumps(template)}
    res2 = requests.post(url_friend, data=data_friend, headers=kheaders)
    if len(res2.json().get('successful_receiver_uuids'))>=1 : print("친구들에게 전송 성공")
    else: print("친구들에게 전송 실패. error: " + str(res2.json()))
