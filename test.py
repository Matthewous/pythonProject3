id_list = [[(3,), (4,)], [(3,)]]

check = {}

for group in id_list:
    for id in group:
        if id not in check.keys():
            check[id] = 1
        else:
            check[id] += 1

find_list = []

for id in check.keys():
    if check[id] == 2:
        find_list.append(id[0])

print(find_list)