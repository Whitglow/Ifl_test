import random

# Создаем массив из 10 случайных чисел от 0 до 1
array_size = 10
array = [random.random() for _ in range(array_size)]

# Вычисляем максимальное, минимальное и среднее значение
max_value = max(array)
min_value = min(array)
avg_value = sum(array) / len(array)

print(f"Массив: {array}")
print(f"Максимальное: {max_value}")
print(f"Минимальное: {min_value}")
print(f"Среднее: {avg_value}")
