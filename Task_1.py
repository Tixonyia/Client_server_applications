# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить
# тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
# преобразовать строковые представление в формат Unicode и также проверить тип и содержимое
# переменных.

development = 'разработка'
socket = 'сокет'
decorator = 'декоратор'
words = [development, socket, decorator]
print('*' * 30)
for i in words:
    print(f'Name variable content: {i}')
    print(f'Type variable: {type(i)}')
    print('*' * 30)

words = [i.encode('utf-8') for i in words]

for i in words:
    print(f'Name variable content: {i}')
    print(f'Type variable: {type(i)}')
    print('*' * 30)


