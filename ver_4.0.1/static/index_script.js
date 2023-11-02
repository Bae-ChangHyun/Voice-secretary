// <!-- index_script.js -->
document.addEventListener('DOMContentLoaded', function() {
    const modelselect = document.getElementById('model');

    const whisperOptions = document.getElementById('whisper-options');
    const whisperVersionInputs = document.querySelectorAll('input[name="whisper_model"]');

    const srOptions = document.getElementById('sr-options');
    const srVersionInputs = document.querySelectorAll('input[name="speech_recognition_model"]');

    const modelDescription = document.getElementById('model-description');

    modelselect.addEventListener('change', function() {
        srOptions.style.display = (this.value === 'Speech recognition') ? 'block' : 'none';
        whisperOptions.style.display = (this.value === 'Whisper') ? 'block' : 'none';

        if ((this.value !== 'Speech recognition') && (this.value !== 'Whisper')) {
            srVersionInputs.forEach(function(radioButton) {
                radioButton.checked = false;
            });
        }
    
        if ((this.value !== 'Speech recognition') && (this.value !== 'Whisper')) {
            whisperVersionInputs.forEach(function(radioButton) {
                radioButton.checked = false;
            });
        }
        //모델 선택에 따른 설명을 업데이트
        updateModelDescription(this.value);
    });
    
    //라디오 버튼 변경 시 해당 버전 설명 업데이트
    srVersionInputs.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            updatesrModelDescription(this.value);
        });
    });

    // 라디오 버튼 변경 시 해당 버전 설명 업데이트
    whisperVersionInputs.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            updateWhisperModelDescription(this.value);
        });
    });

    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        if ((modelselect.value === '' || (modelselect.value === 'Whisper' && !document.querySelector('input[name="whisper_model"]:checked')) || (modelselect.value === 'Speech recognition' && !document.querySelector('input[name="speech_recognition_model"]:checked')))) {
            event.preventDefault();
            alert("모델과 버전을 모두 선택하세요.");
        }
    });

    function updateModelDescription(selectedModel) {
        let description = "각 모델 준비를 마쳐야만 오류없이 사용 가능합니다. API들과 라이브러리들을 설치하고 진행해주세요. <br>(자세한 내용은 폴더 내 README를 참고바랍니다.)";
        if (selectedModel === 'speech_recognition') {
            description = "speech Recognition 라이브러리를 이용한 모델로 정확도가 준수합니다. <br>(라이브러리를 반드시 미리 설치하세요.)";
        } else if (selectedModel === 'ETRI api') {
            description = "ETRI API를 이용한 모델이나, 현재 정확도가 매우 떨어지는 것 같습니다. <br>(API를 반드시 미리 발급받으세요.)";
        } else if (selectedModel === 'Whisper') {
            description = "Whisper 모델은 OpenAI의 sTT 모델이나, API는 유료로 local의 모델을 불러왔습니다. <br>     (Local에 Whisper 및 GPU가 세팅되어 있지 않다면 불가능합니다.)";
        }
        modelDescription.innerHTML = `<p style="text-align: center;">${description}</p>`;
    }
    
    function updatesrModelDescription(version) {
        let description = "다양한 API를 이용한 sTT 라이브러리 입니다.";
        if (version === 'google') {
            description = "별도의 API가 필요하지 않습니다.";
        } else if (version === 'google_cloud_api') {
            description = "사전 Google api 발급이 필요합니다.";
        } else if (version === 'vosk') {
            description = "사전 모델 설치가 필요합니다.";
        } else if (version === 'whisper_local') {
            description = "사전 모델 설치가 필요합니다.";
        } else if (version === 'whisper_api') {
            description = "사전 Whisper api 발급이 필요합니다.";
        }
        modelDescription.textContent = description;
    }
    updateModelDescription(modelselect.value);

    function updateWhisperModelDescription(version) {
        let description = "정확도와 소요시간을 고려하여 모델을 선택하세요. 자세한 모델의 성능은 아래 WHIsPER의 공식문서를 참고바랍니다. <br> https://github.com/openai/whisper";
        if (version === 'tiny') {
            description = "Tiny 모델은 성능이 매우 떨어집니다.(CPU로도 가능, GPU 빠름)";
        } else if (version === 'base') {
            description = "Base 모델은 정확도가 매우 떨어집니다.(CPU로도 가능, GPU 빠름)";
        } else if (version === 'small') {
            description = "small 모델 정확도가 매우 떨어집니다.(CPU 매우느림, GPU 적당)";
        } else if (version === 'medium') {
            description = "Medium 정확도가 적당합니다.(CPU 매우느림, GPU 적당)";
        } else if (version === 'large') {
            description = "Large 정확도가 좋습니다.(CPU 거의불가, GPU 느림)";
        }
        modelDescription.textContent = description;
    }


    updateModelDescription(modelselect.value);
});
