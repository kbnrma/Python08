# 1) 
for i in range(5):
    print(i, "0" * 5)

# 2) 
my_list = []
for i in range(1, 101):
    my_list.append(i)
print(my_list)
 
# 3) 
for i in range(1,497):
    if i % 2 == 0:
        print(i, "чётный")

# 4)
numbers = list (range(1, 1001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 5)
lst = [0 for i in range(100)]
print(lst)

# 6) 
it_company = ('Google', 'Amazon', 'Microsoft')
it_company = list (it_company)
it_company.append('Tesla')
it_company = tuple(it_company)
print(it_company)

# 7)
it_company = ('Google', 'Amazon', 'Microsoft')
print(it_company.index('Amazon'))

# 8)
it_company = ('Google', 'Amazon', 'Microsoft')
it_company = list(it_company)
it_company [0] ='Apple'
it_company = tuple(it_company)
print(it_company)

# 9) 
it_company = ('Apple', 'Amazon', 'Microsoft')
print(it_company[0:3:2])

# 10) 
text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
'overview')
print(text_tuple.count('Python'))

# ДОП ЗАДАНИЕ:
# 6) 
ab = input("Введите число:")
cd = input("Введите число:")
ab, cd = cd, ab
print(ab, cd)

# 7)
while True:
    age = int(input("Введите ваш возраст: "))
    if age >= 18:
        print("Доступ разрешен")
        break 
    else:
        print("Извините, пользование данным ресурсом только с 18 лет")