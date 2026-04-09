numbers = []

print("Введіть числа:")

print("Якщо не хочете продовжуввати ввід, натисність d")

c = 0

while True:
    user_input = input("Число: ").strip()
    
    if user_input.lower() == 'd':        
        break
    
    try:
        num = int(user_input)
        numbers.append(num)
        c += 1
    except ValueError:
        print("Помилка! Введіть число або 'd' для завершення")

c -= 1

# print(c)

numbers.sort()

# print(numbers)

print("Найбільше число у списку:",numbers[c], "Найменше число у списку:",numbers[0])

total = sum(numbers)
middle = total / (c + 1)

print("Середнє число:",middle)

print("Парні числа:")
for numb in numbers:
    if numb % 2 == 0:
        print(numb)

