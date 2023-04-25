while True:
    S = input("Введите общее количество журавликов: ")
    if S.isdigit():
        break
    else:
        print('Введите толко цифры!')

if not int(S) % 6:
     x = int(S) // 6
     print(f'Катя {x * 4}, Сережа {x}, Петя {x}', sep='\n')
