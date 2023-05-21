# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056
class PersonInfo:  # Класс PersonInfo которой хранить информацию о сотруднике Имя Фамилия/возраст/подразделение

    def __init__(self, family_name, age, *department):  # Инициализируем занчения
        self.family_name = family_name
        self.age = age
        self.department = [*department]

    def short_name(self):  # Метод возращающий Фамилия И. сотрудника
        return self.family_name[self.family_name.find(' ')+1:] + ' ' + self.family_name[0] + '.'

    def path_deps(self):  # Метод возращающий подразделение сотрудника
        return ' --> '.join(map(str, self.department))

    def new_salary(self):  # Метод расчета индексации для сотрудника
        department_str = ''.join(map(str, self.department))  # Записываем подразделения сотрудника в одну сторку
        # Вычисляем количество повтороенйи для каждой буквы
        list_count_letters = sorted([department_str.count(j) for j in set(department_str)], reverse=True)
        if len(list_count_letters) > 3:
            # если в подразделении больше 3 уникальных букв, то при прасчете индексации сумируем кол-во вхождений
            # трех наиболее часто встречающихся букв
            return 1337 * self.age * sum(list_count_letters[0:3])
        else:
            # если в подразделении меньше 3 уникальных букв, то при расчете индексации сумируем кол-во вхождений
            # всех букв
            return 1337 * self.age * sum(list_count_letters)
# Здесь пишем код

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
