list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
maxindex = 0
maximum = list_numbers[0]
for i in range(len(list_numbers)-1):
    if list_numbers[i] > maximum:
        maximum = list_numbers[i]
        maxindex = i
list_numbers[maxindex], list_numbers[len(list_numbers)-1] = list_numbers[len(list_numbers)-1], list_numbers[maxindex]
print(list_numbers)
