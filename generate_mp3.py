from gtts import gTTS

def generate_mp3(message):
    # gTTS を使ってテキストを音声に変換
    tts = gTTS(text=message, lang='ja')
    name = 'message.mp3'
    tts.save('./'+name)
    return name