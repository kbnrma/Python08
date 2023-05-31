# 1. Написать функцию binary_search, принимающую в качестве входящего параметра 
# элемент для поиска и список в котором необходимо искать.
# 2. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме
# презентации.
# 3. Функция в итоге должна распечатать результат.
# 4. Написать функцию buble_sort или selection_sort, принимающую в качестве входящего
# параметра не отсортированный список.
# 5. Алгоритм функции должен сортировать список методом пузырьковой сортировки или
# методом сортировки выбором.
# 6. Функция в итоге должна возвращать отсортированный список.


def binary_search(element, lst):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == element:
            return mid
        if guess > element:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def bubble_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


my_list = [1, 3, 5, 7, 9, 11]
element_to_find = 7

result = binary_search(element_to_find, my_list)
if result != -1:
    print("Элемент найден на позиции", result)
else:
    print("Элемент не найден")


unsorted_list = [4, 2, 9, 1, 7, 5]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)
