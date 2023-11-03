# app.py
import os
import psutil
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    selected_model = request.form.get('model')
    model_version = 'default'  # 기본값을 "basic"으로 설정
    if selected_model == 'Whisper': model_version = request.form.get('whisper_model')
    if selected_model == 'Speech recognition': model_version = request.form.get('speech_recognition_model')

    # subprocess로 main.py를 실행 -> 선택한 모델, 버전 넘겨줌.
    cmd = ['python', 'main.py', selected_model, model_version]
    process = subprocess.Popen(cmd)

    # main.py(subprocess)를 관리(실행중인지 확인)하기 위하여 process.pid를 전달
    return render_template('result.html', selected_model=selected_model, model_version=model_version, process_pid=process.pid)

@app.route('/show_result')
def show_result():
    selected_model = request.args.get('selected_model')
    model_version = request.args.get('model_version')
    return render_template('result.html', selected_model=selected_model, model_version=model_version)

@app.route('/check_process_status')
def check_process_status():
    # 실행중인 main.py의 process_pid 받아옴.
    process_pid = int(request.args.get('process_pid'))
    try:
        process = psutil.Process(process_pid)
        if process.is_running(): return jsonify({'process_status': 'running'})
        else: return jsonify({'process_status': 'terminated'})
    except psutil.NoSuchProcess:
        return jsonify({'process_status': 'terminated'})

# 메인화면에서는 process 자동 종료
@app.route('/stop_process', methods=['POST'])
def stop_process():
    # 실행중인 main.py의 process_pid 받아옴.
    process_pid = int(request.args.get('process_pid'))
    if process_pid:
        try:
            os.kill(process_pid, 9)  # 프로세스를 강제 종료
            process_pid = None
            return jsonify({'process_stopped': True})
        except ProcessLookupError:
            return jsonify({'process_stopped': False})
    else:
        return jsonify({'process_stopped': False})

if __name__ == '__main__':
    app.run()
