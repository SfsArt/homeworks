print("На скільки поставити таймер? (секунд чи хвилини)", "\n", "1. Секунди", "\n", "2. Хвилини")

if input() == "1":
    print("введіть кількість секунд:")
    seconds = int(input())
    print("Таймер запущено на", seconds, "секунд")
    while seconds > 0:
        print(seconds, "секунд залишилось")
        seconds -= 1
    print("Відлік завершено!")
elif input() == "2":
    print("введіть кількість хвилин:")
    minutes = int(input())
    seconds = minutes * 60
    print("Таймер запущено на", minutes, "хвилин")
    while seconds > 0:
        print(seconds / 60, "хвилин залишилось", "(", seconds, "секунд)")
        seconds -= 1
    print("Відлік завершено!")
else:
    print("Невірний вибір. Будь ласка, виберіть 1 або 2.")




#Всплывающие подсказки (Hover): Найдите editor.hover.enabled и снимите галочку.