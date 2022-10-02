import funcs

names='Alexander Александр Mikhail Михаил Maxim Максим Lev Лев Artyom Артём Mark Марк Ivan Иван Dmitry Дмитрий Matvey Матвей Daniil Даниил Sergei Сергей Andrei Андрей Alexey Алексей Maxim Максим Evgeny Евгений'
lst_names=list(names.split())

# выбранный список
lst_choosed=funcs.F(lst_names)
print('Выбрано ', len(lst_choosed), 'элементов')
print(lst_choosed)

# частовстречаемоеи имя
name = funcs.Often(lst_choosed)
print("Чаще всего встречается имя", name)

# имя с наименее встречаемой первой буквой
letter, name = funcs.Rarely(lst_choosed)
print(name)
print("Реже всего имя начинается с буквы", letter[0])

# В файле с логами   https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
# найти дату самого позднего лога (по метке времени)
log='''
2011-08-01 18:03:34,338 - exampleApp - INFO - Program started
2012-09-02 19:13:53,338 - exampleApp - INFO - added 7 and 8 to get15
2012-10-02 20:23:31,338 - exampleApp - INFO - Done!
2013-08-01 01:43:33,338 - exampleApp - INFO - Program started
2011-09-19 12:53:33,338 - exampleApp - INFO - added 10 and 11 to get15
2012-10-12 22:03:33,338 - exampleApp - INFO - Done!
2017-08-01 01:13:51,338 - exampleApp - INFO - Program started
2019-09-19 12:21:34,338 - exampleApp - INFO - added 7 and 8 to get15
2018-10-12 23:31:01,338 - exampleApp - INFO - Done!
'''
lst_log = list(filter(lambda x: len(x)>0,list(log.split('\n')) )) # список непустых строк log
lst_log = list(sorted(lst_log , key=(lambda x: x[:20]) ,reverse=True ))
later_log = lst_log[0]
print('Самая поздняя запись:', later_log)


