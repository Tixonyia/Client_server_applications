# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standard']

words = [i.encode('utf-8') for i in words]

for word in words:
    print(word)
    print(type(word))

words = [bytes.decode(word) for word in words]

for word in words:
    print(word)
    print(type(word))