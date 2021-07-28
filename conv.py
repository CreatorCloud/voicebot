from gtts import gTTS

def convert():
    textfile = open('conv_text')
    conv_text = textfile.read()
    textfile.close()
    conv_sound = gTTS(text = conv_text, lang = 'ru', slow = False)
    conv_sound.save('conv_sound.mp3')
