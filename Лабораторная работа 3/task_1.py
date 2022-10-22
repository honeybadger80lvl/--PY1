list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
unique_sum = sum(set(list_))
unique_len = len(set(list_))
unique_all = unique_sum / unique_len

print(unique_sum)
print(unique_len)
print(round(unique_all, 5))


