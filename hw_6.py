# # 1. Создать класс под названием data, в класс добавить атрибуты full_na\.\w+me, email, file_name, color. 
# # Добавить геттеры и сеттеры для всех атрибутов
# # 2. Затем считать из файла MOCK_DATA.txt, в котором 1000 строк с данными (Имя и
# # Фамилия, почта, название файла с расширением и код цвета)
# # 3. Из каждой считанной строки создать объект класса data и добавить его в список.
# # 4. Затем через цикл пройтись по каждому объекту и записать в 4 разных файла все типы информации. (1й файл: Имена с фамилиями, 2й файл: почта, 3й файл: названия файлов с расширением, 4й файл: коды цветов)

import re

class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def file_name(self):
        return self.__file_name
    
    @property
    def color(self):
        return self.__color


    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @email.setter
    def email(self, value):
        self.__email = value

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @color.setter
    def color(self, value):
        self.__color = value


with open('MOCK_DATA.txt', 'r', encoding="utf-8") as file:
    content = file.readlines()

people = []
for line in content:
    print(re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", line))
    full_name = re.findall(r"^[A-Za-z'\-]+\s[A-Za-z'\-]+", line)[0]
    email = re.findall(r"[a-zA-Z0-9]+@[-a-zA-Z0-9]+\.[a-zA-Z0-9]+", line)[0]
    file_name = re.findall(r"\t\w+\.\w+", line)[0].replace("\t", '')
    color = re.findall(r"#\w+", line)[0].replace("\t", '')
    people.append(Data(full_name, email, file_name, color))

print(people)

with open('fullname.txt', 'w', encoding="utf-8") as fullname_file:
    for i in people:
        fullname_file.write(i.full_name + '\n')

with open('mail.txt', 'w', encoding="utf-8") as mail_file:
    for i in people:
        mail_file.write(i.email + '\n')

with open('file.txt', 'w', encoding="utf-8") as file_file:
    for i in people:
        file_file.write(i.file_name + '\n')

with open('color.txt', 'w', encoding="utf-8") as color_file:
    for i in people:
        color_file.write(i.color + '\n')
