while True:
    tiket = input("Введите номер билета: ")
    if tiket.isdigit() and len(tiket) == 6:
        if int(tiket[0]) + int(tiket[1]) + int(tiket[2]) == int(tiket[3]) + int(tiket[4]) + int(tiket[5]):
            print('Поздравляю, у вас счасливый билет!')
        else:
            print('У вас обычный билет, не расстраивайтесь!')
        break
    else:
        print('Введен неправельный номер билета, попробуйте еще раз!')