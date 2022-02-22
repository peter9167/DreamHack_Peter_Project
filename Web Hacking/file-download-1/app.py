#!/usr/bin/env python3
import os
import shutil

from flask import Flask, request, render_template, redirect # render_template : templates에 저장된 html을 불러올 때 사용되는 함수

from flag import FLAG

APP = Flask(__name__)

UPLOAD_DIR = 'uploads'


@APP.route('/')
def index():
    files = os.listdir(UPLOAD_DIR) # 지정한 디렉토리 내의 모든 파일과 디렉토리의 리스트를 리턴
    return render_template('index.html', files=files) # templates에 저장된 index.html을 불러옴
                                                      # files=files에 의미 : 좌항은 html 내에서 사용변수 이름 / 우항은 부분은 변수(Python)의 값


@APP.route('/upload', methods=['GET', 'POST'])
def upload_memo():
    if request.method == 'POST': # HTTP 요청 메서드가 'POST'라면
        filename = request.form.get('filename') # Flask 요청에서 수신한 데이터(filename) 가져오기
        content = request.form.get('content').encode('utf-8') # Flask 요청에서 수신한 데이터(filename) 유니코드로 변환하여 가져오기

        if filename.find('..') != -1: # filename 데이터 내 '..' 문자열 검색
            return render_template('upload_result.html', data='bad characters,,')

        with open(f'{UPLOAD_DIR}/{filename}', 'wb') as f:
            f.write(content)

        return redirect('/')

    return render_template('upload.html')


@APP.route('/read')
def read_memo():
    error = False
    data = b''

    filename = request.args.get('name', '')

    try:
        with open(f'{UPLOAD_DIR}/{filename}', 'rb') as f:
            data = f.read()
    except (IsADirectoryError, FileNotFoundError):
        error = True


    return render_template('read.html',
                           filename=filename,
                           content=data.decode('utf-8'),
                           error=error)


if __name__ == '__main__':
    if os.path.exists(UPLOAD_DIR):
        shutil.rmtree(UPLOAD_DIR)

    os.mkdir(UPLOAD_DIR)

    APP.run(host='0.0.0.0', port=8000)
