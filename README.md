## Notice
- 데이터분석, 머신러닝 하다가 질릴 때 심심풀이로 정성들여 만든 프로그램들입니다.
- 프로그램 주제, 기능 ,ui 까지 전부 혼자 구현한 개인 프로젝트입니다. 
- 혼자서 열심히 기능도 생각해보고, 오류도 찾아서 수정했지만 아직 부족한점이 많으니 사용하시게 된다면 많은 피드백 부탁드립니다.
- 이상입니다. 
- 더 자세한 프로젝트 내용 및 설명은 개인블로그를 참조해주시면 감사하겠습니다. 
[개인블로그](https://changsroad.tistory.com/category/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EC%9D%8C%EC%84%B1%EB%B9%84%EC%84%9C)


# [프로젝트 기간 10/26~11/01]
- 추가 되었으면 하는 기능이 있는지 알려주시면, 추가해보겠습니다.
- 많은 디버깅을 하며, 오류를 잡았지만, 그럼에도 오류가 발생하는 부분이 있다면 알려주시면 감사하겠습니다.
  
- 아래의 필수 발급, 선택 발급을 모두 설치하시면 모든 기능을 이용하실 수 있으며, <br>
 필수 발급만 설치하면 날씨 카카오톡 메세지 전송, stt 모델 선택이 불가 기능이 불가합니다.
- 프로그램은 app.py를 실행하여 실행합니다.
- 현재는 사전 세팅이 많이 필요하며, 키워드가 날씨만 지정되어있어 기능이 부족하지만, 일상대화 및 ui를 구현한데 의의를 둠.
- 추후에 다양한 기능을 추가해보겠습니다. 

### 실행 이미지
![스크린샷 2023-11-03 115238](https://github.com/Bae-ChangHyun/Voice-secretary/assets/48899047/ce714c11-5442-4829-84a0-a3da763e1dea)
![스크린샷 2023-11-03 143419](https://github.com/Bae-ChangHyun/Voice-secretary/assets/48899047/a748397e-24f2-4a3a-ac80-1ec1a0cb6ac8)
![스크린샷 2023-11-03 115249](https://github.com/Bae-ChangHyun/Voice-secretary/assets/48899047/644382b3-0a70-412e-a910-d90360ef4671)
![스크린샷 2023-11-03 115349](https://github.com/Bae-ChangHyun/Voice-secretary/assets/48899047/1c872014-72c8-4f00-9e28-46ef9196f8d0)
![스크린샷 2023-11-03 121654](https://github.com/Bae-ChangHyun/Voice-secretary/assets/48899047/c00a7c37-0b1b-4797-bf2e-bcee78a215bc)


<details>
  <summary><h1>0. Update log(추후 작성 예정)</h1></summary>
</details>

# (Ver 4.0.1 기준. 2023.11.01)

<details> 
  <summary><h1>1. 현재 메인 기능(필수 설치+선택 설치 가정)</h1></summary>
  
  1. stt(speech to text)모델 선택 가능 → 
  : Speech Recognition liabrary : google speech recoginition,  Vosk, whisper api, whisper local, google cloud speech
  : ETRI api 
  : Openai whisper(로컬설치)

    → speech recognition의 google speech recognition는 기본 사용 가능, vosk / whisper local 은 사전설 치, 나머지 사전 api 발급 필요
  
    → ETRI는 인식률이 낮고, 하루 API호출 건수가 제한되어 있어 추후 삭제 예정

  2. 날씨 알림

    → 사용자의 대화에 “날씨”가 들어가면, 해당 대화를 네이버에 query로 입력하여 날씨를 받아옴. 
  
    → 단, 사용자가 날씨를 묻는건지, 날씨에 대한 얘기를 하던 무조건 호출 (추후 의도파악 api등을 이용하여 구분 예정)
  
    → 카카오톡 토큰이 발급 및 사전 세팅이 되어있으면 지정된 사용자들에게 날씨를 전송.

  3. 일상 대화

    → genie labs의 일상채팅 api를 이용하여 키워드(날씨)가 들어가지 않은 음성 인식시, 일상 채팅을 시도. 
  
    → 첫 답변은 잘하지만, 이전 대화기록을 인자로 넣어줘도 대화가 매끄럽지 않고 이전 대화 내용을 인식 못함.(추후 api 변경 혹은 버그가 있으면 수정 예정)

  4. flask를 이용한 웹 ui

    → flask를 이용하여 서버를 열고, 웹 페이지로 구현함. 
  
    → 웹페이지 내에서 모델 선택하고 프로그램이 실행되도록 구현하였음.

  5. 대화 기록 저장
     → sqlite3를 이용하여, 대화기록을 저장(추후 대화기록을 결과창에서 확인 혹은 다운로드 가능하도록 수정 예정)

  </details>

<details> 
  <summary><h1>2. 추후 추가 예정</h1></summary>
  1. speech recognition의 다른 api들도 사용할 수 있도록 코드는 수정해놓았지만, api사전발급이 필요하여 block 처리해둠 <br>
  네이버의 clova나 apple등의 다른 api도 알아보고 있음. 
  
  2. 의도파악 혹은 일상채팅 api를 변경 혹은 모델을 직접 prompt tuning하여 더 매끄러운 대화가 진행되도록 변경 예정
     
  3. 날씨 외의 다른 메인 키워드들 등록 예정(주식, 뉴스 등)
     
  4.대화 기록 db을 result에서 확인하거나, 다운로드 받을 수 있도록 수정 예정(현재는 디렉토리에 자동저장됨) 
   
  5. 웹 디자인, 기능 추가
 </details>

<details> 
  <summary><h1>3. 사용 전 필수 발급</h1></summary>
    <details>
    <summary><h2>1. Genie labs api 발급</h2></summary>
      : 본 voice secretary는 genie labs의 일상대화 api를 통해 대화를 하도록 구성되었음.<br>  
    메인 키워드(날씨 등)외에는 모두 genie labs api를 이용하여 대화를 진행하도록 프로그래밍. <br>  
    아래 발급절차를 통해 발급받고, utils-api_token_list.py에 저장해야함. 이 키들은 모두 local에만 저장됨.<br>  
      
    1-1. [KT GenieLabs에 접속하여, 회원가입 ](https://genielabs.ai/main/genielabs/index)
    
    1-2. [상단의 API→NLP API로 이동하여 일상채팅 API를 클릭.]
    ![Untitled](https://github.com/Bae-ChangHyun/toy_project/assets/48899047/e2ada1d0-e505-41a1-988b-3ca9a5a4cb22)
  
    1-3. API 사용신청 버튼을 클릭후, 게시판에 형식에 맞게 신청하여 API 발급
   ![Untitled 1](https://github.com/Bae-ChangHyun/toy_project/assets/48899047/2c522a2d-be6e-4e6e-a31c-3aaa3eeb181e)
  
    1-4. API발급이 완료되었으면, 화면 상단의 Developer Console의 Developer 클릭후 이동하여
   화면 위의 Client id와 Client secret을 복사하여, 프로젝트 디렉토리의 utils-api_token_list.py에 genie에 해당하는 부분에 입력하고, 아래 My APIs에서 일상채팅 활성화 후 저장
   ![Untitled 1](https://github.com/Bae-ChangHyun/toy_project/assets/48899047/bfabbdb8-6051-457d-8403-a125cf38080e)
   ![Untitled 3](https://github.com/Bae-ChangHyun/toy_project/assets/48899047/d3519a13-2c49-4f76-9dcc-ee9a2a48c971)
   ![Untitled 4](https://github.com/Bae-ChangHyun/toy_project/assets/48899047/43927863-3380-4600-9a30-abdbc23eeea2)
   ![Untitled 5](https://github.com/Bae-ChangHyun/toy_project/assets/48899047/aac19a23-5629-4e19-be88-cd12d113a844)
   
    1-5. id와 secret만 입력해놓으면, 추후 함수 내에서 certificate가 자동으로 실행되고, 프로그램이 정상 실행됨.
  
    1-6  본인의 api 사용량은 genie labs 홈페이지의 Developer Console의 Dashboard에서 확인할 수 있음.
   ![Untitled 6](https://github.com/Bae-ChangHyun/toy_project/assets/48899047/68670a93-a01d-4ea8-95e1-ab5226670f64)
   ![Untitled 7](https://github.com/Bae-ChangHyun/toy_project/assets/48899047/b19b6452-3a4d-428e-b7bb-aaa04cd2e065)
   
   </details>
   <details>
   <summary><h2>2. requirements.txt</h2></summary>
    gpu 관련한 라이브러리를 제외한 모든 라이브러리를 설치.<br> 
    가상환경을 생성하고, 아래 코드를 이용하여 모든 라이브러리 설치<br> 
    pip install -r requirements.txt <br>
   </details>
</details>

<details> 
  <summary><h1>4. 사용 전 선택 발급</h1></summary>
  <details>
    <summary><h2>1. kakao access token 발급</h2></summary>
    : 본 voice secretary는 키워드(날씨)를 입력했을 때, 날씨 정보를 지정된 사용자에게 카카오톡 메세지로 전송. <br> 이를 위해 kakao api를 사용하게 됨. <br> 
    
  자세한 발급절차는 아래 링크에 설명되있음. <br> 
    
  발급받은 후, rest_api, access_token, refresh_token을 모두 디렉토리의 utils-api_token_list.py에 저장해야함. 이 키들은 모두 local에만 저장.<br> 
    
  [카카오톡 access token 발급받기](https://changsroad.tistory.com/349)
    
  이후 개인에게 보내기 ,친구에게 보내기 또한 추가설정을 해줘야만 가능.<br> 
    
  아래 절차들을 통해 kakao developers에서 미리 세팅을 해줘야 정상적으로 메세지가 전송됨.<br> 
    
  [카카오톡 api로 나에게 메세지 보내기](https://changsroad.tistory.com/366)
    
  [카카오톡 api로 친구한테 메세지 보내기](https://changsroad.tistory.com/367)
  </details>

  <details>
    <summary><h2>2. ETRI sst api key 발급</h2></summary>
  
  ETRI 한국전자통신연구원에서 제공되는 한국어 인식 API로 일일 1000건 사용 가능.<br> 
    
  아래 링크에서 API키를 신청하여 발급받은 후, 디렉토리내의 utils-api_token_list.py에 넣어주면 정상적으로 실행가능.<br> 
    
  [AI API/DATA](https://aiopen.etri.re.kr/)
  </details>
  <details>
    <summary><h2>3. Whisper 설치</h2></summary>
  open ai sst 모델인 whisper. 버전에 따라 매우 우수한 성능을 보이며 api도 제공되지만, 유료이며 본 프로젝트 특성상 개인 비서용으로 제작되어 local에 whisper을 직접 설치하여 프로그래밍하였음.
  
  아래 링크에서 whisper을 정상적으로 설치하고, 프로젝트 가상환경에 해당 라이브러리 및 gpu가 사용가능한 환경을 만들어놔야 정상적으로 실행가능. 
  
  [Open ai - Whisper 설치](https://changsroad.tistory.com/361)
  </details>
</details>
