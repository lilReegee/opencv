import json
import requests
import base64

'''
车牌识别
'''

client_id = 'LR6w0HKc8Yzjd8q6FPTkrgpR'
client_secret = 'UyKYwPp38XkPAwPxl9pYpW0WsccfnBc9'

# 获取token
def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    response = requests.get(host)
    if response:
        token_info = response.json()
        token_key = token_info['access_token']
    return token_key



request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
# 二进制方式打开图片文件
f = open('./Test/蒙B099X8.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = get_token()
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())