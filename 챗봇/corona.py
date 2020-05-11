from flask import Flask, request, jsonify
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
import urllib.request
import re
import requests
import urllib
import json
app = Flask(__name__)
# 클리닝 함수 (아래 함수를 사용해 웹 사이트에서 받은 내용에는 ,나 괄호 등 필요 없는 내용이 있어 이 내용을 삭제하는 함수이다)
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', cleaned_text)
    cleaned_text = " ".join(re.split("\s+", cleaned_text, flags=re.UNICODE))
    return cleaned_text
# URL와 cicle을 전달받고 그 URL로 들어가서 div class=circle부분 내용을 리턴한다
def get_text(URL, circle):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', class_=circle):
        text = text + str(item.find_all(text=True))
    return text
    text = ''
    for item in soup.find_all('div', class_=circle):
        text = text + str(item.find_all(text=True))
    return text
@app.route('/corona', methods=['POST'])
def corona():
    req = request.get_json()
    params = req['action']['detailParams']
    answer = ''
    if req == u"코로나 현황":
        print("사용자가 코로나 현황을 요청했습니다")
    URL = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+19&oquery=%EC%BD%94%EB%A1%9C%EB%82%98+10&tqi=UrPCtwp0JXVss6%2FzMgZssssssPs-515140"
    start = time.time()
    temp = get_text(URL, "box")
    # temp1 = get_text(URL, "box bottom")
    # temp2 = get_text(URL, "circle orange level5")
    # temp3 = get_text(URL, "circle black level3")
    temp = temp + '\n'
    temp = clean_text(temp)
    info =""
    answer = '현재 코로나바이러스 현황입니다.\n\n'
    answer += info
    answer += temp + '\n\n'
    answer += '출처 : 중앙안전대책본부, 중앙사고수습본부, 중앙방역대책본부\n\n'+'이 코로나 현황은 네이버에서 가져온 결과입니다.\nCoding by 둔각삼각형'
    end = time.time()
    print("WorkingTime: {} sec".format(end-start))  # 현재시각 - 시작시간 = 실행 시간
    answer += "\nWorkingTime: {} sec".format(end-start)
        # 일반 텍스트 응답형 메시지
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }
    return jsonify(res)
# 메인 함수
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True, threaded=True)
