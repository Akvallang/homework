# Task 1

# Клас осіб
# Створіть клас під назвою Person. Зробіть так, щоб метод __init__() приймав ім’я, прізвище та вік як параметри та додавав їх як атрибути.
# Створіть ще один метод під назвою talk(), який друкує привітання від особи, яке містить, наприклад, таке: «Привіт, мене звати Карл Джонсон, мені 26 років».
 
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Привіт, мене звати {self.first_name} {self.last_name}, мені {self.age} років.")
        
person = Person("Карл", "Джонсон", 26)
person.talk()


# Task 2

# Собачий вік
# Створіть клас Dog з атрибутом класу 'age_factor', рівним 7. Створіть __init__(), який приймає значення для віку собаки. 
# Потім створіть метод `human_age`, який повертає вік собаки в людському еквіваленті.
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        human_equivalent_age = self.dog_age * self.age_factor
        return human_equivalent_age
    
dog = Dog(5)
print(f"Вік собаки в людському еквіваленті: {dog.human_age()} років.")

# Task 3

# ТВ контролер
# Створіть простий прототип телевізійного контролера на Python. Він використовуватиме такі команди:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
 

# Канал за замовчуванням, увімкнений перед усіма командами, — №1.
# Ваше завдання — створити клас TVController і методи, описані вище.
# '''

# CHANNELS = ["BBC", "Discovery", "TV1000"]
#  class TVController:

# pass

#  controller = TVController(CHANNELS)

# controller.first_channel() == "BBC"

# controller.last_channel() == "TV1000"

# controller.turn_channel(1) == "BBC"

# controller.next_channel() == "Discovery"

# controller.previous_channel() == "BBC"

# controller.current_channel() == "BBC"

# controller.exists(4) == "No"

# controller.exists("BBC") == "Yes"

# '''

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, channel_number):
        if 1 <= channel_number <= len(self.channels):
            self.current_channel_index = channel_number - 1
            return self.current_channel()
        else:
            return "Invalid channel number"

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def exists(self, channel):
        if isinstance(channel, int):
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        elif isinstance(channel, str):
            return "Yes" if channel in self.channels else "No"
        else:
            return "Invalid argument type"

CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel())       
print(controller.last_channel())        
print(controller.turn_channel(1))       
print(controller.next_channel())       
print(controller.previous_channel())    
print(controller.current_channel())     
print(controller.exists(4))             
print(controller.exists("BBC"))         
