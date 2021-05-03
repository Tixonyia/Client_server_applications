# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате
# JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
# Для этого:Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
# (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
# должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных
# указать величину отступа в 4 пробельных символа;Проверить работу программы через вызов
# функции write_order_to_json() с передачей в нее значений каждого параметра.
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding='utf-8') as file:
        data = json.loads(file.read())
        data['orders'].append(
            {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

    with open('orders.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, separators=(',', ': '), ensure_ascii=False)
        

write_order_to_json('мыша', '21748', '234323', 'Шапоклякинкорпарейшн', '12.03.2033')

