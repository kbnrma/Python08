# Tuple -кортежи. Циклы for и while
# int, float, bool, str, tuple - неизменные
# list - изменный

# names = ('Kurmanbek', 'Beksultan', 'Nurbolot')
# print(names)
# print(names[0])
# print(names[1::3])
# print(names[::2])

# lst = ['Hello']
# print(type(lst))

# tup = ('Hello')
# print(type(tup))

# tup = ('Hello', '10', '0.1', 'True', [1,2,3,4],(1,2,3,4))
# print(tup) 
# print([4][0])

# cars = ('BMW', 'Mersedes', 'Audi')
# print(cars) 
# lst_cars = list(cars)
# print(lst_cars)
# lst_cars.append('Tesla')
# cars = tuple(lst_cars)
# print(cars)

# import dis
# lst = ['1, 2, ,3, 4, 5']
# lst.append(10)
# tup = ('1, 2, ,3 ,4, 5')

# dis.dis ('lst')
# dis.dis ('tup')

# Циклы for, while

# for num in range (1001):
#     print(num,"Geeks")

# for i in range(10,51):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

# for n in range(1000001):
#     print(n)            # CTRL+C to interrupt

# numbers = [10, 11, 100, 333, 445, 34, 45, 67, 2]
# for n in numbers:
#     if n % 2 == 0:
#         print(n, "Чётный")
#     else:
#         print(n, "Нечётный")

# it = ["Geeks", "Meta", "Google", "Neobis"]
# for i in it:
#     print(i)
#     if i == "Google":
#         break       #Досрочно прерывает цикл. Contunie - продолжает цикл.

# name = "Nurbolot"
# for n in name:
#     print(n)

# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 += 1
#     print(num1)

# n = 0
# while True:
#     n += 1
#     print("Geeks", n)

# while True:
#     num1 = int(input("Number1: "))
#     operator = input("+, -, *, /: ")
#     num2 = int(input ("Number2: "))
#     if operator == "+":
#         print("Ответ: ", num1 + num2)
#     elif operator == "-":
#         print("Ответ: ", num1 - num2)
#     elif operator == "*":
#         print("Ответ: ", num1 * num2)
#     elif operator == "/":
#         print("Ответ: ", num1 / num2)
#     elif num1 == 0 and num2 ==0 and operator == "0":
#         print("Stop")
#         break
#     else:
#         print("Такого оператора не существует")


# import random
# random_number = random.randint (1,10)
# attempt = 0
# while True:
#     input_number = int(input("Введите число от 1 до 10: "))
#     if input_number >= 1 and input_number <= 10:
#         attempt += 1
#         if input_number == random_number:
#             print("Вы выиграли! Поздравляем!")
#         break
#     elif attempt == 5:
#         print("Вы проиграли:")
#         break
#     else:
#         print("Неправильно у вас", 5 - attempt, "попыток")
# else: 
#     print("Введите число от 1 до 10!")
# print(random.randint(1,10))