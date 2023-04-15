import random

N = int(input("Введите арбузов: "))
min = 20
max = 1
for _ in range(N):
    weight = random.randint(1, 20)
    print(weight, end=" ")
    if weight < min:
        min = weight
    else: 
        if weight > max:
            max = weight
print(f"\n {max} {min}")
