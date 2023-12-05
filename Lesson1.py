# Декларативное: Найти сумму всех четных чисел в списке

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even = sum(filter(lambda x: x % 2 == 0, numbers))

print("Сумма четных чисел (декларативно):", sum_of_even)

# Декларативное: Найти сумму всех четных чисел в списке

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even = sum(filter(lambda x: x % 2 == 0, numbers))

print("Сумма четных чисел (декларативно):", sum_of_even)

# Декларативное: Найти сумму всех чисел в списке, больших 5

numbers = [1, 6, 3, 8, 5, 10, 7]
sum_above_5 = sum(filter(lambda x: x > 5, numbers))

print("Сумма чисел больших 5 (декларативно):", sum_above_5)

# Императивное: Сортировка пузырьком

def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [64, 25, 12, 22, 11]
bubble_sort(numbers)
print("Отсортированный список (императивно):", numbers)
Deklsort = sorted(numbers)
print(Deklsort)

# Императивное: Сортировка слиянием

def merge_sort(arr):
# Проверяем, если список длиннее 1 элемента
  if len(arr) > 1:
# Находим середину списка
    mid = len(arr) // 2

# Разделяем список на две половины
    left_half = arr[:mid]
    right_half = arr[mid:]

# Рекурсивно сортируем каждую из половин
    merge_sort(left_half)
    merge_sort(right_half)

# Инициализируем индексы для обхода левой и правой половин
    i = j = k = 0

# Объединяем отсортированные половины обратно в исходный список
    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]
        i += 1
      else:
        arr[k] = right_half[j]
        j += 1
        k += 1

# Добавляем оставшиеся элементы из левой половины (если есть)
    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1

# Добавляем оставшиеся элементы из правой половины (если есть)
    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1

# Начальный список чисел
numbers = [38, 27, 43, 3, 9, 82, 10]

# Вызываем сортировку слиянием для этого списка
merge_sort(numbers)

# Выводим отсортированный список
print("Отсортированный список (императивно):", numbers)


def counting_sort(arr):
# Находим максимальное и минимальное значения в массиве
  max_value = max(arr)
  min_value = min(arr)

# Вычисляем диапазон значений
  range_of_values = max_value - min_value + 1

# Создаем счетчик для хранения количества каждого элемента
  count = [0] * range_of_values

# Заполняем счетчик
  for num in arr:
    count[num - min_value] += 1

# Восстанавливаем отсортированный массив
    sorted_arr = []
    for i in range(range_of_values):
      sorted_arr.extend([i + min_value] * count[i])

      return sorted_arr

# Пример использования
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Отсортированный массив:", sorted_arr)