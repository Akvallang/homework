# Завдання 1
# Напишіть програму Python для визначення кількості локальних змінних, оголошених у функції.

def local_functions_counter():
    first_var = 11
    second_var = 22
    third_var = 33
    local_vars = locals()
    
    print("We have ", len(local_vars), "local variables: ", local_vars)
    
local_functions_counter()

# Завдання 2
# Напишіть програму Python для доступу до функції всередині функції (Поради: використовуйте функцію, яка повертає іншу функцію)


def mother_function():
    print("Inside this function live one more function:")
    def daughtr_function():
        print("Hi! Im daughter function. Are you calling me?")
    return daughtr_function

var_for_daughter_func = mother_function()
var_for_daughter_func()

        


# Завдання 3
# Напишіть функцію під назвою "choose_func", яка приймає список nums і 2 функції зворотного виклику. Якщо всі числа в списку додатні, 
# виконайте першу функцію зі списку та поверніть її результат. В іншому випадку поверніть результат другого


def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)
        
 
# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

result_1 = choose_func(nums1, square_nums, remove_negatives)
print(f"Result for 1st case: {result_1}")

result_2 = choose_func(nums2, square_nums, remove_negatives)
print(f"Result for 2nd case: {result_2}")

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

print()