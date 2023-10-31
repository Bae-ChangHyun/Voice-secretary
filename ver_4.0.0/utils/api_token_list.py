import requests
import json
from datetime import datetime
from pytz import timezone
import hmac, hashlib
# genie -> 일상대화 api

def certificate():
    # timestamp 생성
    timestamp = datetime.now(timezone("Asia/Seoul")).strftime("%Y%m%d%H%M%S%f")[:-3] 
    # HMAC 기반 signature 생성
    signature = hmac.new(
        key=client_secret.encode("UTF-8"), msg= f"{client_id}:{timestamp}".encode("UTF-8"), digestmod=hashlib.sha256
    ).hexdigest()
    
    return client_key,signature,timestamp

client_id="glabs_d081648d33d8c37dd95997205b429d811b93402f8932d09d0afbfcf32ec3c6c5"
client_secret="8665f1f2405d2c524da6bdd873b661d65d79f6289f11d606c8b0912f138805e2"
client_key="63f23e2c-83d2-5635-8306-431f09a2ebf7"

# kakao

def get_new_token(refresh_token):
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type" : "refresh_token",
        "client_id"  : "e6a4aba99b309bc3cff38a5f20bf40d2",
        "refresh_token" : refresh_token
    }
    response = requests.post(url, data=data)
    access_token = response.json().get('access_token')
    return access_token
    
rest_api="e6a4aba99b309bc3cff38a5f20bf40d2"
access_token = "byjMwOGuRBovXKeQvb45qF4_MS8TGCVTT9sKPXMYAAABi34fnPKIenTzhLqDRQ"
refresh_token = "BBB3bE7ork_xRk09T_lEzHlvIDit7ndpxYEKKiWOAAABi3EiXjeIenTzhLqDRQ"

# region

# url = "https://kauth.kakao.com/oauth/token"

# data = {
#     "grant_type" : "authorization_code",
#     "client_id" : rest_api,
#     "redirect_uri" : "http://localhost:5000",
#     "code"         : code
# }
# response = requests.post(url, data=data)

# tokens = response.json()

# with open("kakao_token.json", "w") as fp:
#     json.dump(tokens, fp)
# print(tokens)

# endregion

# etri
etri_accessKey = "a88b7328-a99b-4e37-b9c4-f0a5e57cd3f8"