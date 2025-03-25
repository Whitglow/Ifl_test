import random

# Создаем массив из 10 случайных чисел от 0 до 1
array_size = 10
array = [random.randint(0, 10) for _ in range(array_size)]

# Вычисляем максимальное, минимальное и среднее значение
max_value = max(array)
min_value = min(array)
avg_value = sum(array) / len(array)

# Вычисляем обычное среднее значение
avg_value = sum(array) / len(array)

# Находим ближайшее к среднему число
closest_to_avg = min(array, key=lambda x: abs(x - avg_value))

print(f"Массив: {array}")
print(f"Максимальное: {max_value}")
print(f"Минимальное: {min_value}")
print(f"Среднее: {closest_to_avg}")
