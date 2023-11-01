#  Task 1

my_name = "ярослав"
today = "понеділок"
print("\n")
print("Гарного дня " + my_name.__add__("е").title() + "! " + today.title() + " чудовий день щоб вивчити щось із пайтона!" ) 


# Task 2

name = "ярослав"
last_name = "глухов"
need = "має маніпулювати даними через конкатинацію!"
greeting = "привіт"
print("\n")
print(greeting.title() + " " + name.title() + "! " + "Мені сказали що" + " " + name.title() + " " + last_name.title()+ " " + need )
 

# Task 3

a = 30
b = 10
addition = a + b
subtaction = a - b
division = a / b
multiplication = a * b
exponent = a ** b
modulus = a % b
floor_divisions = a // b
print("\n")
print(a, " та ", b, ": будемо гратись із цими числами.")
print(addition, "Додавання")
print(subtaction, "Віднімання")
print(division, "Ділення")
print(multiplication, "Множення")
print(exponent, "Взведення в стпінь (експонента)")
print(modulus, "Взведення в модуль (залишок від ділення)")
print(floor_divisions, "Поверхове ділення. Ділення з округленням до найближчого цілого числа")