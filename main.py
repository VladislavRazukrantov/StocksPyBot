import telebot
from telebot import types

bot = telebot.TeleBot('5707455690:AAH_dra68o20IGv0q94Bz7O1m3mHdoS73dw')
keyboard = types.InlineKeyboardMarkup()

@bot.message_handler(commands=['start', 'help'])
def start(message):
    start_message = 'Привет! Это финансовый бот, который позволит тебе упростить работу с акциями!\n\n' + \
                    'Команды:\n\n' + \
                    '/quotations - Посмотреть котировки \n' + \
                    '/portfolio - Посмотреть портфель\n'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_quotations = types.KeyboardButton(text='Котировки')
    key_portfolio = types.KeyboardButton(text='Портфель')
    markup.add(key_portfolio, key_quotations)
    bot.send_message(message.chat.id, start_message, reply_markup=markup)  # третий аргумент - меняем клавиатуру на кнопочную

@bot.message_handler(commands=['back'])
def back(message):
    back_message = 'Привет! Это финансовый бот, который позволит тебе упростить работу с акциями!\n\n' + \
                    'Команды:\n\n' + \
                    '/quotations - Посмотреть котировки \n' + \
                    '/portfolio - Посмотреть портфель\n'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_quotations = types.KeyboardButton(text='Котировки')
    key_portfolio = types.KeyboardButton(text='Портфель')
    markup.add(key_portfolio, key_quotations)
    bot.send_message(message.chat.id, back_message, reply_markup=markup)

@bot.message_handler(commands=['quotations'])
def quotations(message):
    bot.send_message(message.chat.id, 'Введите название акции')
    bot.register_next_step_handler(message, get_title_of_stock)

def get_title_of_stock(message): #после ввода пользователем названия мы попадаем сюда
    answer = 'Мы нашли введенную акцию!'
    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text']) #обработка текстового сообщения
def random_answers(message):
    if message.text == 'Котировки':
        quotations(message)
    if message.text == 'Портфель':
        bot.send_message(message.chat.id, 'Мы в портфеле')
    if message.text == 'Вернуться в меню':
        back(message)

bot.polling(none_stop=True, interval=0)