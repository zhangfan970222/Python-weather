import requests
import itchat
import json
import datetime
import time

city = '南京'
url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city


def get_weather():
    resp = requests.get(url)
    return json.loads(resp.text)


def send_data(data):
    friend = itchat.search_friends(name='别捏我肥脸')
    username = friend[0]['UserName']
    print(username)
    if '雨' in data['type']:
        dacey = data['data'] + '  ' + data['type'] + '  ' + data['high'] + '   ' + data['low'] + '  ' + data[
            'fengxiang'] + '  有雨记得带伞呀！'
    else:
        dacey = data['data'] + '  ' + data['type'] + '  ' + data['high'] + '   ' + data['low'] + '  ' + data['fengxiang']
    itchat.send(dacey, toUserName=username)


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    while True:
        time_now = datetime.datetime.now()
        if time_now.hour == 8 and time_now.minute == 0:
            data = get_weather()
            data = data['data']['forecast'][0]
            send_data(data)
            time.sleep(60)
        else:
            time.sleep(60)
            print('waiting')
