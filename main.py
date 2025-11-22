import telebot
import algoritm
from telebot import types
import databases


bot = telebot.TeleBot(token='8528848069:AAEJAspOb6IV1YR3Vkv0GJGr_t9kpcPAOzg')
user_id = 0

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    #bot.send_message(message.chat.id,)
    btn1 = types.InlineKeyboardButton('The last of us 2', callback_data='TLOU2')
    btn2 = types.InlineKeyboardButton('Total war: Atilla', callback_data='Atilla')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, 'Hello, {}!\n'
    'Choose the game, that you want to play!'.format(message.from_user.first_name), reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data in ['TLOU2', 'Atilla'])
def choise_of_game(callback):
    if callback.data == 'TLOU2':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('randomize characters', callback_data='TLOU2 randomize')
        btn2 = types.InlineKeyboardButton('statistics', callback_data='TLOU2 statistics')
        btn3 = types.InlineKeyboardButton('Change the game', callback_data='Atilla')
        btn4 = types.InlineKeyboardButton('exit', callback_data='exit')
        markup.row(btn1), markup.row(btn2), markup.row(btn3), markup.row(btn4)
        photo = open('./templates/TLOU2/The_last_of_us_2.jpeg', 'rb')
        with photo as photo:
            bot.send_photo(
                callback.message.chat.id,
                photo,
                'Super, <b>The Last of Us Part II</b>\nNow choose the function!',
                'HTML',
                reply_markup=markup
            )
    elif callback.data == 'Atilla':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('randomize fractions', callback_data = 'Atilla randomize')
        btn2 = types.InlineKeyboardButton('statistics', callback_data='Atilla statistics')
        btn3 = types.InlineKeyboardButton('Change the game', callback_data='TLOU2')
        btn4 = types.InlineKeyboardButton('exit', callback_data = 'exit')
        markup.row(btn1), markup.row(btn2), markup.row(btn3), markup.row(btn4)
        photo = open('./templates/Atilla/Total_War_Attila.jpg', 'rb')
        with photo as photo:
            bot.send_photo(
                callback.message.chat.id,
                photo,
                'Great, <b>Total war: Atilla</b>\nNow choose the function!',
                'HTML',
                reply_markup=markup
            )

@bot.callback_query_handler(func = lambda callback: callback.data in ['randomize characters', 'randomize fractions'])
def randomize(callback):
    user_id = callback.from_user.id
    if callback.data == 'randomize characters':
        photo_name, phrase = algoritm.choose_caracter(user_id)
        photo = databases.get_photo_from_db(photo_name)
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('randomize again', callback_data = 'randomize characters')
        btn2 = types.InlineKeyboardButton('statistics', callback_data = 'TLOU2 statistics')
        btn3 = types.InlineKeyboardButton('Change the game', callback_data='Atilla')
        btn4 = types.InlineKeyboardButton('exit', callback_data='exit')
        markup.row(btn1), markup.row(btn2), markup.row(btn3), markup.row(btn4)
        with open(photo, 'rb') as photo:
            bot.send_photo(
                callback.message.chat.id,
                photo,
                caption = phrase,
                reply_markup = markup
            )




@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b> <em><u>information!</u></em>', parse_mode='HTML')

@bot.message_handler(func = lambda message: True)
def garbedje(message):
    if message.text.lower() == 'id':
        bot.reply_to(message.chat.id, 'Your ID: {}'.format(message.from_user.id))
    else:
        bot.send_message(message.chat.id, "Sorry, I don\'t understand you!\n"
        "Please use commands or buttons for communicate with me correctly!\n"
        "Else you can use /help to see all my potencial!")


bot.polling(none_stop=True)







