import csv
from pprint import pprint
import re

filepath = "/Users/matthew/Desktop/pythonProject3/py-homeworks-advanced/Regular_expressions/phonebook_raw.csv"

with open(filepath) as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# pprint(contacts_list)

# print(contacts_list[1])
# def last_name(contacts_list):
#     # pattern = r"^((\w+)\s?(\w+)?\s?(\w+)?\,)"
#     pattern = r"^(\w+)[\s|\,](\w+)[\s|\,](\w+)?(\,\,?\,?)"

#     substitution_lastname = r"\1"
#     substitution_firstname = r"\2"
#     substitution_surname = r"\3"

#     for line in contacts_list:
#         # pprint(line[0])
#         lastname = re.sub(pattern, substitution_lastname, line[0])
#         firstname = re.sub(pattern, substitution_firstname, line[0])
#         surname = re.sub(pattern, substitution_surname, line[0])

#         new = []
#         new.append(lastname)
#         pprint(new)
#     return contacts_list
# last_name(contacts_list)


# ^(\w+)[\s|\,](\w+)[\s|\,](\w+)?(\,\,?\,?)
# pprint(contacts_list)

pattern = r"^(\w+)[\s*|\,](\w+)[\s*|\,](\w+)?(\,\,?\,?)"
substitution = r"\1,\2,\3,"


for line in contacts_list:
    c = str(line[0])
    result = re.sub(pattern, substitution, c)
    pprint(result)
# pprint(contacts_list)

