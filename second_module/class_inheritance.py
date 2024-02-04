# Task 1

# Школа
# Створіть структуру класу на Python, яка представлятиме людей у школі. Створіть базовий клас під назвою Person, клас під назвою Student 
# і ще один під назвою Teacher. Спробуйте знайти якомога більше методів і атрибутів, які належать до різних класів, і майте на увазі,
# які з них є загальними, а які ні. Наприклад, ім’я має бути атрибутом Person, тоді як зарплата має бути доступна лише вчителю.
 

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

# Task 4

# Спеціальний виняток
# Створіть власний виняток під назвою "CustomException", ви можете успадкувати від базового класу винятків, але розширити його функціональність до
# реєструвати кожне повідомлення про помилку у файлі з назвою 'logs.txt'. Поради: використовуйте метод __init__, щоб розширити функціональні 
# можливості для збереження повідомлень у файл

# '''

# class CustomException(Exception):
# def __init__(self, msg):

# '''

# '''