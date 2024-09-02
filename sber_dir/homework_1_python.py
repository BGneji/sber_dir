import csv
from tqdm import tqdm
import time
# Сколько всего вакансий?
# За какой период эти вакансии?
# Есть ли вакансии менеджеров с использованием Python, если да сколько их?
# Сколько вакансий для аналитика данных?
# Сколько вакансий для аналитика данных с использованием Python?  8


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
print(f'Сколько вакансий для аналитика данных? - {len(data_analyst)} вакансий')
print(f'Сколько вакансий для аналитика данных с использованием Python?  - {len(data_analyst_python)} вакансий')

# Пример цикла с прогресс-баром
for i in tqdm(range(100), desc="Обработка"):
    # Имитация работы
    time.sleep(0.1)  # Задержка для демонстрации прогресс-бара
