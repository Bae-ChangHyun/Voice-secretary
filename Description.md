# Readme

제작: Bae Chang Hyun(제작 기간 2023.10.26~2023.10.31)

아래의 필수 발급, 선택 발급을 모두 설치하시면 모든 기능을 이용하실 수 있으며, 

필수 발급만 설치하면 날씨 카카오톡 메세지 전송, stt 모델 선택이 불가 기능이 불가합니다.

프로그램은 app.py를 실행하여 실행합니다.

# 1. 현재 메인 기능(필수설치+선택설치 가정)

- stt(speech to text)모델 선택 가능 → speech_recognition 라이브러리, ETRI api, openai whisper(로컬설치)

→ 선택 발급 미설치시, speech recognition만 가능.(현재 speech recognition도 구글의 소스로 이용하고 있고 추후 추가 예정)

→ ETRI는 인식률이 낮고, 하루 API호출 건수가 제한되어 있어 추후 삭제 예정

→ Open AI의 Whisper이 가장 인식률이 좋으나, api는 유료여서 로컬에 설치하여 사용하도록 구성(추후 api 버전 추가 예정)

- 날씨 키워드

→ 사용자의 대화에 “날씨”가 들어가면, 해당 대화를 네이버에 query로 입력하여 날씨를 받아옴. 

→ 단, 사용자가 날씨를 묻는건지, 날씨에 대한 얘기를 하던 무조건 호출 (추후 의도파악 api등을 이용하여 구분 예정)

→ 카카오톡 토큰이 정상적으로 발급되어있고, 세팅이 되어있으면 지정된 사용자들에게 날씨를 전송.

- 일상채팅 기능

→ genie labs의 일상채팅을 이용하여 키워드가 들어가지 않은 대화시, 일상채팅을 시도. 

→ 첫 답변은 잘하지만, 이전 대화기록을 인자로 넣어줘도 대화가 매끄럽지 않고 이전 대화 내용을 인식 못함.(추후 api 변경 혹은 버그가 있으면 수정 예정)

- flask를 이용한 웹 ui

→ flask를 이용하여 서버를 열고, 웹 페이지로 구현함. 

→ 웹페이지 내에서 모델 선택하고 프로그램이 실행되도록 구현하였음.

# 2. 추후 추가 예정

- speech recognition의 다른 api들도 선택 가능하도록 변경
- open ai의 whiper을 사용자들이 사용할 수 있도록, 로컬 설치가 아닌 api로 변경 예정(api는 본인 발급)
- 의도파악 혹은 일상채팅 api를 변경 혹은 모델을 직접 prompt tuning하여 더 매끄러운 대화가 진행되도록 변경 예정
- 날씨 외의 다른 메인 키워드들 등록 예정(주식, 뉴스 등)
- 웹 디자인, 기능 추가

# 3. 사용 전 필수 발급

## 1. Genie labs api 발급

: 본 voice secretary는 genie labs의 일상대화 api를 통해 대화를 하도록 구성되었음. 

메인키워드(날씨 등)외에는 모두 genie labs api를 이용하여 대화를 진행하도록 프로그래밍. 아래 발급절차를 통해 발급받고, utils-api_token_list.py에 저장해야함. 이 키들은 모두 local에만 저장됨.

### genie labs api 발급

1. KT GenieLabs에 접속하여, 회원가입 

[](https://genielabs.ai/main/genielabs/index)

1. 상단의 API→NLP API로 이동하여 일상채팅 API를 클릭.

![Untitled](Readme%200e77a7118c354090b0b080fcf9c9dcd5/Untitled.png)

1. API 사용신청 버튼을 클릭후, 게시판에 형식에 맞게 신청하여 API 발급

![Untitled](Readme%200e77a7118c354090b0b080fcf9c9dcd5/Untitled%201.png)

1. API발급이 완료되었으면, 화면 상단의 Developer Console의 Developer 클릭후 이동하여 

![Untitled](Readme%200e77a7118c354090b0b080fcf9c9dcd5/Untitled%202.png)

1. 화면 위의 Client id와 Client secret을 복사하여, 프로젝트 디렉토리의 utils-api_token_list.py에 genie에 해당하는 부분에 입력하고, 아래 My APIs에서 일상채팅 활성화 후 저장

![Untitled](Readme%200e77a7118c354090b0b080fcf9c9dcd5/Untitled%203.png)

![Untitled](Readme%200e77a7118c354090b0b080fcf9c9dcd5/Untitled%204.png)

![Untitled](Readme%200e77a7118c354090b0b080fcf9c9dcd5/Untitled%205.png)

1. id와 secret만 입력해놓으면, 추후 함수 내에서 certificate가 자동으로 실행되고, 프로그램이 정상 실행됨.
2. 본인의 api 사용량은 genie labs 홈페이지의 Developer Console의 Dashboard에서 확인할 수 있음.

![Untitled](Readme%200e77a7118c354090b0b080fcf9c9dcd5/Untitled%206.png)

![Untitled](Readme%200e77a7118c354090b0b080fcf9c9dcd5/Untitled%207.png)

## 2. requirements.txt

: gpu 관련한 라이브러리를 제외한 모든 라이브러리를 설치.

가상환경을 생성하고, 아래 코드를 이용하여 모든 라이브러리 설치

[requirements.txt](Readme%200e77a7118c354090b0b080fcf9c9dcd5/requirements.txt)

```python
pip install -r requirements.txt
```

# 4. 사용 전 선택 발급

## 1. kakao access token 발급

: 본 voice secretary는 키워드(날씨)를 입력했을 때, 날씨 정보를 지정된 사용자에게 카카오톡 메세지로 전송. 이를 위해 kakao api를 사용하게 됨. 

자세한 발급절차는 아래 링크에 설명되있음. 

발급받은 후, rest_api, access_token, refresh_token을 모두 디렉토리의 utils-api_token_list.py에 저장해야함. 이 키들은 모두 local에만 저장.

[카카오톡 access token 발급받기](https://changsroad.tistory.com/349)

이후 개인에게 보내기 ,친구에게 보내기 또한 추가설정을 해줘야만 가능.

아래 절차들을 통해 kakao developers에서 미리 세팅을 해줘야 정상적으로 메세지가 전송됨.

[카카오톡 api로 나에게 메세지 보내기](https://changsroad.tistory.com/366)

[카카오톡 api로 친구한테 메세지 보내기](https://changsroad.tistory.com/367)

## 2. etri sst api key 발급

ETRI 한국전자통신연구원에서 제공되는 한국어 인식 API로 일일 1000건 사용 가능.

아래 링크에서 API키를 신청하여 발급받은 후, 디렉토리내의 utils-api_token_list.py에 넣어주면 정상적으로 실행가능.

[AI API/DATA](https://aiopen.etri.re.kr/)

## 3. Whisper 설치

open ai sst 모델인 whisper. 버전에 따라 매우 우수한 성능을 보이며 api도 제공되지만, 유료이며 본 프로젝트 특성상 개인 비서용으로 제작되어 local에 whisper을 직접 설치하여 프로그래밍하였음.

아래 링크에서 whisper을 정상적으로 설치하고, 프로젝트 가상환경에 해당 라이브러리 및 gpu가 사용가능한 환경을 만들어놔야 정상적으로 실행가능. 

[Open ai - Whisper 설치](https://changsroad.tistory.com/361)