oleh = 15
colourGreen = "green"
colourRed = "red"
#Якщо менше 15 - дитина, якщо з 15 до 18 - підліток, якщо 18 і більше - дорослий

if oleh < 15:
    print("Олег дитина.")
elif oleh >= 15 and oleh < 18:
    print("Олег підліток.")
elif oleh >= 18:
    print("Олег дорослий.")