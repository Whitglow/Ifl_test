class BaseConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def convert(self, to):
        to = to.lower()
        if to in ["k", "kelvin"]:
            return self.celsius + 273.15
        elif to in ["f", "fahrenheit"]:
            return self.celsius * 9 / 5 + 32
        else:
            return "Ошибка: Неизвестная единица измерения"

# Ввод пользователя
celsius = float(input("Введите температуру в Цельсиях: "))
unit = input("Конвертировать в (K - Кельвины, F - Фаренгейты): ").strip().upper()

converter = BaseConverter(celsius)
print(f"Результат: {converter.convert(unit)}")
