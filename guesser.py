import random


def is_valid_line(num):
    return num.isdigit()


def get_left_num():
    while True:
        print('Левая граница, от которой будет генерироваться число:')
        num = input()
        if not is_valid_line(num) or int(num) <= 0:
            print('Попробуйте ввести целое число больше 0.')
            continue
        return int(num)


def get_right_num():
    while True:
        print('Правая граница:')
        num = input()
        if not is_valid_line(num) or int(num) <= left_num:
            print('Введите целое число, которое больше предыдущего :)')
            continue
        return int(num)


def is_valid(num):
    return num.isdigit() and int(num) in range(left_num, right_num + 1)


print('Добро пожаловать в числовую угадайку!')
print('Эта программа генерирует случайное число в диапазоне, который вы укажите. Вы должны отгадать это число.')
print('Укажите диапазон ниже.')

left_num = get_left_num()
right_num = get_right_num()

number = random.randint(left_num, right_num)

print('Начинайте игру! Предположите какое число загадала программа в диапазоне от', left_num, 'до', right_num, '?')

count_attempts = 0
running = True

while running:
    user_number = input()
    if not is_valid(user_number):
        print('Может быть все-таки введем целое число от', left_num,  'до', right_num, '?')
        continue
    else:
        user_number = int(user_number)
    if user_number < number:
        count_attempts += 1
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif user_number > number:
        count_attempts += 1
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif user_number == number:
        print('Вы угадали, поздравляем!')
        print('Вот столько попыток Вам потребовалось:', count_attempts)
        print('Спасибо, что играли в числовую угадайку. Хотите сыграть еще раз?')
        answer = input().lower()
        if answer in ['да', 'хочу', 'ага', 'давай', 'lf', '[jxe', 'lfdfq', 'fuf', '+']:
            left_num = get_left_num()
            right_num = get_right_num()
            number = random.randint(left_num, right_num)
            count_attempts = 0
            print('Предположите какое число загадала программа в диапазоне от', left_num, 'до', right_num, '?')
        else:
            print('Не хотите играть, ну ладно :(. Приходите еще раз, до скорой встречи!')
            running = False
