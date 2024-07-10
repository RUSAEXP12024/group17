import sensor_get_data
import generate_text
import requests
import generate_mp3
import play_mp3
import textize
import app

def main():
    tmp, hum = sensor_get_data.sensor_get_data()
    text = generate_text.generate_text(tmp, hum)
    #send_line_notify(text)
    app.app(text)
    name = generate_mp3.generate_mp3(text)
    textize.textize(tmp,hum)
    play_mp3.play_mp3(name)



#以下は個別のLINE通知用
def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'jVDyQ09syjCQzPAzqcI9PtuCrSdKmACr3lVOqUy7Dwy'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()