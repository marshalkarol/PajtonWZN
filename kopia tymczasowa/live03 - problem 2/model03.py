#jako pierwszy krok to wykonanie m na n losowań spinów 
#wizualizacja
#policzyć magnetyzację (średni spin)
#czy dla 0 temp jest nieuporządkowanie i czy dla giga temp jest duże uporządkowanie
#co krok (macro) zapisał wygląd naszej siatki (polecane - pillow ew. matplotlib, ale lepiej pillow)
#na siatce najlepiej operować w numpy. Protip -> numpy ma funkcję convolve2d, która może być tutaj pomocna
#symulacja -> obrazki -> progress bar
#spinów powinno być koło 1000 na 1000, a nie 15 na 15

from PIL import Image, ImageDraw

img = Image.new('RGB', (1920,1024), (255, 0, 255))

draw = ImageDraw.Draw(img)

draw.rectangle((50, 50, 500, 500), (0, 255, 0))

img.save('live03/xD2.png')



# def yolo():
#     yield 'Hello'
#     yield 'World'
#     yield '!'

# for w in yolo():
#     print(w)

# print(type(yolo()))



# def my_range(maxv):
#     index = 0
#     while index < maxv:
#         yield index, 'Hakuna matata'
#         index += 1

# for i in my_range(10):
#     print(i)


#classes 101
# class student:
#     pass

# class Student:
#     def __init__(self):
#         print("I'm a student!")

# s1 = Student()
# s2 = Student()


# class Student:
#     classes = []

#     def __init__(self):
#         print("I'm a student!")

# s1 = Student()
# s2 = Student()
# #dodawanie w ten sposób powoduje dodanie do listy klasy, a nie do konkretnego obiektu
# s1.classes.append("PwZN")
# s2.classes.append('WdPRiR')

# print(s1.classes, s2.classes, Student.classes)
# print(Student.__dict__)



# class Student:
#     def __init__(self):
#         self.classes = []
#         print("I'm a student!")

# s1 = Student()
# s2 = Student()

# s1.classes.append("PwZN")
# s2.classes.append('WdPRiR')

# s1.lol = 'lol'

# print(s1.classes, s2.classes, s1.lol)
# print(s1.__dict__, s2.__dict__)



# class Student:
#     def __init__(self):
#         self.classes = []
#         print("I'm a student!")

#     def print_classes(self, od_czapy):
#         print(self.classes, od_czapy)

# s1 = Student()
# s2 = Student()

# s1.classes.append('PwZN')
# s2.classes.append('WdPRiR')

# s1.print_classes('xD')
# Student.print_classes(s1, 'xD')

# print(s1.classes, s2.classes)
# print(s1.__dict__, s2.__dict__)



# class Student:
#     def __init__(self):
#         self.classes = []
#         self._private_attr = 3213
#         print("I'm a student!")

#     def __getitem__(self, pp):
#         print(pp)
#         return 9001

#     def print_classes(self, od_czapy):
#         print(self.classes, od_czapy)

#     def __len__(self):
#         return 232131

# s1 = Student()

# print(s1['xD'])
# print(len(s1))
# print(s1._private_attr)


### basic inheritance   UNIKAĆ DZIEDZICZENIA 

# class Parent:
#     def __init__(self):
#         self.parent_atr = 3
#         print('Hello from Parent!')

#     def parent_function(self):
#         print('Function from Parent!')
    
#     def other_function(self):
#         self.parent_function()

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print('Hello from Child!')

#     def parent_function(self):
#         print('Function from Child!')

# c = Child()
# c.other_function()



class Parent:
    def __init__(self):
        self.parent_atr = 3
        print('Hello from Parent!')

    def parent_function(self):
        print('Function from Parent!')

    __parent_function = parent_function
    
    def other_function(self):
        self.__parent_function()

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Hello from Child!')

    def parent_function(self):
        print('Function from Child!')

print(Parent.__dict__)
print(Child.__dict__)

c = Child()
c.other_function()