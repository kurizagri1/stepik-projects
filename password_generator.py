import random


def conditional_append(password, chars, subset, condition):
    if condition:
        password.append(random.choice(subset))
        chars += subset


def generate_password(len_of_password, use_numbers, use_upper, use_lower, use_symbols, not_use_ambiguous):
    password = []
    chars = []

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'

    for subset, condition in zip([digits, uppercase_letter, lowercase_letters, punctuation],
                                 [use_numbers, use_upper, use_lower, use_symbols]):
        conditional_append(password, chars, subset, condition)

    chars = "".join(chars)
    while len(password) < len_of_password:
        random_char = random.choice(chars)
        if not (not_use_ambiguous and random_char not in 'il1Lo0O'):
            password.append(random_char)
    random.shuffle(password)
    return ''.join(password)


print('Сколько будем генерировать паролей? Введите число:')
count_of_passwords = int(input())
print('Какой длины должны быть пароли? Введите число больше 5:')
len_of_password = int(input())
print('Включать ли цифры 0123456789?')
use_numbers = input() in ['да', 'lf']
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
use_upper = input() in ['да', 'lf']
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
use_lower = input() in ['да', 'lf']
print('Включать ли символы !#$%&*+-=?@^_?')
use_symbols = input() in ['да', 'lf']
print('Исключать ли неоднозначные символы il1Lo0O?')
not_use_ambiguous = input() in ['да', 'lf']

for _ in range(count_of_passwords):
    print(generate_password(len_of_password, use_numbers, use_upper, use_lower, use_symbols, not_use_ambiguous))
