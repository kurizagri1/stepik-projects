import random

from hangman_data import word_rus, stages


def get_word():
    random_word = random.choice(word_rus).upper
    return random_word()


def display_hangman(tries):
    return stages[tries]


def not_fool(char):
    if not char.isalpha():
        print('Кажется, Вы написали что-то не то. Напишите букву или слово полностью:')


def play(word):
    word_completion = ['_'] * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов! У Вас есть 6 попыток :)')
    print(display_hangman(tries))

    while True:
        print(*word_completion, sep='')
        user_char = input('Предположите какая буква есть в загаданном слове или напишите это слово полностью:').upper()
        if len(user_char) == 1:
            if user_char in guessed_letters:
                print('Эту букву Вы уже писали. Попробуйте другую :)')
                continue
            else:
                guessed_letters += user_char
        if len(user_char) > 1:
            if user_char in guessed_words:
                print('Это слово Вы уже писали.  Попробуйте другое :)')
            else:
                guessed_words += user_char
        if user_char in word:
            for i in range(len(word)):
                if word[i] == user_char:
                    word_completion[i] = user_char
        if user_char not in word:
            tries -= 1
            print('Не подходит! У вас осталось попыток:', tries)
            print(display_hangman(tries))
        if all([c.isalpha() for c in word_completion]):
            print('Поздравляем, вы угадали слово! Вы победили!')
            break
        if tries == 0:
            print('К сожалению, Вы проиграли. Загаданное слово было:', word)
            break


tries = 6
word = get_word()

play(word)
