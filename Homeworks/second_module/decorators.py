# Task 1

# Напишіть декоратор, який керує функцією з переданими їй аргументами.
# ПРИМІТКА! Він повинен друкувати функцію, а не результат її виконання!
# Наприклад:
#  "add called with 4, 5"
# ```
# def logger(func):
#     pass

# @logger
# def add(x, y):
#     return x + y

# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]
# '''
def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {str(args)[1:-1]}")
        return func(*args)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(1, 2, 3)


# Task 2

# Напишіть декоратор, який бере список стоп-слів і замінює їх на * в декорованій функції
# '''
# def stop_words(words: list):
#     pass

# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"

# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
# ```
def stop_words(words: list):
    def decorator(func):
        def wrapper(name):
            modified_name = []
            for word in name.split():
                if word.lower() in map(str.lower, words):
                    modified_name.append('*')
                else:
                    modified_name.append(word)
            modified_name = " ".join(modified_name)
            
            return func(modified_name.split())
        return wrapper
    return decorator

@stop_words(["pepsi", "BMW"])
def create_slogan(name):
    return " ".join(name)

result = create_slogan("Steve drinks pepsi in his brand new BMW!")
print(result)
assert result == "Steve drinks * in his brand new *!"

def stop_words(words):
    def decorator(func):
        def wrapper(name):
            modified_name = ' '.join('*' if word.lower() in words else word for word in name.split())
            return func(modified_name)
        return wrapper
    return decorator

@stop_words(['pepsi', 'bmw'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

result = create_slogan("Steve")
assert result == "Steve drinks * in his brand new *!"

# Task 3

# Напишіть декоратор "arg_rules", який перевіряє аргументи, передані функції.
# Декоратор повинен приймати 3 аргументи:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
# ```
# def arg_rules(type_: type, max_length: int, contains: list):
#     pass

# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"

# assert create_slogan('johndoe05@gmail.com') is False
# assert create_slogan('05years') is False
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

# ```

def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Argument {arg} has invalid type {type(arg)}. Expected type {type_}.")
                    return False

                if isinstance(arg, str) and len(arg) > max_length:
                    print(f"String argument {arg} exceeds maximum length of {max_length}.")
                    return False
                
                if isinstance(arg, str) and not all(char in arg for char in contains):
                    print(f"String argument {arg} does not contain required symbols: {contains}.")
                    return False

            result = func(*args, **kwargs)
            return result if all(isinstance(result, bool) and result else True for result in [result])

        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
