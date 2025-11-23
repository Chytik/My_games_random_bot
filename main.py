import telebot
import algoritm
from telebot import types
import databases


bot = telebot.TeleBot(token='8528848069:AAEJAspOb6IV1YR3Vkv0GJGr_t9kpcPAOzg')
user_id = 0


@bot.message_handler(commands=['start'])
@bot.callback_query_handler(func=lambda callback: callback.data in ['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    #bot.send_message(message.chat.id,)
    btn1 = types.InlineKeyboardButton('The last of us 2', callback_data='TLOU2')
    btn2 = types.InlineKeyboardButton('Total war: Atilla', callback_data='Atilla')
    btn3 = types.InlineKeyboardButton('help', callback_data='help')
    markup.row(btn1), markup.row(btn2), markup.row(btn3)
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

@bot.callback_query_handler(func = lambda callback: callback.data in ['TLOU2 statistics', 'Atilla statistics'])
def statistics(callback):
    user_id = callback.from_user.id
    if callback.data == 'TLOU2 statistics':
        expt = algoritm.expt_transmission(databases.get_expt(user_id))
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('randomize characters', callback_data = 'randomize characters')
        btn2 = types.InlineKeyboardButton('Change the game', callback_data = 'Atilla')
        btn3 = types.InlineKeyboardButton('exit', callback_data = 'exit')
        markup.row(btn1), markup.row(btn2, btn3)
        bot.send_message(callback.message.chat.id, 'So, these are last 3 characters, you\'ve chosen randomized characters!\n\n'
                         '<b>{}\n\n{}\n\n{}</b>'.format(expt[0], expt[1], expt[2]), parse_mode='HTML', reply_markup=markup)

@bot.callback_query_handler(func = lambda callback: callback.data in ['exit'])
def exit(callback):
    bot.send_message(callback.message.chat.id, 'Ny i poshel nahyi, chmo eblivoe, blyat')


@bot.message_handler(commands=['help'])
@bot.callback_query_handler(func=lambda callback: callback.data in ['help'])
def help(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('start', callback_data='start')
    markup.row(btn1)
    bot.send_message(message.chat.id, '<b>help</b> <em><u>information!</u></em>'
    'So, this is beta version of <b>My games random bot</b>! No all fuctions are enable, but you also can use it!\n'
    'About functions:\n'
    '/start - move you to choise of games!\n'
    '<b>The last of us II</b>/<b>Total war: Atilla</b> move you to their windows for you can use their fuctions\n'
    '<em>P.S. Total War: Atilla is currently under development and isn\'t working now!</em>\n'
    '<b>randomize characters</b> give you random character to play rouge-like mode!\n'
    '<b>statistics</b> show you last 3 characters, that can\'t be rolled!\n'
    '<b>change the game</b> just swap the game!)\n'
    '<b>exit</b> bad bottom', parse_mode='HTML')

@bot.message_handler(func = lambda message: True)
def garbedje(message):
    if message.text.lower() == 'id':
        bot.reply_to(message.chat.id, 'Your ID: {}'.format(message.from_user.id))
    else:
        bot.send_message(message.chat.id, "Sorry, I don\'t understand you!\n"
        "Please use commands or buttons for communicate with me correctly!\n"
        "Else you can use /help to see all my potencial!")


bot.polling(none_stop=True)







