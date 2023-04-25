while True:
    income = input('Введите выручку фирмы:')
    if income.isdigit():
        break
    else:
        print('Введите только цифры!')

while True:
    cost = input('Введите издержки фирмы:')
    if cost.isdigit():
        break
    else:
        print('Введите только цифры!')

while True:
    staff = input('Введите численность сотрудников фирмы: ')
    if staff.isdigit():
        break
    else:
        print('Введите только цифры!')

print(f'Финансовы! результат - прибыль. Ее величина: {int(income) - int(cost)}',
      f'Рентабельность выручки = {(int(income) - int(cost)) / int(income)}',
      f'Прибыль фирмы в расчете на одного сотрудника = {(int(income) - int(cost)) / int(staff)}', sep='\n')


