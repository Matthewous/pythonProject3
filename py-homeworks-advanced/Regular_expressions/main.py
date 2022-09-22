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


filepath = "/Users/matthew/Desktop/pythonProject3/py-homeworks-advanced/Regular_expressions/phonebook_raw.csv"


if __name__ == '__main__':

    contacts_list = file_opener(filepath)
    name_correction(contacts_list)
    phones_correction(contacts_list)

    print(contacts_list)

# TODO объединить все дублирующиеся записи о человеке в одну.

new_list = []
compared = []

num = 0
num_compare = 0
for line in contacts_list:
    if line[0] not in compared:
        lastname = line[0]
        firstname = line[1]
        num += 1
        # print(lastname)
        for line_compare in contacts_list:
            num_compare += 1
            lastname_compare = line_compare[0]
            firstname_compare = line_compare[1]
            if num != num_compare and lastname == lastname_compare and firstname == firstname_compare:
                new_list_line = {}
                
                new_list_line[0] = lastname
                new_list_line[1] = firstname
                
                keys = range(7)
                # print(num_compare)
                # print(line)
                # print(line_compare)

                for if_num in keys:
                    # print(new_list_line)
                    # print(line_compare)

                    if line[if_num] == "":
                        new_list_line[if_num] = line_compare[if_num]
                        # pprint(line_compare)
                    else:
                        new_list_line[if_num] = line[if_num]
                    
                    # print(new_list_line[if_num])

                # code = 0 
                # for new_line in new_list:
                #     for lastnames in new_line.values():
                #         if new_list_line[0] == lastnames:
                #             code = 1

                compared.append(new_list_line[0])
                new_list.append(new_list_line)

                # if code == 0:
                #     new_list.append(new_list_line)

# pprint(new_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)