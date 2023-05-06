# Функции - functions
# print("Geeks")
# def hello_world():
#     print("Hello World") 
# # hello_world()

# def add():
#     num1 = int(input("Number1: "))
#     num2 = int(input("Number2: "))
#     print(num1+num2)
# add()

# def count_numbers(): 
#     numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     for number in numbers:
#         if number %2 ==0:
#             print(number, "чётный")
#         else:
#             print(number, "нечётный")
# count_numbers()      

# def reverse_word (word): 
#     print(word[::-1])
# reverse_word("Geeks")   
# reverse_word("Python")  
# reverse_word('Django')

# def hello(name): 
#     print("Привет,", name)
# hello("Kurmanbek")
# hello("Beksultan")

# def test(word:str) -> str:
#     "My testing function"
#     print(word+word)
# test("geeks")
# test(10)

# def mult (num1:int=1, num2:int=1) -> int:
#     print("Ответ: ", num1*num2)
# mult(10, 10)
# mult(10, 20)

# def calculator (num1:int=1, num2:int=1, operator:str="+")->int:
#     "Simple calculator Python with function def"
#     if operator == "+":
#         print("Ответ:", num1+num2) 
#     elif operator == "-":
#         print("Ответ:", num1-num2)
#     elif operator== "*":
#         print("Ответ:", num1*num2)
#     elif operator =="/":
#         print("Ответ:", num1/num2)
#     else:
#         print ("Такого ответа нет")
# calculator(10, 20, "+") 
# calculator(10, 20, "*")
# calculator(10, 3, "/")
# calculator(30, 5, "-")

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Деление на ноль")

# try:
#     print(10+"5")
# except TypeError:
#     print("Ошибка типа данных")
#     num1 = 10
#     num2 = 20
#     print(num1+num2)

# try:
#     print(10+10)
# except BaseException:
#     print("Code Error")

# while True:
#     try:
#         num1 =int(input("Number1: "))
#         operator =input("Operatop: ")
#         num2 =int(input("Number2: "))
#         if operator == "+":
#             print("Ответ:", num1+num2) 
#         elif operator == "-":
#             print("Ответ:", num1-num2)
#         elif operator== "*":
#             print("Ответ:", num1*num2)
#         elif operator =="/":
#             try:
#                 print("Ответ: ", num1/num2)
#             except ZeroDivisionError:
#                 print("Nope")   
#         else:
#             print ("Такого ответа нет")
#     except ValueError:
#         print("Введите цифры")
