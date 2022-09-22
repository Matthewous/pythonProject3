from pprint import pprint
import csv
import re

# filepath = "/Users/matthew/Desktop/pythonProject3/py-homeworks-advanced/Regular_expressions/phonebook_raw.csv"

# with open(filepath) as f:
#     rows = csv.reader(f, delimiter=",")
#     contacts_list = list(rows)

# def name_correction(contacts_list):

#     pattern = r"(\w+)\s?(\w+)?\s?(\w+)?"
#     substitution_lastname = r"\1"
#     substitution_firstname = r"\2"
#     substitution_surname = r"\3"

#     for line in contacts_list:
#         lastname = re.sub(pattern, substitution_lastname, line[0])
#         firstname = re.sub(pattern, substitution_firstname, line[0])
#         surname = re.sub(pattern, substitution_surname, line[0])

#         line[0] = lastname

#         if line[1] == "":
#             line[1] = firstname
        
#         if line[2] == "":
#             line[2] = surname

#     return(contacts_list)


# list1 = [1, 2, 3, 4]
# list2 = [4, 5, 6, 7]
# # list3 =  list(set(list1) & set(list2))

# # print(list3)
# l = list1 + list(set(list2) - set(list1))
# print(l)

contacts_list = [
    ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'], 
    ['Усольцев', 'Олег', 'Валентинович', 'ФНС', 'главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц', '+7(495)913-04-78', 'opendata@nalog.ru'], 
    ['Мартиняхин', 'Виталий', 'Геннадьевич', 'ФНС', '', '+7(495)913-00-37', ''], 
    ['Наркаев', 'Вячеслав', 'Рифхатович', '', 'ФНС', '', '+7(495)913-01-68', ''], 
    ['Мартиняхин', 'Виталий', 'Геннадьевич', 'ФНС', 'cоветник отдела Интернет проектов Управления информационных технологий', '', '', ''], 
    ['Лукина', 'Ольга', 'Владимировна', 'Минфин', '', '+7(495)983-36-99 доб.2926', 'Olga.Lukina@minfin.ru'], 
    ['Паньшин', 'Алексей', 'Владимирович', 'Минфин', '', '+7(495)748-49-73', '1248@minfin.ru'], 
    ['Лагунцов', 'Иван', 'Алексеевич', 'Минфин', '', '+7(495)913-11-11 доб.0792', ''], 
    ['Лагунцов', 'Иван', '', '', '', '', 'Ivan.Laguntcov@minfin.ru']
]

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

final_list = []
line_to_final = []

num = range(7)

for n in num:
    for line in new_list:
        for value in line.values():
            line_to_final.append(value)
        final_list.append(line_to_final)

print(final_list)
# print

# new_list = []

# contacts_dict = {
#     'lastname': None, 
#     'firstname': None, 
#     'surname': None, 
#     'organization': None, 
#     'position': None, 
#     'phone': None, 
#     'email': None
# }

# for line in contacts_list[1:]:
#     contacts_dict['lastname'] = line[0]
#     contacts_dict['firstname'] = line[1]
#     contacts_dict['surname'] = line[2]
#     contacts_dict['organization'] = line[3]
#     contacts_dict['position'] = line[4]
#     contacts_dict['phone'] = line[5]
#     contacts_dict['email'] = line[6]
#     new_list.append(contacts_dict)



# pprint(new_list)

# # number = 0
# # for contact in new_list:
# #     if number == 0:
# #         lastname = contact[0]
# #         number += 1
# #     else:
# #         if contact[0] == lastname:

