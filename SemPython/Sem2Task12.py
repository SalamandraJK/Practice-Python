import random
first_num = 0
second_num = 0
j = 0
X = random.randint(1, 100)
print(X, end=" ")
Y = random.randint(1, 100)
print(Y, end=" ")

for first_num in range(X):
    for second_num in range(Y):
        if X == first_num + second_num and Y == first_num * second_num:
            print(first_num, second_num)
        