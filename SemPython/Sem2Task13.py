import random

N = int(input("Введите количество дней: "))
counts = 0
Max = 0
i = 0
for _ in range(N):
    temp = random.randint(-50, 50)
    print(temp, end=" ")
    if temp > 0:
        counts += 1
    else:
        counts = 0
    if Max < counts:
        Max = counts
print(f"\n {Max}")

