numbers = list(map(int, input("Введите список чисел ").split()))#Введение списка чисел с клавиатуры
x = 0#число для обозначения индекса
max = numbers[x]#обозначение максимального числа из списка
while x < len(numbers): #Цикл while для проверки чисел из списка на максимальное из них
     if numbers[x] > max:#Оператор if  для проверки условия
      max = numbers[x]#если условие истинно, то выполняется смена переменной
     x += 1 #увеличение значения на 1

print ("Максимальное число из списка",max)# вывод максимального числа из введенного списка
