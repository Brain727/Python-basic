import telebot
import random

token = "1778106641:AAGBBRBdYa1akx9xjubQQN_BEbnGTHqx9os"

bot = telebot.TeleBot(token)

HELP = """
/help - вывести список команд
/add - добавить задачу в список
/show - напечатать все задачи
/end - конец работы
/random - добавить случайную задачу на дату Сегодня"""

random_tasks = ["Записаться на курс", "Купить горошек", "Посмотреть кино", "Написать код"]

tasks = {}

def add_todo(date, task):
    if date in tasks:  # если дата уже существует, то добавляем
        tasks[date].append(task)
    else:  # если даты нет, то создаем
        tasks[date] = [task]


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    if len(task) >= 3:
        add_todo(date, task)
        text = "Задача " + task + " добавлена на дату " + date
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Ошибка! Задача короче 3 символов")

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(random_tasks)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "- " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)  #постоянно обращается к серверам телеграм