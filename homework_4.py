income = input('Введите выручку фирмы:')
cost = input('Введите издержки фирмы:')
staff = input('Введите численность сотрудников фирмы: ')
print(f'Финансовый результат - прибыль. Ее величина: {int(income) - int(cost)}',
      f'Рентабельность выручки = {(int(income) - int(cost)) / int(income)}',
      f'Прибыль фирмы в расчете на одного сотрудника = {(int(income) - int(cost)) / int(staff)}', sep='\n')


