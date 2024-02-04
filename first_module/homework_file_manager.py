# Task 1
# Файли

# Напишіть сценарій, який створює новий вихідний файл під назвою myfile.txt і записує рядок "Hello file world!" в цьому. 
# Потім напишіть інший сценарій, який відкриває myfile.txt, читає та друкує його вміст. Запустіть два сценарії з командного 
# рядка системи.
# Чи відображається новий файл у каталозі, де ви запускали свої сценарії?
# Що, якщо ви додасте інший шлях до каталогу, переданого для відкриття?

# Примітка: методи запису файлів не додають символи нового рядка до ваших рядків; додайте явний "\n" у кінці рядка, 
# якщо ви хочете повністю завершити рядок у файлі.

with open ("my_file.txt", "w") as file:
    file.write("Hello file word")

with open ("my_file.txt", "r") as file:
    txt = file.read()
print(txt)

text = (""" \n\nДобрий день, люди! Добрий день буде
Буде або ні!
Все на шару буде, розпродаж буде
Буде або ні!
Подивись налєво, подивись направо
Танцюють там і тут (танцюють там і тут)
Кароче, браво
Галлівуд!
Мене кумарить, марить, нудить від цих менуетів
Від таких куплєтов, тіпа "Кружатся планеты где-то"
А час мина, нема за шо, і скоро восьме березня
І я своїй коханій — тюльпани в целафані
Затанцюю менуети
Шо робити, коли музики ніхто не слухає?
Затанцюю менуети
"Слава, где ты? Приходи, тебя я жду!""")
with open ("D:\homework\Homeworks\my_functions\made_in_hw.txt", "w+", encoding="utf-8" ) as new_file:
    new_file.write(input("Напиши щось сюди в файл: "))
    new_file.write(text)
    new_file.seek(0)
    file_content = new_file.read()
    print(new_file.name,"\n", file_content)



# Task 2 
# Ледь зробив. Здебільшого замучував чат гпт, вчився разом із ним, морочився кілька днів. Саме тому код такий величезний. 
# Але загалом суть наче вловив. Загалом, може настпним студентам на майбутнє - генерити код через чат гпт то ще та лажа =)
# Він починає пихати в код все що знає, і неокріпші студентські уми починають тонути в том ізобілії штучноінтелектного коду.
# Перевіряти правити і корегувати власнонаписаний - ок, часто допомагає знайти помилки синтаксису. Але я дмаю що промучився так довго саме
# через то що намагався зрозуміти його хід думки і виправити його код =)
# 
# Розширте програму Телефонна книга
# Функціональність програми Телефонна книга:
# Додайте нові записи
# Пошук по імені
# Пошук за прізвищем
# Пошук за ПІБ
# Пошук за номером телефону
# Пошук за містом або штатом
# Видалити запис для даного номера телефону
# Оновити запис для вказаного номера телефону
# Можливість виходу з програми

# Першим аргументом програми має бути назва телефонної книги. Програма повинна завантажити дані JSON, 
# якщо вони присутні в папці з програмою, інакше виникне помилка. Після виходу користувача всі дані мають бути збережені
# в завантаженому JSON.

import json
# Завантаження телефонної книги
def load_contact_book():
    try:
        with open("D:\\homework\\data_files\\my_cellbook.json", 'r', encoding="utf-8") as cellbook_file:
            return json.load(cellbook_file)
    except FileNotFoundError:
        return []

# Збереження телефонної книги
def save_contact_book(contact_book):
    with open("D:\\homework\\data_files\\my_cellbook.json", 'w', encoding="utf-8") as cellbook_file:
        json.dump(contact_book, cellbook_file, indent=2, ensure_ascii=False)

# Додавання нового запису
def add_contact(contact_book):
    new_contact = {
        "last_name": input("Прізвище: ").title(),
        "name": input("Ім'я: ").title(),
        "father_name": input("По батькові: ").title(),
        "tel_num": input("Номер телефону: "),
        "city": input("Місто: ").title()
    }
    contact_book.append(new_contact)
    save_contact_book(contact_book)

    print("Запис додано!")

# Пошук по імені
def search_by_name(contact_book):
    search_name = input("Введіть ім'я для пошуку: ")
    results = [contact for contact in contact_book if contact["name"] == search_name]
    print_results(results)

# Функція для виводу результатів пошуку
def print_results(results):
    if results:
        for idx, result in enumerate(results, 1):
            print(f"\nРезультат #{idx}")
            print_contact(result)
    else:
        print("Записів не знайдено.")

# Функція для виводу контакту
def print_contact(contact):
    print(f"Ім'я: {contact['name']}")
    print(f"Прізвище: {contact['last_name']}")
    print(f"По батькові: {contact['father_name']}")
    print(f"Номер телефону: {contact['tel_num']}")
    print(f"Місто: {contact['city']}")

# Фнкція видалення контактів
def delete_contact(contact_book):
    tel_num_to_delete = input("Введіть номер телефону для видалення запису: ")

    for contact in contact_book.copy():
        if contact["tel_num"] == tel_num_to_delete:
            contact_book.remove(contact)
            print(f"Запис для номера {tel_num_to_delete} видалено!")
            save_contact_book(contact_book)
            break
    else:
        print("Контакт для видалення не знайдено.")

    input("Натисніть Enter, щоб продовжити...")

# Функція редагування контактів
def update_contact(contact_book):
    tel_num_to_update = input("Введіть номер телефону для оновлення запису: ")
    for contact in contact_book:
        if contact["tel_num"] == tel_num_to_update:
            contact["name"] = input("Нове ім'я: ")
            contact["last_name"] = input("Нове прізвище: ")
            contact["father_name"] = input("Нове по батькові: ")
            contact["city"] = input("Нове місто: ")
            print("Запис оновлено!")
            save_contact_book(contact_book)
            break
    else:
        print("Запис не знайдено.")

# Функція пошуку за прізвищем
def search_by_last_name(contact_book):
    search_last_name = input("Введіть прізвище для пошуку: ")
    results = [contact for contact in contact_book if contact["last_name"] == search_last_name]
    print_results(results)

# Функція пошуку за ПІБ
def search_by_full_name(contact_book):
    search_full_name = input("Введіть ПІБ для пошуку: ")
    results = [contact for contact in contact_book if search_full_name.lower() in f"{contact['name']} {contact['last_name']} {contact['father_name']}".lower()]
    print_results(results)


# Головна функція програми
def main():
    contact_book = load_contact_book()

    while True:
        print("\nМеню:")
        print("1. Додати новий запис")
        print("2. Пошук по імені")
        print("3. Пошук за прізвищем")
        print("4. Пошук за ПІБ")
        print("5. Видалити запис за номером телефону")
        print("6. Оновити запис за номером телефону")
        print("7. Зберегти дані та вийти з програми")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            search_by_name(contact_book)
        elif choice == "3":
            search_by_last_name(contact_book)
        elif choice == "4":
            search_by_full_name(contact_book)
        elif choice == "5":
            delete_contact(contact_book)
        elif choice == "6":
            update_contact(contact_book)
        elif choice == "7":
            save_contact_book(contact_book)
            print("Дякую за використання телефонної книги. Дані збережено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

contact_book = load_contact_book()
load_contact_book()
save_contact_book(contact_book)
main()