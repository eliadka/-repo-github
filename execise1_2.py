second1 = int(input('Введите секунды: '))
hour = (second1 // 3600)
minute1 = second1 % 3600
minute2 = minute1 // 60
second2 = minute1 % 60
print(f"Now is {hour}:{minute2}:{second2} ")
