from pprint import pprint

import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)


pattern = "(\+7|8)?\s*\(?(\d\d\d)\D?\s?(\d\d\d)\D?\s?(\d\d)\D?\s?(\d\d)(\s)?\(?([д][о][б]\.)?[\s]?(\d+)?"
substitution = r"+7(\2)\3-\4-\5\6\7\8"
result = re.sub(pattern, substitution, text)