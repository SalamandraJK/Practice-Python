# print(5) # Функция вывода(печати)
# print(5, 5, 7, 2)

# a = 2333 # Присвоение значения переменной
# print(a)

# str1 = 'Football'
# print(str1)

# # Функция для определения типа данных у переменной "type"

# n = 2
# print(type(n))
# n1 = 'hi, my lord'
# print(type(n1))

# # Печать нескольких переменных с разделителями

# a = 1
# b = 2.34
# c = "given"

# print(f"{a} - {b} - {c}")
# print(f"{a} , {b} , {c}")
# print("{} - {} - {}".format(a, b, c))

# # Пример ввода данных

# print('Введите первое значение: ')
# a = input()
# print("Полученный результат: ", a)

# b = input('Введите второе число: ')
# c = ("Полученный результат: ")
# print(c, b)

# # Сумма нескольких чисел

# print(a,'+',b,'+','=', a + b) # Вданном случае не происходит сложение чисел, а сложение строк

# c = 5.55

# print(c)
# print(type(c))

# j = int(c) # Приведение переменной к целочисленному значению

# print(j)
# print(type(j))

# j = str(c) # Приведение переменной к значению строки

# print(j)
# print(type(j))


# j = bool(c) # Приведение переменной к значению высказывания

# print(j)
# print(type(j))

# # Проба сложения с тим переменных int
# print('Введите первое значение: ')
# a = int(input())
# print("Полученный результат: ", a)
# b = int(input('Введите второе число: '))
# print('Результат сложения: ',a,'+',b,'=', a + b)


# # Арифметические операции

# a = 5.2345455
# b = 3.4543333111
# print(round(a*b, 4)) # Функция для ограничения символов после запятой


# #  Пример управляющей конструкции

# username = input('Введите имя пользователя: ')
# if username == 'Маша':
#     print('Наконец-то, Мария, вы вернулись')
# elif username == 'Федор':
#     print('Нус, здравствуйте, Федор')
# else:
#     print('Привет, ',username)

# # Пример работы программы с методом Флажка

# n = int(input('Введите число: '))
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2: # Услове: Делитель(i) не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# a = 'groowy'

# for i in a:
#     print(i)


# line = ""
# for i in range(5):
#     line =""
#     for j in range(5):
#         line += "*"
#     print(line)

# Пример работы со строками и текстом

# text = 'OOOPS! Yes, I did iT agaIn'
# print(len(text)) # Функция len, позволяет узнать длинну строки
# print('Yes'in text) # Проверка на наличии строки в тексте
# print(text.lower()) # Перевод всех символом в нижний регистр
# print(text.upper()) # Перевод всех символом в верхний регистр
# print(text.replace('Yes', 'YES')) # Позволяет поменять сочетание символов в нашей строке


# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # Функция len, позволяет узнать длинну строки
# print(text[:20])
# print(text[0:len(text):6])  

# text = text[2:9] + text[-5] + text[:2]
# print(text)


# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1[0])

# for i in list_1:        # Вывод всех элементо  списка
#     print (i)

# print(len(list_1))      # Длинна списка

# list_1 = [7, 9, 11, 13, 15, 17]
# list_1.append(77)
# print(list_1)

# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# t = ()
# print(type(t))

# t = (1, 2, 3,)
# print(type(t))

# v = [1, 3, 5]
# print(v)
# print(type(v))

# v = type(v)
# print(v)
# print(type(v))


# a,b,c = v

# print(a, b, c)


# t = (1, 2, 3, 4, 5,)

# print(t[1])

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])


# c = [1, 2, 3, 4, 5,]

# c[0] = 2

# print(c)
# d = {}
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d)

# print(d['q'])

# diction = {'ffff' : 'f', 'l' : '3', 'r' : '4'}
# for item in diction:
#     print('{} : {}'.format(item, diction[item]))

# print(diction.items())


# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('darck')
# print(colors)
# colors.remove('darck')
# print(colors)
# colors.discard('darck')
# print(colors)
# colors.clear()
# print(colors)

# q = set()

# a = {1, 2, 3, 5, 7}
# b = {2, 5, 6, 8, 12, 13}
# c = a.copy()    #Копировать значения
# print(c)
# u = a.union(b)  #Будет содержать уникальные значения обоих множеств
# print(u)
# i = a.intersection(b)   # Будет содержать общие элементы из двух списков
# print(i)
# dl = a.difference(b)    # Будет содержать элементы вычтенные множеством А от множества В
# print(dl)
# dr = b.difference(a)    # Будет содержать элементы вычтенные множеством В от множества А
# print(dr)
# q = a.union(b).difference(a.intersection(b))    #    
# print(q)


#                                   Функции

# Сумма чисел от 1 до N

# def sum_numbers(n, ):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# a = sum_numbers(5)
# print(a)

# def sum_numbers(n, y = 'Helloy' ):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# a = sum_numbers(5)
# print(a)

# # Функция для приема неограниченных параметров
# def sum_str(*args):
#     res = str('')
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r', 't'))
# # str(sum_str)
# # print(sum_str(str(8, 9, 1)))


# Модуль - файл с функциями

# import modul    # Пример импортирования модуля с функцией
# print(modul.max1(5,9))


# from modul import max1  # Пример инпорта именно функции из модуля
# print(max1(10,7))

# import modul as m   # Пример сокращения именни модуля при вызове
# print(m.max1(4,8))


# Рекурсия: Вывод нескольких чисел Фибонначи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Алгоритм. Сортировка

# # Пример быстрой сортировки
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     great = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(great)

# print(quick_sort([14,5,67,9,34,5,7,8,9,]))
# print(quick_sort([10, 7, 3, 5]))

# # Пример сортировки слиянием

# def merge_sort(nums):
#     if len(nums) > 1:           # Деление списка на двое, пока не останется ниодного элемента
#         mid = len(nums) // 2    #
#         left = nums[:mid]       #
#         right = nums[mid:]      #
#         merge_sort(left)        #
#         merge_sort(right)       #
#         i = j = k = 0           
#         while i < len(left) and j < len(right):     # Сравниваем значения
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):            # Записываем значения
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list_1 = [1,3,5,6,2,3,5,7,9,23,89,5]
# merge_sort(list_1)
# print(list_1)