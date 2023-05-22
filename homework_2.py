while True:
    secund = input('Ведите секунды:')
    if secund.isdigit():
        break
    else:
        print('Введите только цифры!')
hour = int(secund) / 3600
minute = int(secund) / 60
print(f'ч:м:с = {hour}:{minute}:{secund}')