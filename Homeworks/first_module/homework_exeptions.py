# Task 1

# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function 
# that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError
# instead of IndexError?
# 
def ooops(name):  
    result = name, name[6]
    print(result)
    
while True:
    try:
        ooops({"vasya":["kabasya"]})
        # ooops("kolbasa")
    except IndexError:
        print("Замало буков! В твоєму слові їх всього ", len("kolbasa"))
    except KeyError:
        print("Та це ж не словник")
    break
# 
# Task 2

# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the 
# value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the 
# input function were not numbers, and if value b was zero (cannot divide by zero).    

while True:
        try:
            a = int(input("Введи перше число: "))
            b = int(input("Введи друге число: "))
            print("ти ввів: ", a, "та", b)
            print("Результат квадрату першого числа діленого на друге: ",(a ** 2) / b)
        except ZeroDivisionError:
            print("Не діли на нуль, двієшник =) ")
        except ValueError:
            print("Не жульнічай і вводь циферки! ")
        break

