
lst_1 = [34587, 'Learning Python, Mark Lutz', 4, 40.95]
lst_2 = [98762, 'Programming Python, Mark Lutz', 5, 56.80]
lst_3 = [77226, 'Head First Python, Paul Barry', 3, 32.95]
lst_4 = [88112, 'Einfuhrung in Python3, Bernard Klein', 3, 24.99]
total_lst = [lst_1, lst_2, lst_3, lst_4]
print(total_lst)

func = lambda lst: (lst[0], round(lst[2]*(lst[3]+10), 2)) if (lst[2]*lst[3]) < 100 else (lst[0], round(lst[2]*(lst[3]), 2))
res = map(func, total_lst)
print(list(res))
