# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

# Здесь пишем код
class RomanNums:
    """Класс для работы с римскими числами

       Атрибуты
       --------
       arabic_roman_dict : dict
           Словарь соответсвия римских цифр и арабских чисел
       roman_num : str
           Римское число
       """
    arabic_roman_dict = {1000: 'M',  # Задаем словарь римских цифр
                         900: 'CM',
                         500: 'D',
                         400: 'CD',
                         100: 'C',
                         90: 'XC',
                         50: 'L',
                         40: 'XL',
                         10: 'X',
                         9: 'IX',
                         5: 'V',
                         4: 'IV',
                         1: 'I'}

    def __init__(self, roman_num: str) -> None:
        """Устанавливает все необходимые атрибуты для объекта RomanNums

        Параметры
        ---------
        roman_num: str
            Римское число
        """
        self.roman_num = roman_num

    def from_roman(self) -> int:
        """Переводит римскую запись числа в арабскую и возвращает его."""
        arabic_num = 0
        j = 0
        for arabic, roman in self.arabic_roman_dict.items():
            while j < len(self.roman_num):
                if self.roman_num[j] == roman:
                    arabic_num += arabic
                    j += 1
                elif self.roman_num[j:j+2] == roman:
                    arabic_num += arabic
                    j += 2
                else:
                    break
        return arabic_num

    def is_palindrome(self) -> bool:
        """Определяет, является ли арабское число палиндромом.
           Возвращает True - если число является палиндромом, иначе False"""
        list_arabic_num = list(map(int, str(self.from_roman())))
        for j in range(len(list_arabic_num)//2):
            if list_arabic_num[j] == list_arabic_num[-j - 1]:
                continue
            else:
                return False
        return True

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]


test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
