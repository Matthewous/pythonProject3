
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


print(cook_book_form('recipes.txt'))




