documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2', '5455 028765'],
  '2': ['10006'],
  '3': []
}



# поиск имени по номеру документа
def name_by_doc(number):

    name = None
    for id in documents:
        for document in id.values():
            if document == number:
                name = id.get("name")

    if name is None:
        result = f"\nДокумент не найден\n-----------"
    else:
        result = f'\nВладелец документа {name}\n-----------'

    return result

# поиск полки по номеру документа

def shelf_by_doc(number):

    shelf = None
    for shelf_number, docs in directories.items():
        if number in docs:
            shelf = shelf_number

    if shelf is None:
        result = f"\nДокумент не найден\n-----------" 
    else:
        result = f'Документ находится на полке {shelf}\n-----------'

    return result 

# вывести список всех документов

def list_of_docs():
    print("Список документов:\n")
    for doc in documents:
        print(f"{doc['type']} {doc['number']} {doc['name']}\n-----------")
    return True

# добавить новый документ

def add_doc_check(doc_input):

    if doc_input == "1":
        result = "passport"
    elif doc_input == "2":
        result = "invoice"
    elif doc_input == "3":
        result = "insurance"
    else:
        result = "mistake"

    return result

def add_doc(doc_type, doc_number, doc_name, doc_dir):

    doc_dict = {'type':doc_type, 'number':doc_number, 'name':doc_name}
    documents.append(doc_dict)


    if doc_dir in directories:
        for key, value in directories.items():
            if key == doc_dir:
                value.append(doc_number)
    else:
        value = list()
        value.append(doc_number)
        directories[doc_dir] = value

    return True

# print(directories)
  

def task_1():
    start = 0
    while True:
        if start == 0:
            print("Список команд:\np - поиск имени по документу\ns - поиск полки по документу\nl - вывести список документов\na - добавить новый документ\nq - завершить программу\n------------------------------------------\n")
            start += 1
        else:
            command = input("Введите команду:")
            print()
            if command == "p":
                number = input("Введите номер документа:")
                print(name_by_doc(number))
                print()
            if command == "s":
                number = input("Введите номер документа:")
                print(shelf_by_doc(number))
                print()
            if command == "l":
                list_of_docs()
                print()
            if command == "a":
                doc_stastus = 0
                while doc_stastus == 0:
                    print("\nДопустимые типы документов:\n1 - passport\n2 - invoice\n3 - insurance\n")
                    doc_input = input("Выберите тип документа:")
                    doc_check = add_doc_check(doc_input)
                    if doc_check == "mistake":
                        print("Данного типа документов не существует, попробуйте заново\n")
                    else:
                        doc_type = doc_check
                        doc_stastus = 1
                
                doc_number = input("Введите номер документа:")
                doc_name = input("Введите имя владельца документа:")
                doc_dir = input("Введите номер полки хранения:")
                
                add_doc(doc_type, doc_number, doc_name, doc_dir)
                print(f'\n{doc_type} под номером {doc_number} сохранен и помещен на полку {doc_dir}. Владелец документа - {doc_name}\n-----------')
                print()
            elif command == "q":
                print("Завершение программы")
                break

if __name__ == '__main__':
    task_1()