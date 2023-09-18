"""Task 1 - Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні на поточну
дату (курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv"""

import csv

kurs = 40
try:
    with open('test_file.csv', 'r') as file:
        rows = csv.reader(file)
        salaries = [row for row in rows]
        print(salaries)
    with open('salaries_uah.csv', 'w') as file:
        for i in salaries:
            row = []
            new_j = 0
            for j in i:
                if j.isdigit():
                    new_j = int(j) * kurs
                    row.append(new_j)
                else:
                    row.append(j)
            file.writelines(str(row) + '\n')
except Exception as error:
    print(error)
