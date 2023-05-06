# 1) Напишите функцию, которая принимает фразу, и возвращает его сокращенную
# форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest --
# FYI и т.п.
# def abcd (*phrase):
#     words == list(phrase.split())
#     first_letters = [word[0] for word in words] 
#     return ''.join(first_letters).upper()  
# print (abcd ("Кыргызская Республика", "Ruby on Rails", "For your interest"))

# 2) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
# фразе было использовано. Например: “Money, money, money, it’s always sunny, in
# the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1,
# world: 1.
# def counting (words):
#     text = str(words)
#     print(text.count)
#     return 
# counting('Money, money, money, it's always sunny, in the richmen's world')

# 3) Напишите функцию, которая принимает слово и возвращает True, если слово
# изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.
# def iso_word (word):
#     if word == set:
#         return True
#     else:
#         return False
# print (iso_word({"Numu"}))

# 4) 
# def reverse_num (n):
#     reverse_str = str(n)[::-1]
#     return int(reverse_str)
# print (reverse_num(27))

# ДОП ЗАДАНИЕ:
# 5) Напишите функцию -- чат-бот с бесконечным циклом, который
# a. Всегда отвечает “Конечно!” на любой вопрос
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же
# духе!” Если вызвал функцию, но ничего не передал.
# d. В любых других случаях, отвечает “ну и что"









# def shorten_phrase(phrase):
#     words = phrase.split()  # разделить строку на список слов
#     first_letters = [word[0] for word in words]  # извлечь первую букву каждого слова
#     return ''.join(first_letters).upper()  # объединить буквы в строку и вернуть ее в верхнем регистре
# shorten_phrase("Кыргызская Республика")
# # 'КР'




# def count_words(sentence):
#     words = sentence.lower().split()  # привести все слова к нижнему регистру и разделить строку на список слов
#     word_counts = {}  # создать пустой словарь для хранения количества каждого слова
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1  # увеличить счетчик, если слово уже в словаре
#         else:
#             word_counts[word] = 1  # добавить слово в словарь, если оно еще не было обнаружено
#     return word_counts
# >>> count_words("Money, money, money, it's always sunny, in the richmen's world")
# {'money,': 3, "it's": 1, 'always': 1, 'sunny,': 1, 'in': 1, 'the': 1, "richmen's": 1, 'world': 1}


# def is_isogram(word):
#     letters = set()  # создать множество для хранения букв
#     for letter in word:
#         if letter.isalpha():  # проверить, является ли символ буквой
#             if letter in letters:  # если буква уже встречалась, то слово не является изограммой
#                 return False
#             letters.add(letter)  # добавить букву в множество
#     return True  # если функция дошла до этого места, значит слово является изограммой


# def reverse_integer(n):
#     reversed_n = 0
#     is_negative = n < 0  # сохранить информацию о том, является ли число отрицательным
#     if is_negative:
#         n = -n  # перевести число в положительную форму для удобства
#     while n > 0:
#         reversed_n = reversed_n * 10 + n % 10  # добавить следующую цифру в перевернутое число
#         n //= 10  # удалить последнюю цифру из исходного числа
#     return -reversed_n if is_negative else reversed_n  # вернуть перевернутое число с учетом знака

# def chat_bot():
#     while True:
#         user_input = input("Ты: ")
        
#         if not user_input:
#             print("Бот: Как классно, когда ты молчишь. Продолжай в том же духе!")
#         elif user_input.isupper():
#             print("Бот: Успокойся")
#         else:
#             print("Бот: Конечно!")
# chat_bot()
