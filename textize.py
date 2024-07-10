from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json import loads
import sensor_get_data
import datetime

#txtファイルに情報を追加・保存
def textize(tmp,hum):
    dt_now = datetime.datetime.now()
    with open('status.txt', 'a', encoding='utf-8') as file:
        file.write(dt_now.isoformat()+"\n")
        file.write(f"温度: { tmp }度\n湿度: { hum } \n \n")
