'''Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

s = input('Введите элемента списка через пробел: ') #Приглашение ко вводу
numbers = list(map(float, s.split()))               #Формирование множества

numbers2 = []

for i in range(0,len(numbers)):                     #Нахождение дробной части в списке
     if (numbers[i] - int(numbers[i])) != 0:
         numbers2.append(numbers[i] - int(numbers[i]))

print(numbers2)
print(max(numbers2))
print(min(numbers2))

raznost = (round(max(numbers2),2) - round(min(numbers2),2))  #Нахождение разницы между максимальным и минимальным значением дробной части
print('Разница между максимальным и минимальным значением дробной части элементов равна ', raznost)