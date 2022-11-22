#napisać własny dekorator
#sprawdzić czy działa dla jakiejś czasochłonnej funkcji (można sobie w numpy jakąś znaleźć)
#sposób na zmianę funkcjonalności funkcji

import functools
from symbol import decorator


# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper():
#         print('executed')
#         return func()

#     return wrapper

# @my_decorator
# def my_function():
#     s = 'My Function'
#     print(s)
#     return s

# #my_function = my_decorator(my_function)

# print(my_function())
# print(my_function.__name__)

##################################

# def func (x, y, z):
#     print(x, y, z)

# func(1,2,3)
# a=[1,2,3]

# func(a[0], a[1], a[2])
# func(*a)

##################################

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(args, kwargs)
#         print('executed')
#         return func(*args, **kwargs)

#     return wrapper

# @my_decorator
# def my_function(x, y, z = 7):
#     s = 'My Function'
#     print(s)
#     return x + y + z

# #my_function = my_decorator(my_function)

# print(my_function(3, 7, z = 100))

###################################

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(args, kwargs)
#         print('executed')
#         return func(*args, **kwargs)

#     return wrapper

def my_decorator(st = 'XYZ'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(st)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@my_decorator
def my_function(x, y):
    s = 'My Function'
    print(s)
    return x + y

my_function(5, 6)

# my_function = my_decorator('Hakuna matata')(my_function)
