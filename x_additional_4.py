n = int(input("Введите n размер шоколадки: "))
m = int(input("Введите m размер шоколадки: "))

k = int(input("Введите k долек, которое хотите отломить: "))

if k < m * n and k % m == 0 or k % n == 0:
    print('Да')
else:
    print('Нет')