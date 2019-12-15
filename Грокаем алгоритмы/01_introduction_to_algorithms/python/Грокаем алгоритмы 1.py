# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:48:54 2019

@author: Николай
"""

# пример алгоритма бинарного поиска. То есть простая игра "Угадай число"
import random as rd
num = rd.randrange(1,101)
while True:
    answer = input('Введите целое число от 1 до 100: ')
    if not answer.isdigit():
        print('Введите целое число')
        continue
    answer = int(answer)
    if answer > num:
        print('Введи число меньше')
    elif answer < num:
        print('Введи число больше')
    else:
        print('Правильно!')
        break

