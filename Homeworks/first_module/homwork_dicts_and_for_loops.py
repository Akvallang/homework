# Task 1

# Make a program that has some sentence (a string) on input and returns a dict containing all 
# unique words as keys and the number of occurrences as values. 

# sentence = input("Введи мені яксь абракадабру для словничка. Якесь речення, наприклад о котрій розпочався твій день: ")
# my_dict = {}
# word = sentence.split()
# for word, index in enumerate(word, start=1):
#     my_dict[word] = index

# print(my_dict)
    

# Task 2

# Input data:

# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# sums_of_the_prices = {}

# for key in stock:
#     sums_of_the_prices[key] = stock[key] * prices[key]
# print(sums_of_the_prices)


# Compute the total price of the stock where the total price is the sum of the price of an item 
# multiplied by the quantity of this exact item.

# The code has to return the dictionary with the sums of the prices by the goods types.


# Task 3

# List comprehension exercise

# Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' 
# is corresponding to 'i' squared.

# list_comperhension = [(i, i**2) for i in range(1, 11)]
# print(list_comperhension)

# Task 4

# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,
# num_of_days = {}
# days_of_num = {}
# days = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"]
# for i, key in enumerate(days, start=1):
#     num_of_days[i] = key
#     days_of_num[key] = i

# print(num_of_days, days_of_num)
