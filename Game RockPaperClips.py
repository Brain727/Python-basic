import random
botrandom = ["камень", "ножницы", "бумага"]
botwin = 0
userwin = 0
print("Сыграем в игру Камень-Ножницы-Бумага")
n = int(input("Введите количсетво раундов: "))

for i in range(n):
    botin = random.choice(botrandom)
    userin = ""
    while userin != "камень" and userin != "ножницы" and userin != "бумага":
        userin = input("Введите к(камень)-н(ножницы)-б(бумага)").lower()
        if userin == "к":
            userin = "камень"
        elif userin == "н":
            userin = "ножницы"
        elif userin == "б":
            userin = "бумага"
        else:
            print("Неправильный ввод!")

    if userin == "камень" and botin == "камень":
        print("Вы выбрали ", userin, ",а компьютер выбрал ",botin, " НИЧЬЯ!")
    elif userin == "камень" and botin == "ножницы":
        print("Вы выбрали ", userin, ",а компьютер выбрал ",botin, " ВЫ ПОБЕДИЛИ!")
        userwin +=1
    elif userin == "камень" and botin == "бумага":
        print("Вы выбрали ", userin, ",а компьютер выбрал ",botin, " ВЫ ПРОИГРАЛИ!")
        botwin +=1

    elif userin == "ножницы" and botin == "камень":
        print("Вы выбрали ", userin, ",а компьютер выбрал ", botin, " ВЫ ПРОИГРАЛИ!")
        botwin += 1
    elif userin == "ножницы" and botin == "ножницы":
        print("Вы выбрали ", userin, ",а компьютер выбрал ", botin, " НИЧЬЯ!")
    elif userin == "ножницы" and botin == "бумага":
        print("Вы выбрали ", userin, ",а компьютер выбрал ", botin, " ВЫ ПОБЕДИЛИ!")
        userwin += 1

    elif userin == "бумага" and botin == "камень":
        print("Вы выбрали ", userin, ",а компьютер выбрал ", botin, " ВЫ ПОБЕДИЛИ!")
        userwin += 1
    elif userin == "бумага" and botin == "ножницы":
        print("Вы выбрали ", userin, ",а компьютер выбрал ", botin, " ВЫ ПРОИГРАЛИ!")
        botwin += 1
    elif userin == "бумага" and botin == "бумага":
        print("Вы выбрали ", userin, ",а компьютер выбрал ", botin, " НИЧЬЯ!")

print("-"*10)
print("Игра окончена! Общий счет- ", userwin, ":", botwin)
if userwin == botwin:
    print("НИЧЬЯ!")
elif userwin > botwin:
    print("ВЫ ПОБЕДИЛИ!")
elif userwin < botwin:
    print("ВЫ ПРОИГРАЛИ!")


