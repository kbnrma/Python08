# def reverse_name (name:str="Alihan")->str:
#     return name [::-1]
# print(reverse_name())
# print(reverse_name("Nurbolot"))

# def hello(word:str="Python")->str:
#     print("Geeks")
#     print("Hello")
#     return "Alihan"
# print (hello())

# def calculator (num1:int=1, operator:str="+", num2:int=1)->int:
#     "Базовая функция калькулятора на Python"
#     if operator == "+":
#         return num1+num2
#     elif operator == "-":
#         return num1-num2
#     elif operator == "*":
#         return num1*num2
#     elif operator == "/":
#         return num1/num2
#     else:
#         return "Такого оператора нет"
# print(calculator(10, "*", 10))
# print(calculator(10, "/", 3))
# print(calculator(1, "Alihan", 2))





#Args, kwargs
# print("Hello", "World", "and", "Python")
# def welcome(name, name2):
#     print("Добро пожаловать", name)
#     print("Добро пожаловать", name2)
# welcome("Nurbolot", "Alihan", "Kurmanbek")

# def args_welcome (*args):
#     for name in args:
#         print("Добро пожаловать", name)
# # args_welcome("Nurbolot", "Alihan", "Kurmanbek", 'Beksultan', 'Askat')

# def avg_student (name:str="Askat", *points)->str:
#     print(name, sum(points)/len(points), round(sum(points)/len(points)))
# avg_student('Alihan', 3, 3, 3, 3, 4, 4, 4, 5, 2)
# avg_student('Nurbolot', 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 5)
# avg_student('Askat', 4, 4, 4, 5, 5, 5, 5, 5, 3, 3, 3, 3)

# def translate (**words)->dict:
#     print(words)
# translate(USA="США", Apple="Яблоко", car="машина", phone="телефон")





#Лямбда - функция lambda
# def simple_function(num:int)->int:
#     return num*num
# print(simple_function(20))

# lambda_function = lambda num: num*num
# print(lambda_function(20))

# print((lambda num: num*num)(20))

# Пример 2
# def add(num1:int=10, num2:int=10)->int:
#     return num1+num2
# print(add(20, 20))

# add_lambda = lambda num1, num2: num1 + num2
# print(add_lambda(20, 20))

# print((lambda num1, num2: num1+num2)(20, 20))

# Пример 3 
# numbers = [10, 20, 30, 40, 50]
# new_numbers = []
# def mult_two(nums:list)-> list:
#     for i in nums:
#         new_numbers.append(i*2)
#     return new_numbers
# print(mult_two(numbers))

# numbers = [10, 20, 30, 40, 50]
# new_numbers = list(map(lambda nums: nums *2, numbers))
# print(new_numbers)

# numbers = [10, 20, 30, 40, 50]
# print(list(map(lambda nums: nums *2, numbers)))

# print(list(map(lambda nums: nums *2, [10, 20, 30, 40, 50])))

# Пример 4 
# numbers = [10, 3, 4, 5, 6, 555, 333, 1001, 1002, 1114]
# chet = []
# def check_chet(nums:list)->list:
#     for num in nums:
#         if num %2 == 0:
#             chet.append(num)
#     return chet
# print(check_chet(numbers))

# numbers = [10, 3, 4, 5, 6, 555, 333, 1001, 1002, 1114]
# chet = list(filter(lambda nums: nums %2 == 0, numbers))
# print(chet)

# numbers = [10, 3, 4, 5, 6, 555, 333, 1001, 1002, 1114]
# print(list(filter(lambda nums: nums %2 == 0, numbers)))

print(list(filter(lambda nums: nums %2 == 0, [10, 3, 4, 5, 6, 555, 333, 1001, 1002, 1114])))