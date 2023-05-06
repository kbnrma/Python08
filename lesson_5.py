# Множества set, frozenset
# numbers = {1, 2, 3, 4, 5, 5, "5"}
# print(numbers)
# print(numbers[0:2])

# it_company = {"Google", "Meta", "Space X"}
# print(it_company)
# it_company.add("Tesla")
# print(it_company)
# it_company.remove("Google")
# print(it_company)
# it_company.pop()
# print(it_company)

# st = {1, 0.1, "Hello", False, (1, 2, 3)}    # list, set - нельзя хранить 
# print(st)

# nums1 = [1, 2, 3, 4, 5]
# nums2 = [3, 4, 5, 6, 7]
# nums3 = nums1 + nums2
# print(list(set(nums3)))

# cars = {"BMW", "DODGE", "TESLA", "HONDA"}
# for car in cars:
#     print(car)

# numbers = {1, 0.1, 100, 4, 99, 1111, 9, 8, 34}
# print(sorted(numbers))

# st = {1, 0.1, True, "1"}
# print(st)
# print(True + 1)     # True = 1
# print(False + 1)    # False = 0

# frozen_set = frozenset({1, 2, 3, 4, 5, 5, 5})
# print(frozen_set)


# Dictionary - Словари
# student = {"name" : "Askat", "age" : 18}
# print(student)
# print(len(student))
# print(student["name"])
# print(student["age"])
# student.setdefault("language", "Python")
# print(student)
# student.pop("age")
# print(student)
# student["language"] = "Java"
# print(student)

# tesla_model_x = {
#     "brand" : "Tesla",
#     "model" : "Model X",
#     "year" : 2022,
#     "price" : "46000$",
#     "color" : "white"
# }
# print(tesla_model_x["brand"])
# print(tesla_model_x.keys())
# print(tesla_model_x.values())
# print(tesla_model_x.items())

# for tesla in tesla_model_x.items():
#     print(tesla)
# for key, value in tesla_model_x.items():
#     print(key, value)

# todo_list = {
#     "08:00" : "Проснуться"
# }
# while True:
#     command = int(input("Введите команду, 1 - посмотреть список дел, 2- добавить, 3 - удалить:"))
#     if command == 1:
#         print("СПИСОК ДЕЛ:")
#         for time, task in todo_list.items():
#             print(time, task)
#     elif command == 2:
#         add_time = input("Время: ")
#         add_task = input("Задание: ")
#         todo_list.setdefault(add_time, add_time)
#         print("Задание", add_task, "Успешно добавлено на", add_time)
#         print("-------------------------")
#     elif command == 3:
#         delete_time = input("Введите время для удаления:")
#         todo_list.pop(delete_time)
#         print("Задание удалено")
#         print("-------------------------")
#     elif command == 0:
#         print("EXIT TODO")
#         break
#     else:
#         print("Такой команды нет")    
