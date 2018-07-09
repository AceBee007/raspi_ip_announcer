# coding: utf-8
import requests
import time

sleeptime = 5
looptimes = 24
for i in range(looptimes):
    try:
        api_token = requests.post('http://192.168.11.10:3090/slack-api-token')
        if 'xoxb' in api_token.text:
            break
    except:
        print("Can't connect to internet or Quiz-Robots\n\t\tSleeping 5s...\t\tProgram will be closed after "+str((looptimes-i)*sleeptime)+"s")
        time.sleep(sleeptime)

# botアカウントのトークンを指定
API_TOKEN = api_token.text

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "I can't understand what you said!\nあなたが言ってることがわかりません！"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
