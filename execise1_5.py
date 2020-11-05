proceed = int(input("Enter proceed: "))
outlay = int(input("Enter outlay: "))
if proceed > outlay:
    print('выручка больше издержек')
    profit = proceed - outlay
    print(f'рентабельность выручки {profit}')
    people = int(input('численность сотрудников фирмы: '))
    proceed = profit / people
    print(f'прибыль фирмы в расчете на одного сотрудника {proceed}')
else:
    print('издержки больше выручки')
