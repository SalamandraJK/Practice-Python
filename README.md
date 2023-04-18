# Practice-Python
* Для запуска компиляции нужно написать:

         python "имя файла.py"
* Для комментирования поставить перед тесктом #
  
  для комментирования нескольких строк поставить """ перед первой 
  и """ после последней, комментируемой строкой

        """

        ffffffffff
        ffffffffff
        ffffffffff
        
        """
* Выделить неоходимую часть строк и нажать
  
        ctrl + k   и   ctrl + c

* Для того что бы убрать коммит 
  
        ctrl + k    и   ctrl + u

* Ввод данных осуществляется через функцию  

        input()

* Объявление переменной

        a = 12

        b = 1.23

* Присвоение значения "строки" перменной

        str1 = "good"

        str2 = 'bad'

* Фунция вывода

         print( )

* Функция для определения типа данных у переменной

        type

        print(type(n))

Для вывода нескольких переменных, разделенных символами или знаками используем запись:

    print(f"{a} - {b} - {c}")

* Пример ввода данных

        print('Введите первое значение: ')
    
        a = input()
    
        print("Полученный результат: ", a)

    
        b = input('Введите второе число: ')
    
        c = ("Полученный результат: ")
    
        print(c, b)

* Арифметические операции и  их обозначения

        +       Словежние
        -       Вычитание
        *       Умножение
        /       Деление(в вещественных числах, по умолчанию)
        %       Остаток от деления
        //      Целочисленное деление
        **      Возведение в степень

* Примеры операций с одной переменной

        N = 2     (N присваивается значение 2)
        N += 2    (N = N + 2)
        N -= 2    (N = N - 2)
        N *= 2    (N = N * 2)
        N /= 2    (N = N / 2)
        N //= 2   (N = N // 2)
        N **= 2   (N = N**2)
        N %= 2    (N = N % 2)

* Для того, что бы ограничить колличество знаком после "запятой"
при выполнении арифметической операции нужно написать функцию

                round(число, кол-во символов)
                
                
                round(2.3343533, 4)


                результат: 2.3343

* Логические операции

        >         Больше
        >=        Больше или равно
        <         Меньше
        <=        Меньше или равно
        ==        Проверка равенства
        !=        Проверка неравенства
        not       НЕ (отрицание)
        and       И (конъюнкция)
        or        ИЛИ (дизъюнкция)

* Управляющие конструкции __if, if-else__


        if условие

                действие для проверки
        
        else иначе
        
                действие

* Цикл __While__

        while условие
                действие 1
                действие 2
                ...
                действие n

* Управляющие конструкции __while - else__

Конструкция работает, когда основное тело цикла перестает работать самостоятельно.

                while условие
                        действие 1
                        действие 2
                        ...
                        действие n
                else:
                        действие n + 1
                        действие n + 2
                        ...
                        действие n + m

* Функция __range()__ - генирирует некую последовательность

        range(начало последовательности, конец последовательности, шаг последовательности)


        r = range(5)                    Результат: 0 1 2 3 4
        r = range(2, 5)                 Результат: 2 3 4
        r = range(0, -5)                Результат: ----
        r = range(1, 10, 2)             Результат: 1 3 5 7 9
        r = range(100, 0, -20)          Результат: 100 80 60 40 20
        
        r = range(100, 0, -20)
        for i in r:
        print(i)
        результат: 100 80 60 40 20

* Пример работы с индексами в тексте

text = 'съешь ещё этих мягких французских булок'

Длина строки = 39

        print(text[0])                    Выводим символ с индексом 0 - "c"
        print(text[1])                    Выводим символ с индексом 1 - "ъ"
        print(text[len(text)-1])          Выводим символ с индексом (длинна строки -1) - "к"
        print(text[:])                    Выводм все символы         
        print(text[:2])                   Выводим символ с индексом 0 и 1 - "cъ"
        print(text[len(text)-2:])         Выводим символ с индексом 39 и 38 - "ок"
        print(text[20:])                  Выводим символ с индексами от 20 до 39 - "х французских булок"
        print(text[:20])                  Выводим символ с индексами от 0 до 20 - "съешь ещё этих мягких"
        print(text[2:9])                  Выводим символ с индексами от 2 до 9 - "ешь ещё"
        print(text[6: -18])               Выводим символ с индексом 0 - "ещё этих мягких  "
        print(text[0:len(text):6])        Выводим символы от 0 до конца с шагом(6) - "сеикакл"
        print(text[::6])                  Выводим символы от 0 до конца с шагом(6) - "сеикакл"
        
        text = text[2:9] + text[-5] + text[:2]

        print(text)                    Выводим "ешь ещёбсъ"

* Списки

        list_1 = []             Создание пустого списка
        list_2 = list()         Создание пустого списка
        list_1 = [7, 9, 11, 13, 15, 17]

        Для вывода __первого__ элемента из списка искользуем конструкцию:
                list_1 = [7, 9, 11, 13, 15, 17]
                print(list_1[0])
                Вывод: [7]
        Для того, что бы убрать квадратные скобки нужно добавить в запись символ *
                print(*list_1[0])
                Вывод: 7

                for i in list_1:        # Вывод всех элементо  списка
                print (i)

                print(len(list_1))      # Длинна списка

                При записи : print(list_1[-2]) нумерация пойдет с конца списка
                Вывод: 15

* Функции списков

        .append()               Добавление элемента в список 
                list_1 = [7, 9, 11, 13, 15, 17]
                list_1.append(77)
                print(list_1)
                [7, 9, 11, 13, 15, 17, 77]

        list_1 = []
        for i in range(5):                      Дополняем список значениями поочередно
                list_1.append(i)
                print(list_1)

        Вывод:  [0]   
                [0, 1]
                [0, 1, 2]
                [0, 1, 2, 3]
                [0, 1, 2, 3, 4]

        .pop("Значение индекса // или пустые скобки для удаления последнего элемента")
        Удаление последнего элемента в списке

        Запись: list_1.pop      print(list_1.pop())
        
        a = list_1.pop

        .insert(значение индекса, элемент)       Добавление элемента на определенную позицию в списке

Пример:
        list_1 = [7, 9, 11, 13, 15, 17]

        print(list_1[:])                [7, 9, 11, 13, 15, 17]
        print(list_1[:2])               [7, 9]
        print(list_1[len(list_1)-2:])   [15, 17]    
        print(list_1[2:4])              [9, 11]


* Кортеж - неизменяемый список
        t = ()          создание пустого кортежа

* Словарь
        d = {}          Создание пустого словаря
        d = dict()

        d['q'] = 'qwerty'
        print(d)
        Вывод: {'q': 'qwerty'}

        Для вывода элемента по ключу:
        print(d['q'])
        q

        del - функция удаления элемента

        diction = {'ffff' : 'f', 'l' : '3', 'r' : '4'}
        del diction['ffff']

        print(item) - вывод только ключей 
        ffff
        l
        r

        diction = {'ffff' : 'f', 'l' : '3', 'r' : '4'}
                for item in diction:
                print('{} : {}'.format(item, diction[item]))
        ffff : f
        l : 3
        r : 4

* Моножества - содаржаю УНИКАЛЬНЫЕ значения

colors = {'red', 'green', 'blue'}