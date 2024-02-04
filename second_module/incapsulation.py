# Task 1

# Перевантаження методу.
# Створіть базовий клас під назвою Animal за допомогою методу під назвою talk, а потім створіть два підкласи: Dog і Cat і створіть їх власну реалізацію
# of the method talk бути іншим. Наприклад, собака може надрукувати «гав гав», а кот — «мяу».
# Крім того, створіть просту загальну функцію, яка приймає як вхідний екземпляр класів Cat або Dog і виконує метод talk для вхідного параметра.
 

# Task 2

# Бібліотека
# Напишіть структуру класу, яка реалізує бібліотеку. Класи:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

# Усі 3 класи повинні мати читабельні методи __repr__ і __str__.
# Крім того, клас книги повинен мати змінну класу, яка містить кількість усіх існуючих книг
# '''

# class Library:
#     pass

# class Book:
#     pass

# class Author:
#     pass

# '''

# Task 3
# Fraction
# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок. 
# Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

# class Fraction:
#     pass

# if __name__ == "__main__":
#     x = Fraction(1, 2)
#     y = Fraction(1, 4)
#     x + y == Fraction(3, 4)