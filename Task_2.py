# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

words = [b'class', b'function', b'method']

print('*' * 30)
for i in words:
    print(f'Name variable content: {i}')
    print(f'Type variable: {type(i)}')
    print(f'Line length: {len(i)}')
    print('*' * 30)