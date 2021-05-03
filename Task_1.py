# -*- coding: utf-8 -*-
# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
# определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
# «отчетный» файл в формате CSV.
import csv
import re


def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file_name in files:
        with open(f'{file_name}') as file:
            os_prod_list = []
            os_name_list = []
            os_code_list = []
            os_type_list = []
            result = []
            for line in file:
                for item in line.split(':'):
                    if item == 'Изготовитель ОС':
                        os_prod_list += (re.findall(r'\s+([^:\n]+)\s*$', line))
                    elif item == 'Название ОС':
                        os_name_list += (re.findall(r'\s+([^:\n]+)\s*$', line))
                    elif item == 'Код продукта':
                        os_code_list += (re.findall(r'\s+([^:\n]+)\s*$', line))
                    elif item == 'Тип системы':
                        os_type_list += (re.findall(r'\s+([^:\n]+)\s*$', line))
            result += os_prod_list
            result += os_name_list
            result += os_code_list
            result += os_type_list
            main_data.append(result)
    return main_data


def write_to_csv(file_csv):
    data = get_data()
    with open(file_csv, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            writer.writerow(row)


write_to_csv('file_csv')
