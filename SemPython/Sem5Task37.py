# Задача №37. 
# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
import random

n = int(input("Введите число: "))
list_2 = str(n)
list_1 = list(list_2)
print(*list_1)
list_1.reverse()
print(*list_1)

def rev(n):
    if n == 0:
        return " ! "
    el = random.randrange(n)
    print(el, end = " ")
    return rev(n - 1) + " " + str(el)
print(rev(n))