# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
list_purchases = []
purchases = 0
with open("test_file/task_3.txt", 'r', encoding='utf-8') as task_3:  # Открытие файла на чтение
    for line in task_3:
        if line != '\n':  # Провека на разделитель покупок
            purchases += int(line)  # Увеличиваем сумму покупки на цену
        else:
            list_purchases.append(purchases)  # Записываем окончательную сумму в список
            purchases = 0
list_purchases.sort()  # Сортировка списка по возростанию
three_most_expensive_purchases = sum(list_purchases[-3:])  # Суммируем три последнии занчниея списка
assert three_most_expensive_purchases == 202346
