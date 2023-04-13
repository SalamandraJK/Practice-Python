Num = int(input('Введите чило N: '))
multiplication = 1
Control = 1
if Num == 0:
    print(f"Факториал числа {Num} = {multiplication}")
elif Num < 0:
    print(f"Введено отрицательно число {Num}")
else:
    while Control <= Num:
        multiplication *= (Control)
        Control += 1
    print(f"Факториал числа {Num} = {multiplication}")
