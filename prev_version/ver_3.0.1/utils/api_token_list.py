import json,hmac, hashlib, requests
from datetime import datetime
from pytz import timezone

# genie -> 일상 채팅
def certificate():
    timestamp = datetime.now(timezone("Asia/Seoul")).strftime("%Y%m%d%H%M%S%f")[:-3] 
    signature = hmac.new(
        key=client_secret.encode("UTF-8"), msg= f"{client_id}:{timestamp}".encode("UTF-8"), digestmod=hashlib.sha256
    ).hexdigest()
    
    return client_key,signature,timestamp

client_id="본인 Client id"
client_secret="본인 Client secret"
client_key=""

# kakao -> 날씨 정보 보내기
def get_new_token(refresh_token):
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type" : "refresh_token",
        "client_id"  : rest_api,
        "refresh_token" : refresh_token
    }
    response = requests.post(url, data=data)
    access_token = response.json().get('access_token')
    return access_token
    
rest_api="본인 rest api"
access_token = "본인 access token"
refresh_token = "본인 refresh token"

# etri
etri_accessKey = "본인 etri access key"

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

