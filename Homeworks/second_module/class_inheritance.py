# Task 1

# Школа
# Створіть структуру класу на Python, яка представлятиме людей у школі. Створіть базовий клас під назвою Person, клас під назвою Student 
# і ще один під назвою Teacher. Спробуйте знайти якомога більше методів і атрибутів, які належать до різних класів, і майте на увазі,
# які з них є загальними, а які ні. Наприклад, ім’я має бути атрибутом Person, тоді як зарплата має бути доступна лише вчителю.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.grades = {}

    def study(self, subject, grade):
        self.grades[subject] = grade
        return f"{self.name} is studying {subject} and got a grade of {grade}."

class Teacher(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.salary = salary
        self.classes_taught = []

    def assign_grade(self, student, subject, grade):
        if subject in student.grades:
            student.grades[subject] = grade
            return f"Grade assigned to {student.name} for {subject}: {grade}."
        else:
            return f"{student.name} is not studying {subject}."

    def add_class(self, class_name):
        self.classes_taught.append(class_name)
        return f"{self.name} is now teaching {class_name}."

student1 = Student("Alice", 15, "female", "S001")
teacher1 = Teacher("Mr. Smith", 40, "male", 50000)

print(student1.introduce())
print(student1.study("Math", 90))

print(teacher1.introduce())
print(teacher1.assign_grade(student1, "Math", 95))
print(teacher1.add_class("History"))


# Task 2

# Математик
# Реалізуйте клас Mathematician, який є допоміжним класом для виконання математичних операцій зі списками
# Клас не приймає жодних атрибутів і має лише методи:
# square_nums (бере список цілих чисел і повертає список квадратів)
# remove_positives (бере список цілих чисел і повертає його без додатних чисел
# filter_leaps (бере список дат (цілі числа) і видаляє ті, які не є «високосними роками»
# '''

# class Mathematician:
#     pass

# m = Mathematician()
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
# '''

class Mathematician:
    def square_nums(self, numbers):
        return [num ** 2 for num in numbers]

    def remove_positives(self, numbers):
        return [num for num in numbers if num <= 0]

    def filter_leaps(self, years):
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


# Task 3

# Магазин товарів
# Напишіть клас Product, який має три атрибути:

# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
# '''

# class Product:
#     pass

# class ProductStore:
#   pass

# p = Product('Sport', 'Football T-Shirt', 100)
# p2 = Product('Food', 'Ramen', 1.5)
# s = ProductStore()
# s.add(p, 10)
# s.add(p2, 300)
# s.sell_product('Ramen', 10)
# assert s.get_product_info('Ramen') == ('Ramen', 290)
# '''

class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {'type': product.type, 'price': product.price * 1.3, 'amount': amount}

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product_name, product_info in self.products.items():
            if identifier_type == 'name' and identifier == product_name:
                product_info['price'] *= (1 - percent / 100)
            elif identifier_type == 'type' and identifier == product_info['type']:
                product_info['price'] *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name in self.products and self.products[product_name]['amount'] >= amount:
            self.products[product_name]['amount'] -= amount
            self.income += amount * self.products[product_name]['price']
        else:
            raise ValueError(f"Not enough {product_name} in stock.")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        if product_name in self.products:
            return (product_name, self.products[product_name]['amount'])
        else:
            raise ValueError(f"{product_name} not found in the store.")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

print(s.get_product_info('Ramen')) 



# Task 4

# Спеціальний виняток
# Створіть власний виняток під назвою "CustomException", ви можете успадкувати від базового класу винятків, але розширити його функціональність до
# реєструвати кожне повідомлення про помилку у файлі з назвою 'logs.txt'. Поради: використовуйте метод __init__, щоб розширити функціональні 
# можливості для збереження повідомлень у файл

# '''

# class CustomException(Exception):
# def __init__(self, msg):

# '''

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_message(msg)

    def log_message(self, msg):
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"{msg}\n")

try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print(f"Caught CustomException: {e}")

with open('logs.txt', 'r') as log_file:
    content = log_file.read()
    print("Content of 'logs.txt':")
    print(content)
