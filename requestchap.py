import os
import sys
import urllib.request
count=0
while(1):
    client_id = "" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "" # 개발자센터에서 발급받은 Client Secret 값
    key = "" # 캡차 Key 값 , chapkey.py output
    url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        #print("캡차 이미지 저장")
        response_body = response.read()
        with open('E:\\naver_captchar_image\\captcha%d.jpg'%count, 'wb') as f:
            f.write(response_body)
            count=count+1
    else:
        print("Error Code:" + rescode)
        break

print("Program Done...")
