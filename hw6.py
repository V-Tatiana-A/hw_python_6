# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print("Задача 30")
a, d, n = map(int, input("Введите первый элемент, разность и количество элементов через пробел: ").split())
list=[]
for i in range(a, (a+n*d),d):
    list.append(i)
print(*list, sep='\n')



# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

print("\nЗадача 32")
number=int(input("Введите размер списка:  "))
array=[]
for i in range(number):
    array.append(random.randint(-20,20))
    i+=1
print(array)
x,y = map(int, input("Введите мин. и макс. диапазона через пробел: ").split())

def get_index(arr, min, max):
    result=[]
    for j in range(len(arr)):
        if arr[j]>=min and arr[j]<=max:
            result.append(j)
    return result

print(f'Индексы элементов массива, удовлетворяющих условию : {get_index(array,x,y)}')


