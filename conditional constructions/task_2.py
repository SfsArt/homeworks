age = int(input("введіть вік:"))

if age < 18:
    print("Дитина")
elif age >= 18 and age <= 60:
    print("Дорослий") 
elif age > 60:
    print("Пенсіонер")