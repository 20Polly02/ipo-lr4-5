numbers = list(map(int, input("Введите список чисел ").split()))
x = 0 
max = numbers[x] 
while x < len(numbers): 
     if numbers[x] > max:
      max = numbers[x] 
     x += 1

print ("Максимальное число из списка",max)