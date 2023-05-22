while True:
    number = input("Введите трехзначное число: ")
    if number.isdigit():
        break
    else:
        print('Введите толко цифры!')
sum_of_digits = int(number[0]) + int(number[1]) + int(number[2])
print(f'Сумма цифр числа {number}, равна {sum_of_digits}')