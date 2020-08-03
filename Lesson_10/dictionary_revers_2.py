"""
Дан словарь (смотрите пример ниже) ключами которого являются английские слова, а занчениями - списки латинских слов.
Необходимо развеннуть словарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь,
у которого в качестве ключей будут взяты латинские слова, из исходного словаря, а значениями будет список, соответствующих им, английских слов.

Исходный словарь:

d = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']

}
"""

original_dict = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'pomum'],

   'punishment': ['malum', 'multa']

}

print(original_dict)

reversed_dict = {}

for i in original_dict:
    for j in original_dict[i]:
        if j not in reversed_dict:
            empty_list = []
            reversed_dict[j] = empty_list
        reversed_dict[j].append(i)

print(reversed_dict)
