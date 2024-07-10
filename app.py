# -*- coding:utf-8 -*-
import requests
import urllib.request, urllib.error
import json

#LINEアカウントによる一斉通知
def app(text):
    url = 'https://api.line.me/v2/bot/message/broadcast'
    channel_access_token = 'I24Jgb5VB2VPVASMZoUt6VzRFj3dL3lAHBlTi4Z6S1tOtGDApKGxv5IkbPacfNIl4KQ9kribk9mNeObbKjThaH8QzeMU+OnFeEzxumtDuIXMOjEaszE3HMqNM8sZpF0tv1zw3hGXFrEYM2dicai6QAdB04t89/1O/w1cDnyilFU='
    # 送信用のデータ
    # messageの中にtype,textの配列を追加すれば一度に複数のメッセージを送信できます。(最大件数5)
    data = {
        'messages' : [{
            'type':'text',
            'text':text
        }]
    }
    jsonstr = json.dumps(data).encode('ascii')
    request = urllib.request.Request(url, data=jsonstr)
    request.add_header('Content-Type', 'application/json')
    request.add_header('Authorization', 'Bearer ' + channel_access_token)
    request.get_method = lambda: 'POST'
    # 送信実行(レスポンスが200なら送信成功)
    response = urllib.request.urlopen(request)
    print(response)

