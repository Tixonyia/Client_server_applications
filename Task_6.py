# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

strings = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    [file.write(i + '\n') for i in strings]

print(f'Coding file: {file.encoding}')

with open('test_file.txt', 'r', encoding='utf-8') as file:
    for item in file:
        print(item)
