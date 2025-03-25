word = "Hello"
char_count = {}

# Подсчет символов в слове
for char in word.lower():
    if char in char_count:
        print(f"Первый повторяющийся символ: {char}")
        break
    char_count[char] = 1
