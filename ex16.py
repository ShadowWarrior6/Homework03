# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

X=abs(int(input('Введите количество элементов списка А: ')))
Entering=input("Введите через пробел элементы списка: ").split()
Number=list(map(int, Entering))
if len(Number) != X:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    N=int(input('Введите число X, которое необходимо найти в списке: '))
    Count=0
    for i in range(X):
        if Number[i]==N:
            Count+=1
            print(f'Число {N} встречается в списке A {Count} раз') 