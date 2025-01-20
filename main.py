
print("Привет, друг!")
ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz"
alphabet=ALPHABET_RU
result=""

lang=input("Введите язык EN/RU: ")
if lang == "EN":
    alphabet = ALPHABET_EN
if lang == "RU":
    alphabet = ALPHABET_RU
else:
    print("нет такого варианта")
if alphabet:
    message=input("Введите сообщение:").lower()
    chipher=[]
    print(message)
    step =int(input("Введите шаг сдвига:"))
    for i in message:
        chipher.append(alphabet.find(i)+step)    
    print(chipher)
    for i in chipher:
        result +=(alphabet[i-step])
    print(result)







