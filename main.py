import telebot
from random import choices

bot = telebot.TeleBot('6051245699:AAGOc5qWvckjgbevdXWJUqGTJYxxv-FO6sY')

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
ally = upper+lower+nums
chars = ''


@bot.message_handler(commands=['start'])

def start_message(message):
    if message.text == '/start':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Создать пароль')
        bot.send_message(message.from_user.id, 'Приветствую! Я генерерирую пароли! Приступим?', reply_markup=markup)
        bot.register_next_step_handler(message, how_generation)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понял, напишите /start')
        bot.register_next_step_handler(message, start_message)


def how_generation(message):
    if message.text == 'Создать пароль':
        markup1 = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Из скольких символов должен состоять пароль?', reply_markup=markup1)
        bot.register_next_step_handler(message, generation)
    elif message.text == '/start':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Создать пароль')
        bot.send_message(message.from_user.id, 'Приветствую! Я генерерирую пароли! Приступим?', reply_markup=markup)
        bot.register_next_step_handler(message, how_generation)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понял, напишите /start')
        bot.register_next_step_handler(message, start_message)
def generation(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Создать пароль')
    try:
        number_of_signs = int(message.text)
        if number_of_signs < 128:
            chars = ''
            chars += ally
            pwd = ''.join(choices(chars, k=number_of_signs))
            bot.send_message(message.from_user.id, pwd)
            bot.send_message(message.from_user.id, 'Готово хотите создать еще пароль?', reply_markup=markup)
            bot.register_next_step_handler(message, how_generation)
        elif number_of_signs < 0:
            mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            mark.row('Создать пароль')
            bot.send_message(message.from_user.id, 'Пишите только положительные цифры!', reply_markup=mark)
            bot.register_next_step_handler(message, how_generation)
        elif number_of_signs > 128:
            mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            mark.row('Создать пароль')
            bot.send_message(message.from_user.id, 'Недопустимое значение', reply_markup=mark)
            bot.register_next_step_handler(message, how_generation)
    except ValueError:
        mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        mark.row('Создать пароль')
        bot.send_message(message.from_user.id, 'Пишите только цифры!', reply_markup=mark)
        bot.register_next_step_handler(message, how_generation)
    except telebot.apihelper.ApiTelegramException:
        mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        mark.row('Создать пароль')
        bot.send_message(message.from_user.id, 'Пишите только положительные цифры!', reply_markup=mark)
        bot.register_next_step_handler(message, how_generation)

bot.polling()