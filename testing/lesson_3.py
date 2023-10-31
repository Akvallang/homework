#
# print("\n\n\n", "Реалізація вибору пошт:")
# name = input("Введіть будь ласка ваше ім'я латинкою: ")
# last_name = input("Введіть бдь ласка ваше прізвище латинкою: ")
# domen = "kobzar.com"
# at = ("@")
# print("Варіант 1: ", name[0].lower() + "." + last_name.lower() + at + domen)
# print("Варіант 2: ", name[:3].lower() + "." + last_name[:5].lower() + at + domen)

print("\n\n\n Вредний клієнт")
yes = "так"
no = "ні"
question_1 = input("Доброго дня! Чи бажаєте ви щоб Вам зателефонвали?(Так чи ні) ").lower()
if question_1 == yes:
    number_field = int(input("Введіть ваш номер телефон в форматі 380... :  "))
if type(number_field) != int:
    answer_1 = input("Не жульнічай! Вводь знову, але цифри: ")
if type(number_field) == int:
    answer_2 = "Дякую, ми з вами якомога швидше зв'яжемось!"
else:
    question_2 = input("То можливо нам варто було би вас набрати?(Так чи ні) ")
    if question_2 == yes:
         number_field = input("Введіть ваш номер телефон в форматі 380... :  ")
    if question_2 == no:
         print("Нам офігенно прикро =(")
    if number_field != int:
         answer_1 = input("Не жульнічай! Вводь знову, але цифри: ")
    else:
        question_3 = input("Але все ж таки, я хотів би бачити Ваш номер. Ви його введете?(Так чи ні) ")