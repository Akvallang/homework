# Task 1

# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random
ran_list = [] # ліст для наповнення рандомними значеннями
it = 0        #  початкова кількість ітерацій
while it <10: # цикл в 10 ітерацій
    ran_numbers = random.randint(1, 10000)  # межа рандомних чисел
    it += 1
    ran_list.append(ran_numbers)   #  додавання значень в ліст
print(ran_list)  # для самоперевірки
max_number = max(ran_list)  
print(max_number)


# Task 2

# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list 
# containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random
list_1 = []
list_2 = []
cont_list = []
it_1 = 0
while it_1 < 10:
    random_values_1 = random.randint(1, 10)
    it_1 += 1
    list_1.append(random_values_1)
#print(list_1)   # для перевірки

it_2 = 0
while  it_2 < 10:
    random_values_2 = random.randint(1, 10)
    it_2 += 1
    list_2.append(random_values_2)
#print(list_2)  # для перевірки
cont_list = list(set(list_1 + list_2))
print(cont_list)

# Task 3

# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are 
# divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

i = 1
integers_list = []
answers_list = []
while i < 101:
    integers_list.append(i)
    i +=1

for element in integers_list:
    if element % 7 == 0:
        if element % 5 !=0:
            answers_list.append(element)

print(answers_list)
