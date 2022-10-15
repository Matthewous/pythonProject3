from pprint import pprint
import csv
import re

def file_opener(filepath):

    with open(filepath) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    
    return contacts_list

def name_correction(contacts_list):

    # поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О

    pattern = r"(\w+)\s?(\w+)?\s?(\w+)?"
    substitution_lastname = r"\1"
    substitution_firstname = r"\2"
    substitution_surname = r"\3"

    for line in contacts_list:
        lastname = re.sub(pattern, substitution_lastname, line[0])
        firstname = re.sub(pattern, substitution_firstname, line[0])
        surname = re.sub(pattern, substitution_surname, line[0])

        line[0] = lastname

        if line[1] == "":
            line[1] = firstname
        
        if line[2] == "":
            line[2] = surname

    return contacts_list
    
def phones_correction(contacts_list):

    # привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;

    pattern = r"(\+7|8)?\s*\(?(\d\d\d)\D?\s?(\d\d\d)\D?\s?(\d\d)\D?\s?(\d\d)(\s)?\(?([д][о][б]\.)?[\s]?(\d+)?\)?"
    substitution = r"+7(\2)\3-\4-\5\6\7\8"

    for line in contacts_list:
        result = re.sub(pattern, substitution, line[5])
        line[5] = result
    
    return contacts_list

def undoubling(contacts_list):

    contacts_list_len = len(contacts_list[0])

    fams = {}
    num = 0
    for a in contacts_list:
        fams[num] = a
        num += 1

    new_list = {}

    num = 0
    for a in contacts_list:
        new_list[num] = a[0]
        num += 1

    rev_new_list = {}
    for key, value in new_list.items():
        rev_new_list.setdefault(value, list()).append(key)

    so = []
    for a in rev_new_list.values():
        if len(a) > 1:
            so.append(a)

    doubles = []
    for doubl in so:
        for number in doubl:
            doubles.append(number)

    final_contacts_list = []
    ignore_list = []
    num = len(so)

    for position in fams.items():
        count = 0
        for doubl in so:
            ppppp = position[0]
            count += 1
            if position[0] not in doubl and count == num and position[0] not in ignore_list:
                final_contacts_list.append(position[1])
            elif position[0] in doubl and position[0] not in ignore_list:
                doubl.remove(position[0])
                doubl_pos = doubl[0]
                ignore_list.append(position[0])
                ignore_list.append(doubl_pos)
                united_record = []
                for field in range(0,contacts_list_len):
                    field_num = 0
                    recent_field = position[1][field]
                    if recent_field != '':
                        united_record.append(recent_field)
                    else:
                        united_record.append(fams[doubl_pos][field])
                final_contacts_list.append(united_record)

    return(final_contacts_list)

def file_rewrite(contacts_list):

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

filepath = "/Users/matthew/Desktop/pythonProject3/py-homeworks-advanced/Regular_expressions/phonebook_raw.csv"

if __name__ == '__main__':

    contacts_list = file_opener(filepath)
    name_correction(contacts_list)
    phones_correction(contacts_list)
    final_contacts_list = undoubling(contacts_list)
    file_rewrite(final_contacts_list)