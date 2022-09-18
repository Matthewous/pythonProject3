from pprint import pprint
import csv
import re

filepath = "/Users/matthew/Desktop/pythonProject3/py-homeworks-advanced/Regular_expressions/phonebook_raw.csv"

with open(filepath) as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О


# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
pattern = r"(\+7|8)?\s*\(?(\d\d\d)\D?\s?(\d\d\d)\D?\s?(\d\d)\D?\s?(\d\d)(\s)?\(?([д][о][б]\.)?[\s]?(\d+)?\)?"
substitution = r"+7(\2)\3-\4-\5\6\7\8"

for line in contacts_list:
    counter = 1
    for object in line:
        if counter == 6:
            result = re.sub(pattern, substitution, object)
            line[counter-1] = result
            break
        else: counter += 1
    # pprint(line)
# pprint(contacts_list)


# TODO объединить все дублирующиеся записи о человеке в одну.


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)