
numbers = []

print("Введіть 5 чисел:")

for i in range(5):
    numbers.append(int(input("Число: ")))



print(numbers)

total = sum(numbers)
middle = total / 5

print(total)

print(middle)