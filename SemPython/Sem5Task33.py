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
max_num = 5
min_num = 5
for i in list_1:
    if list_1[i] < min_num:
        min_num = list_1[i] 
        i += 1
    else: 
        if list_1[i] == max_num:
            list_1[i] = min_num
            i += 1

print(list_1)