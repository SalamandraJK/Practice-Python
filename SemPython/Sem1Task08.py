# Задача №8. 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите кол-во долек N: "))
m = int(input("Введите кол-во долек M: "))
k = int(input("Введите кол-во долек K: "))

print(f"Общее количетсво долек = {n*m}")

if k == (n * m) / 2:
    print(f"Можно отломить {k} долек")
else:
    print(f"Нельзя отломить {k} долек")
