# Необходимые и достаточные условия

# 1. Реализовать приведение строк "разработка", "сокет", "декоратор" к типу bytes используя нативные методы строк;
# 2. Реализовать приведение полученных экземпляров типа bytes к типу str;
# 3. Реализовать приведение полученных строк и байтовых последовательностей
# с использование различных кодировок utf-8 latin-1.

# -------------------------------------------------- Реализация -------------------------------------------------------

# 1

word_1 = 'разработка'.encode()
word_2 = 'сокет'.encode()
word_3 = 'декоратор'.encode()

print(word_1, word_2, word_3, sep='\n')
print()

# 2

word_1_str = word_1.decode()
word_2_str = word_2.decode()
word_3_str = word_3.decode()

print(word_1_str, word_2_str, word_3_str, sep='\n')
print()

# 3

word_1_str_latin = word_1.decode('latin-1')
word_2_str_latin = word_2.decode('latin-1')
word_3_str_latin = word_3.decode('latin-1')
print(word_1_str_latin, word_2_str_latin, word_3_str_latin, sep='\n')

# Кодирование строк с кириллицей с использованием кодировки latin-1 выдает ошибку:
# UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-9: ordinal not in range(256)
# Декодирование с использованием latin-1 искажает изначально введенное слово, поскольку в кодировке latin-1
# вместо кириллицы (как в utf-8) на местах стоят другие символы.
