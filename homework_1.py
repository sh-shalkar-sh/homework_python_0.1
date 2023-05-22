while True:
    name = input('Ведите ваше имя: ')
    if name.isalpha():
        break
    else:
        print('Вы не правильно ввели Имя! Еще раз попробуйте!')
password = input('Ведите ваш пароль: ')
while True:
    age = input('Введите ваш возраст: ')
    if age.isdigit():
        break
    else:
        print('Вы не правильно ввели возраст! Еще раз попробуйте!')
print (f'Ваши данные для входа в аккаунт: Имя - {name}, пароль - {password}, возраст - {age}')
