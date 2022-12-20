import telebot
import random
from env import TOKEN
bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1,button2)

@bot.message_handler(commands=['start', 'hi'])



def start_function(mesage):
    msg = bot.send_message(mesage.chat.id,f'Привет { mesage.chat.first_name} начнем игру ?', reply_markup=keyboard)
    # bot.send_sticker(mesage.chat.id,'CAACAgIAAxkBAAJKAAFjoT1YcKhXSmYkOfn_pgfYSRjpNAACDwEAAlKJkSNldRdchg_VhiwE')
    # bot.send_photo(mesage.chat.id,'https://www.google.com/url?sa=i&url=https%3A%2F%2Frosphoto.com%2Fbest-of-the-best%2F55_luchshih_foto_online-galerei-4112&psig=AOvVaw2y2uWmoinLEfyVIIeBvKFS&ust=1671598290785000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCIjan4izh_wCFQAAAAAdAAAAABAD')
    bot.register_next_step_handler(msg,answer_check)



# @bot.message_handler()
# def echo_all(message):
#bot.send_message(message.chat.id,message.text)
def answer_check(msg):
    if msg.text == 'Да':
        bot.send_message(msg.chat.id, 'у тебя есть 3 попытки не проебаться выбирая цифры в промежутке 1 - 10')
        random_number = random.randint(1,10)
        p = 3
        start_game(msg, random_number , p)
    else:
        bot.send_message(msg.chat.id, 'Тогда пощёл на хуй!')

def start_game(msg,random_number,p):
    msg = bot.send_message(msg.chat.id, 'выбирай число от 1 до 10 сука')
    bot.register_next_step_handler(msg,check_func,random_number, p-1)

def check_func(msg, random_number , p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id,'Ты не лох!')
    elif p==0:
        bot.send_message(msg.chat.id, f'Лошара попытки закончились число было {random_number}')
    else:
        bot.send_message(msg.chat.id, f'Пытайся лучше сука, еще {p} шанса')
        start_game(msg, random_number , p)



bot.polling()



'''
git init 
git add . 
git commit -m 'names comit'
git remote add origin ssh/htps
git push origin master
'''