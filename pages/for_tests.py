import random
import re


# Русские буквы
def russian_chars():
    """ Русский алфавит"""
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Китайские символы
def chinese_chars():
    """ Китйские символы"""
    return '的一是不了人我在有他这为之大来以个中上们'


# Спецсимволы
def special_chars():
    """ Набор спецсимволов"""
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


# генератор буквенной строки различной длины
def generate_string(num):
    """ Герератор буквенной строки различной длины"""
    a = 'фхцчabcабвгдежdefghijkзиклмнlmnopqrsопрстуtuvw'
    char_list = []
    for i in range(num):
        char_list.append(random.choice(a))
    return ''.join(map(str, char_list))


# генератор буквенно-цифровой строки различной длины
def generate_string_num(num):
    """ Герератор буквенно-цифровой строки различной длины"""
    a = '678фхцч90abcабвгдежdefghijkзиклмнlmnopqrsопрстуtuvw12345'
    char_list = []
    for i in range(num):
        char_list.append(random.choice(a))
    return ''.join(map(str, char_list))


# Японские символы
def japan_chars():
    """ Японские символы"""
    return '自動車教科書天然色'


# Цифры
def digit_in_char(num, s=""):
    """ Функция генерит номер телефона с указанным колличесвом цифр и указанной, при необходимости первой цифрой"""
    number = [1, 2, 4, 5, 6, 9, 0]
    number_list = []
    if s != "":
        number_list = [int(s)]
    if s == "":
        number_list.append(random.randint(0, len(number) - 1))
    for i in range(num):
        number_list.append(random.randint(0, 9))
    return ''.join(map(str, number_list))


def eng_string(num):
    """ Герератор строки различной длины c английскими буквами"""
    a = 'abcdefjhijklmnopqrstuvwxyz'
    char_list = []
    for i in range(num):
        char_list.append(random.choice(a))
    return ''.join(map(str, char_list))


