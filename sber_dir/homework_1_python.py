import csv

# Сколько всего вакансий?  4002
# За какой период эти вакансии?  '2020-10-16, '2021-03-17'
# Есть ли вакансии менеджеров с использованием Python, если да сколько их?  29 или
# Сколько вакансий для аналитика данных? 21
# Сколько вакансий для аналитика данных с использованием Python?  8

destination_file_path = 'целевой_файл.csv'

str_ = 'Python'
str_1 = 'менеджер'
str_2 = 'аналитик'
file = 'vacancy_nh.csv'

data_analyst = []
data_analyst_python = []
date_list = []

c = 0
l = []
with open(file, mode='r', newline='', encoding='utf-8') as csvfile:
    with open(destination_file_path, mode='w', newline='', encoding='utf-8') as destination_file:
        csv_reader = csv.reader(csvfile)
        # пропускаем первую строчку
        next(csv_reader)
    for i, row in enumerate(csv_reader):
        c += 1
        date_list.append(row[6])
        for g in range(len(row)):
            if str_.lower() in row[4].lower() and str_1.lower() in row[5].lower():
                if row not in l:
                    l.append(row)
        for elem in range(len(row)):
            if str_2.lower() in row[4].lower():
                if row not in data_analyst:
                    data_analyst.append(row)
        for item in range(len(row)):
            if str_.lower() in row[4].lower() and str_2.lower() in row[5].lower():
                if row not in data_analyst_python:
                    data_analyst_python.append(row)

date_list.sort()
filtered_sorted_list = [item for item in date_list if item not in ('', None)]

print(f'Сколько всего вакансий?  - {c} всего вакансий')
print(
    f'За какой период эти вакансии? {filtered_sorted_list[0]} - {filtered_sorted_list[len(filtered_sorted_list) - 1]}')
print(f'Есть ли вакансии менеджеров с использованием Python, если да сколько их?  - {len(l)} вакансий')
# # Укажите пути к исходному и целевому файлам
# source_file_path = 'исходный_файл.csv'
print(f'Сколько вакансий для аналитика данных? - {len(data_analyst)} вакансий')
print(f'Сколько вакансий для аналитика данных с использованием Python?  - {len(data_analyst_python)} вакансий')
