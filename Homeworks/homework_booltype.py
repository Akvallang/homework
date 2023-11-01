# Task 1

unit_for_manipulation = "Якась абракадабра"
var1 = (unit_for_manipulation[:2].lower() + unit_for_manipulation[-2:].lower())
var2 = "r"
print(var1)
print(var1*2) # Це типу замість муму із прикладу. Бо не дуже зрозумів про що йде мова з муму =)
if len(var1) < 2:
    print("\n")
# elif len(var2) < 2:
#     print("Пустий рядок")
else:
    print("В нас нема менше двох символівб бо: var1 = ", len(var1), "символи, та var2 = ", len(var2), "символів, але він закоментований =)" )

# Task 2

mobile_number = input("\nВведіть ваш номер телефону в форматі 380...: ")
if mobile_number.isdigit() and len(mobile_number) == 12: 
        print("\nДякую, номер коректний!")
else:
    print("\nВведіть коректний номер у форматі 380ххххххх!")

# Task 3 (Недоробок, бо хотілось повністю реалізувати юзабіліті, але свого розм не вистачило, а чат ГПТ сказав що треба вчити настпні уроки)

a = 36
b = 72
c = 4
equation_1 = a + b * c  #324
equation_2 = b - a * c  #-72
equation_3 = b * c / a  #8.0
answer_false = "\nВідповідь не вірна, спробуйте ще раз!"
answer_true = "\nВи молодець! Наступне питання: "
answer_end = "Супер! Ви крутий математик!"
print("\nПограємо у вікторину. Дайте відповідь на наступне запитання: ")

print(a, "+", b, "*", c)

flag = True                                                                     
while flag is True:                                                             
    answer_1 = int(input("Введіть результат обчислення виразу:  "))             
    if equation_1 == answer_1:
        flag = False
        print(answer_true)
        print(b, "-", a, "*", c)
        answer_2 = int(input("Введіть результат обчислення виразу:  "))
        if equation_2 == answer_2:
            print(answer_true)
            print(b, "*", c, "/", a)
            answer_3 = int(input("Введіть результат обчислення виразу:  "))
            if equation_3 == answer_3:
                print(answer_end)
            else:
                print(answer_false) 
        else:
            print(answer_false)       
    else:
        print(answer_false)

#    Чат GPT сказав що поточна стрктура код не дозволить перевірити всі вирази по черзі через вкладені умови, і том він переробив через
#   ліст та тьюпл, тому якщо цікаве його рішення, то осьо:
    
# a = 36
# b = 72
# c = 4
# equation_1 = a + b * c  # 324
# equation_2 = b - a * c  # -72
# equation_3 = b * c / a  # 8.0

# answer_false = "\nВідповідь не вірна, спробуйте ще раз!"
# answer_true = "\nВи молодець! Наступне питання: "
# answer_end = "Супер! Ви крутий математик!"

# print("\nПограємо у вікторину. Дайте відповідь на наступне запитання: ")

# questions = [
#     (equation_1, f"{a} + {b} * {c}"),
#     (equation_2, f"{b} - {a} * {c}"),
#     (equation_3, f"{b} * {c} / {a}")
# ]

# for equation, equation_str in questions:
#     print(equation_str)
#     while True:
#         answer = int(input("Введіть результат обчислення виразу: "))
#         if equation == answer:
#             print(answer_true)
#             break
#         else:
#             print(answer_false)

# print(answer_end)

# Task 4

name = "ярослав"
name_for_check = input("\nВведіть тут моє ім'я:  ")
zminna = True

while zminna is True:
    if name.lower() == name_for_check.lower():
        print("Все ок, вам вдалось коректно написати моє ім'я")
        zminna = False
    else:
        print("Ну як можна не впоратись із написанням мого імені?")
        

