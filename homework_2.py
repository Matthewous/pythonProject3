def str_count(name):
    count = 0
    with open(name) as file:
        for line in file:
            count += 1
        return count

def reading(name, number):
    with open(name) as file:
        print(name)
        print(number)
        for line in file:
            print(line)

file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'

count_1 = str_count(file_name_1)
count_2 = str_count(file_name_2)
count_3 = str_count(file_name_3)

file_list = {}
file_list[file_name_1] = count_1
file_list[file_name_2] = count_2
file_list[file_name_3] = count_3

sorted_file_list = {}
sorted_keys = sorted(file_list, key=file_list.get)

for key in sorted_keys:
    sorted_file_list[key] = file_list[key]

print(file_list)
print(sorted_file_list)

for name, number in sorted_file_list.items():
    reading(name, number)

