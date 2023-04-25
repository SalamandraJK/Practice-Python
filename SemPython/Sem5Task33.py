# Задача №33. 
# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

import random
 
list_1 = []
n = int(input('Введите колличество оценок: '))
for i in range(n):
    list_1.append(random.randint(1, 5))
print(list_1)
max_num = max(list_1)
min_num = min(list_1)
arr = 0   

# for i in range(n):
#     if list_1[i] == max_num:
#         list_1[i] = min_num

for i, elem in enumerate(list_1):
    if elem == max_num:
        list_1[i] = min_num
print(list_1)
print(f"Максимальная оценка: {max_num}")
print(f"Минимальная оценка: {min_num}")

