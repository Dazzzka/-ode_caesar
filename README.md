result = ""
chipher = []

lang = input("Введите язык EN/RU: ").lower().strip()
if lang == "ru":
    ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
if lang == "en":
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
else:
    print("нет такого варианта. выбран русский алфавит")
    ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

message = input("Введите сообщение:").lower().strip()
step = int(input("Введите шаг сдвига: "))

for index in message:
    chipher.append(ALPHABET.find(index)+step)
print(f"Шифр: {chipher}")

for index in chipher:
    result += ALPHABET[index-step]
print(f"Расшифровка: {result}")     
