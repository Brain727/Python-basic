import telebot
from telebot import types # клавиатура
import random

token = ""

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def game_start(message):
    # Открываем файл для записи
    file = open('RPC_log.txt', 'w')
    # Записываем
    file.write("\nUser id: {}".format(message.from_user.id))
    # Закрываем файл
    file.close()
    # Создаем клавиатуру
    bot.send_message(message.chat.id, "Игра 'Камень, Ножницы, Бумага' начинается!")
    bot.send_message(message.chat.id, "Сделай свой выбор: ")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Камень🤜')
    btn2 = types.KeyboardButton('Ножницы✌️')
    btn3 = types.KeyboardButton('Бумага✋')
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Камень🤜, ножницы✌️, бумага✋, раз, два, три! Выбирай сердцем:',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def game(message):
    botin = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
    if message.text == botin:
        bot.send_message(message.chat.id, "Мы оба выбрали {}. НИЧЬЯ!".format(botin))
        bot.send_message(message.chat.id, 'Для начала новой игры пишите или нажмите /start')
    else:
        if message.text == 'Камень🤜':
            if botin == 'Ножницы✌️':
                bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите или нажмите /start'.format(botin))
            else:
                bot.send_message(message.chat.id, 'Извините, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите или нажмите /start'.format(botin))
        elif message.text == 'Ножницы✌️':
            if botin == 'Бумага✋':
                bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(botin))
            else:
                bot.send_message(message.chat.id, 'Извините, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(botin))
        elif message.text == 'Бумага✋':
            if botin == 'Камень🤜':
                bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(botin))
            else:
                bot.send_message(message.chat.id, 'Извините, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(botin))


bot.polling(none_stop=True)  #постоянно обращается к серверам телеграм
