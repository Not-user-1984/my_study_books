string1 = "Привет мир!"
string2 = "こんにちは世界！"
print(string1)
print(string2)

# запись строк в файл как utf-8
with open("test.txt", mode="w", encoding="utf-8") as file:
    file.write(string1 + "\n")
    file.write(string2 + "\n")

# чтение строк из файла как utf-8
with open("test.txt", mode="r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line.split())
