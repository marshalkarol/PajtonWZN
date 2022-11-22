# class FunctionClass:
#     def __call__(self):
#         print('Hello Call!')

# fc = FunctionClass()

# fc()


class ClassDecorator:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('Hello from Decorator Class')
        return self._func(*args, **kwargs)


@ClassDecorator
def my_function():
    s = 'My Function'
    print(s)
    return s

# print(type(my_function))

my_function()