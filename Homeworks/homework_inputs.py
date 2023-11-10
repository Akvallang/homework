# Task 1

# The Guessing Game.

# Write a program that generates a random number between 1 and 10 and lets the user guess what number
#  was generated. The result should be sent back to the user via a print statement.

# import random

# while True:
#     number = random.randint(1, 10)
#     user_input = int(input("\nВведіть ваше число від 1 до 10:  "))
#     print("\nНе фарт, було ", number, "\nСпробуй но ще, або нажми 99 для зупинки!")
#     if user_input == number:
#         print(user_input, " = ", number,  "\nЯ навіть не сумнівався що ти краснчик і ти це подужаєш")
#         break
#     elif user_input == 99:
#         print("\nДякуємо за гру!")
#         break


# Task 2

# The birthday greeting program.

# Write a program that takes your name as input, and then your age as input and greets you with
#  the following:

# “Hello <name>, on your next birthday you’ll be <age+1> years”   

# name = input("Як тебе звть, друже? Напиши своє ім'я: ")
# age_string = input("Скільки тобі рочків? Введи цифрами: ")

# if name == "":
#     print("Не залишай поля пустими, я від цього засмучуюсь =(")
# else:
#     if age_string.isdigit():
#         age = int(age_string)
#         if age > 100:
#             print("Ну нашо ти брешеш?")
#         else:
#             greetings = ("\nПривіт, ", name.title(), ", на настпний ДР тобі сткне вже ", age + 1, " років. Сумно!")
#             print(*greetings)
#     else:
#         print("Тут поле було лише для циферок =(")

 

# Task 3

# Words combination

# Create a program that reads an input string and then creates and prints 5 random strings 
# from characters of the input string.

# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) 
# that combine characters 

# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)

import random
keyword = "счастье"
i = 0
my_list = []
while i < len(keyword):
    my_list.append(keyword[i])
    i += 1

print(my_list)
random_str_1 = "".join(random.choices(my_list, k=len(my_list)))
random_str_2 = "".join(random.choices(my_list, k=len(my_list)))
random_str_3 = "".join(random.choices(my_list, k=len(my_list)))
random_str_4 = "".join(random.choices(my_list, k=len(my_list)))
random_str_5 = "".join(random.choices(my_list, k=len(my_list)))
print(random_str_1)
print(random_str_2)
print(random_str_3)
print(random_str_4)
print(random_str_5)