
def cook_book_form(name):
    with open(name) as file:
        result = {}
        for line in file:
            plate = line.strip()
            ingridients = []
            quantity = file.readline()
            for item in range(int(quantity)):
                ingridient = file.readline()
                ingridients.append(ingridient.strip())
            result[plate] = ingridients
            file.readline()

    positions = ['ingridient', 'quantity', 'measure']
    list = []
    ingr = []
    plates_list = []
    ingridients_list = []

    for b in result.keys():
        plates_list.append(b)

    for plate, ingr in result.items():
        for pos in ingr:
            new = pos.split(' | ')
            new[1] = int(new[1])
            p = dict(zip(positions, new))
            list.append(p)
        ingridients_list.append(list)
        list = []
    cook_book = dict(zip(plates_list,ingridients_list))
    return cook_book


def order():
    cook_book = cook_book_form('recipes.txt')
    dishes = []
    for plate in cook_book.keys():
        choise = input(f'Вы будете "{plate}"? - да/нет: ')
        if choise == 'да':
            dishes.append(plate)
    return dishes


def persons():
    quantity = int(input('Введите количество гостей: '))
    return quantity


def get_shop_list_by_dishes(dishes = order(), person_count = persons()):
    cook_book = cook_book_form('recipes.txt')
    # print(cook_book)
    order_book = {}
    for plate in dishes:
        ingridients_list = cook_book.get(plate)
        for list in ingridients_list:
            ingridient = str(list.get('ingridient'))
            if ingridient not in order_book.keys():
                list.pop('ingridient')
                list['quantity'] *= person_count
                order_book[ingridient] = list
            else:
                list.pop('ingridient')
                old = order_book.get(ingridient)
                quantit = old.get('quantity')
                adding = person_count * list['quantity'] + quantit
                list['quantity'] = adding
                order_book[ingridient] = list
    return order_book


cook_book_form('recipes.txt')
print(get_shop_list_by_dishes())


