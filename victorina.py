# переписать программу "Викторина" (из прошлого домашнего задания), используя функции

import random

def test_birthday(date1,date2):
    '''
    ф-я сравнения 2-х дат по совпадению года, месяца или дня. Каждое совпадение дает 1 балл
    :param date1: дата первая
    :param date2:  дата вторая
    :return: количество баллов
    '''

    balls=0
    if len(date1)!=10 or len(date2)!=10:
        return 0

    balls += 1 if date1[6:] == date2[6:] else 0 # совпадает год
    balls += 1 if date1[3:5] == date2[3:5] else 0 # совпадает месяц
    balls += 1 if date1[:2] == date2[:2] else 0 # совпадает день
    return balls

lst_writers=['Пушкиин',    'Лермонтов', 'Гоголь',    'Есенин',    'Толстой',   'Достоевский','Тургенев',
             'Островский', 'Чехов',     'Лесков']
lst_borns = ['06.06.1799', '15.10.1814','01.04.1809','03.10.1895','09.09.1828','11.11.1821', '09.11.1818',
             '12.04.1821', '29.01.1860','16.02.1831']

lst_victory = random.sample(lst_writers,5)

while True:
    print('Угадали год - 1 балл, угадали год/месяц - 2 балла, угадали год/месяц/день - 3 балла')
    score = 0
    for item in lst_victory:
        dr = input(f'Введите ДР писателя {item} в формате ДД.ММ.ГГГГ ')
        score += test_birthday(dr,lst_borns[lst_writers.index(item)])

    print(f'Количество набранных баллов {score} из {len(lst_victory)*3}')

    elseone = input('Сыграем ещё ? (да - символ 1, нет - любой другой символ ')
    if elseone != '1':
        break
