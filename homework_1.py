
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

# cook_book = cook_book_form('recipes.txt')

# print(cook_book_form('recipes.txt'))


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
    order_book = {}
    for plate in dishes:
        ingridients_list = cook_book.get(plate)
        for list in ingridients_list:
            ingridient = str(list.get('ingridient'))
            list.pop('ingridient')
            list['quantity'] *= person_count
            order_book[ingridient] = list
    
    ingridients_list = {}
    for a in cook_book.values():
        for b in a:
            i = b.get('ingridient')
            ingridients_list[i] = 0
    print(ingridients_list)

    count = 0
    n = 0

    for ingridient in order_book:
        print(ingridient)
        for name, count in ingridients_list.items():
            if name == ingridient:
                ingridients_list[name] = count + 1
    print(ingridients_list)
    
    return order_book



cook_book_form('recipes.txt')
print(get_shop_list_by_dishes())


