from datetime import datetime
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json import loads
import datetime

#Remo 3から情報を取得
def sensor_get_data():
    api_key = "T0UyquNAlljemYWs-7Y8INbsUdarMstYo9OK5RVV2_4.SWOPmmP7HhJ59osDHlntyr5urTAvzk4Eek7Rfwki7Y4"  # APIアクセストークン

    url = "https://api.nature.global/1/devices/"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + api_key,
    }

    request = Request(url, headers=headers)

    try:
        with urlopen(request) as response:
            data_byte = response.read()
            data = loads(data_byte)
    except HTTPError as e:
        print(e)

    device_info = data[0]["newest_events"]

    print("温度 : " + str(device_info["te"]["val"]) + "度")
    print("湿度 : " + str(device_info["hu"]["val"]) + "%")
    return device_info["te"]["val"], device_info["hu"]["val"]
