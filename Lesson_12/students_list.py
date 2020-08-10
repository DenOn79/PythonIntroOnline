"""
1. В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.

 Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести
средний балл по классу. Так же,
 записать в новый файл всех учащихся в формате "Фамилия И. Ср. балл":

 Выравнивание колонок - желательно!
"""
from pprint import pprint as pp

lst = []
print()
file = open('students.txt', encoding='utf-8')
for line in file:
    lst.append(line.strip('\n'))
pp(lst)
print()
average_value = int(input('Введите минимальный средний балл: '))
file.close()
lst_item = []
total_average = 0
file_2 = open('students_average.txt', 'w', encoding='utf-8')
print('Следующие ученики имеют средний балл ниже введенного: \n')
for i in range(len(lst)):
    lst_item = lst[i].split()
    sum_items = 0
    number_of_items = 0
    for j in range(2, len(lst_item)):
        sum_items += int(lst_item[j])
        number_of_items += 1
    average = round((sum_items/number_of_items), 1)
    if average < average_value:
        print('{} {} --- {:>}'.format(lst_item[0], lst_item[1], average))
        print()
    total_average += average
    get_spaces = 25 - (len(list(lst_item[0]))+len(list(lst_item[1]))+1)
    line = ('{} {} {} {}'.format(lst_item[0], lst_item[1], str('-'*get_spaces), str(average)))
    file_2.write(line)
    file_2.write('\n')
file_2.close()
print('Средний балл по классу: ', round(total_average/len(lst), 1))
