def clock_angle(hours, minutes):
    # Угол часовой стрелки
    hour_angle = (hours % 12) * 30 + minutes * 0.5
    # Угол минутной стрелки
    minute_angle = minutes * 6
    # Разница углов
    angle = abs(hour_angle - minute_angle)
    # Находим минимальный угол
    return min(angle, 360 - angle)

h = int(input("Введите часы (0-23): ")) % 12
m = int(input("Введите минуты (0-59): "))

print(f"Угол между стрелками: {clock_angle(h, m)}°")
