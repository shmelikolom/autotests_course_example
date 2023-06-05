# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
with open("test_file/task1_data.txt", mode='r', encoding='utf-8') as task1_data:  # Открытие файла на чтение
    with open("test_file/task1_answer.txt", mode='w', encoding='utf-8') as task1_answer:  # Открытие файла на запись
        trans_table = str.maketrans({f'{j}': None for j in range(10)})  # Создаем таблицу пакетной замены символо
        for line in task1_data:  # Чтение файта построчно
            task1_answer.write(line.translate(trans_table))  # Замена цифр на None и запись новой строки в файл
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
