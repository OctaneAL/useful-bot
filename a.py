import telebot, time, os
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv('env.env')

TOKEN = os.getenv("TELEGRAM_TOKEN")

global bot, language
bot = telebot.TeleBot(TOKEN)
language = 'ru'
text2read = 'Привет'
myobj = gTTS(text=text2read, lang=language, slow=False)
myobj.save("welcome.mp3")

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == '/stop':
        bot.send_message(message.from_user.id, 'Данная команда может выполнится лишь после команды /start :|')
        return
    if message.text.lower() == '/help':
        bot.send_message(message.from_user.id, 'Данный бот озвучает Ваши сообщения ;)\nНапиши /start для начала работы этого крутецкого бота c;\nЕсли вы хотите завершить работу, это можно сделать с помощью команды /stop')
        return
    if message.text.lower() == '/start':
        bot.send_message(message.from_user.id, "Введите текст для озвучки\nДля завершения работы напишите /stop")
        bot.register_next_step_handler(message, send_voice)
        return
    bot.send_message(message.from_user.id, 'Я не знаю такой команды 0_o\nНапишите /help для ознакомления с моими возможностями')

def send_voice(message):
    global name
    text2read = message.text
    if text2read.lower() == '/stop':
        bot.send_message(message.from_user.id, 'Бот завершил работу\nНапишите /start для продолжения работы')
        return
    myobj = gTTS(text=text2read, lang=language, slow=False)
    myobj.save("welcome.mp3")
    #bot.send_voice(message.from_user.id, 'welcome.mp3')
    bot.send_voice(message.from_user.id, voice=open('welcome.mp3', 'rb'))
    bot.register_next_step_handler(message, send_voice)
    return
    #bot.register_next_step_handler(message, get_surname);

if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print('----------')
        print(e) # или import traceback; traceback.print_exc() для печати полной инфы
        print('----------')
