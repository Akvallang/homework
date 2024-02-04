# Task 1

# Перевантаження методу.
# Створіть базовий клас під назвою Animal за допомогою методу під назвою talk, а потім створіть два підкласи: Dog і Cat і створіть їх власну реалізацію
# of the method talk бути іншим. Наприклад, собака може надрукувати «гав гав», а кот — «мяу».
# Крім того, створіть просту загальну функцію, яка приймає як вхідний екземпляр класів Cat або Dog і виконує метод talk для вхідного параметра.
 
class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return "гав гав!"

class Cat(Animal):
    def talk(self):
        return "мяв мяв!"

def animal_talk(animal_instance):
    return animal_instance.talk()

dog_instance = Dog()
cat_instance = Cat()

print(animal_talk(dog_instance))  
print(animal_talk(cat_instance))  


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

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return f"Library: {self.name}, Books: {len(self.books)}, Authors: {len(self.authors)}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"Book: {self.name} ({self.year}), Author: {self.author.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return f"Author: {self.name}, Country: {self.country}, Birthday: {self.birthday}"



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

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator не може бути нулем.")
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __add__(self, other):
        result_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def __sub__(self, other):
        result_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def __mul__(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Не може бути нулем.")
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        return Fraction(result_numerator, result_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    result = x + y
    print(result)  
    print(result == Fraction(3, 4)) 
