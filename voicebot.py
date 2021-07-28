import telebot, conv
bot = telebot.TeleBot('')

@bot.message_handler(commands = ['start'])
def welc(message):
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.username + '. Введи текст, чтобы получить его в виде голосового сообщения: ')
    bot.register_next_step_handler(message, send_voicemsg)

@bot.message_handler(content_types = ['text'])
def send_voicemsg(message):
    conv_text = message.text
    textfile = open('conv_text', 'w')
    textfile.write(conv_text)
    textfile.close()
    conv.convert()
    conv_sound = open('conv_sound.mp3', 'rb')
    bot.send_audio(message.chat.id, conv_sound)
    conv_sound.close()

bot.polling(none_stop = True)
