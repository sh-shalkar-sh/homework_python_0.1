while True:
    n = input('Введите целое положительное число n: ')
    if n.isdigit():
        break
    else:
        print('Введите только цифры!')
nn = n + n
nnn = n + n + n
summa = int(n) + int(nn) + int(nnn)
print(f'n + nn + nnn = {summa}')