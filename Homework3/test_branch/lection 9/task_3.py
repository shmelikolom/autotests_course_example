# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
list_purchases = []
purchases = 0
with open("test_file/task_3.txt", 'r', encoding='utf-8') as task_3:
    for i in task_3:
        try:
            purchases += int(i)
        except ValueError:
            list_purchases.append(purchases)
            purchases = 0
list_purchases.sort()
three_most_expensive_purchases = sum(list_purchases[-3:])
assert three_most_expensive_purchases == 202346
