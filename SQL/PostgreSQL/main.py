import psycopg2
from pprint import pprint

def programm():

    start = 0
    
    while True:
        if start == 0:
            print("""Список команд:
                \na - добавить нового клиента
                \np - добавить телефон для существующего клиента
                \nc - изменить данные существующего клиента
                \ndp - удалить телефон существующего клиента
                \nd - удалить запись о клиенте
                \nf - найти клиента
                \n------------------------------------------\n""")

            start += 1
        else:
            command = input("Введите команду:")
            print()
            if command == "a":
                add_client(conn,insert_form())
                print("Клиент создан успешно")
            elif command == "p":
                client_id = str(input("Введите ID клиента:"))
                phone = input("Введите телефон:")
                add_phone(conn, client_id, phone)
                print("Телефон добавлен успешно")
            elif command == "c":
                client_id = str(input("Введите ID клиента:"))
                change_client(conn, client_id)
                print("Изменение прошло успешно")
            elif command == "dp":
                client_id = str(input("Введите ID клиента:"))
                delete_phone(conn, client_id)
                print("Удаление тефона прошло успешно")
            elif command == "d":
                client_id = str(input("Введите ID клиента:"))
                delete_client(conn, client_id)
                print("Удаление записи прошло успешно")
            elif command == "f":
                find_client(conn)
            elif command == "q":
                print("Завершение программы")
                break

def create_db(conn):

    cur.execute("CREATE TABLE first_names (id SERIAL PRIMARY KEY, first_name VARCHAR(40) NOT null);")
    cur.execute("CREATE TABLE last_names (id SERIAL PRIMARY KEY, last_name VARCHAR(40) NOT null);")
    cur.execute("CREATE TABLE emails (id SERIAL PRIMARY KEY, email VARCHAR(40) NOT null);")
    cur.execute("CREATE TABLE phones (id SERIAL PRIMARY KEY, phone VARCHAR(20));")
    cur.execute("""
        CREATE TABLE clients 
            (id integer NOT NULL,   
            first_name_id integer references first_names(id), 
            last_name_id integer references last_names(id), 
            email_id integer references emails(id), 
            phone_id integer references phones(id))
        ;
        """)
    
    conn.commit()

def delete_db(conn):

    cur.execute("DROP TABLE IF EXISTS clients")
    cur.execute("DROP TABLE IF EXISTS first_names")
    cur.execute("DROP TABLE IF EXISTS last_names")
    cur.execute("DROP TABLE IF EXISTS emails")
    cur.execute("DROP TABLE IF EXISTS phones")

    conn.commit()

def insert_form():
    
    name_imp = str(input("Введите имя: "))

    while name_imp == "":
        print("Имя - обязательное поле. Оно не должно быть пустым")
        name_imp = str(input("Введите имя: "))

    last_name_imp = str(input("Введите фамилию: "))

    while last_name_imp == "":
        print("Фамилия - обязательное поле. Оно не должно быть пустым")
        last_name_imp = str(input("Введите фамилию: "))

    email_imp = str(input("Введите email: "))

    while email_imp == "":
        print("Email - обязательное поле. Оно не должно быть пустым")
        last_name_imp = str(input("Введите email: "))

    phone_imp = input("Введите номер телефона: ")

    contact_list = [name_imp, last_name_imp, email_imp, phone_imp]

    return contact_list

def add_client(conn, contact_list):

    cur.execute(f"SELECT id FROM first_names WHERE first_name='{contact_list[0]}'")
    check = cur.fetchone()
    if check is None:
        cur.execute(f"INSERT INTO first_names(first_name) VALUES('{contact_list[0]}') RETURNING id")
        first_name_id = cur.fetchone()
    else:
        first_name_id = check

    cur.execute(f"SELECT id FROM last_names WHERE last_name='{contact_list[1]}'")
    check = cur.fetchone()
    if check is None:
        cur.execute(f"INSERT INTO last_names(last_name) VALUES('{contact_list[1]}') RETURNING id")
        last_name_id = cur.fetchone()
    else:
        last_name_id = check

    cur.execute(f"SELECT id FROM emails WHERE email='{contact_list[2]}'")
    check = cur.fetchone()
    if check is None:
        cur.execute(f"INSERT INTO emails(email) VALUES('{contact_list[2]}') RETURNING id")
        email_id = cur.fetchone()
    else:
        email_id = check

    cur.execute(f"SELECT id FROM phones WHERE phone='{contact_list[3]}'")
    check = cur.fetchone()
    if check is None:
        cur.execute(f"INSERT INTO phones(phone) VALUES('{contact_list[3]}') RETURNING id")
        phone_id = cur.fetchone()
    else:
        phone_id = check
    
    cur.execute("SELECT max(id) FROM clients")
    max_id = list(cur.fetchone())[0]
    if max_id is None:
        id = 1
    else:
        id = max_id + 1

    cur.execute(f"""
        INSERT INTO clients(id, first_name_id, last_name_id, email_id, phone_id) 
            VALUES('{id}', '{first_name_id[0]}', '{last_name_id[0]}', '{email_id[0]}', '{phone_id[0]}');
    """)

    conn.commit()
 
def add_phone(conn, client_id, phone):
    
    cur.execute(f"INSERT INTO phones(phone) VALUES('{phone}') RETURNING id")
    phone_id = list(cur.fetchone())
    cur.execute(f"SELECT first_name_id, last_name_id, email_id FROM clients WHERE id = '{client_id}'")
    data = list(cur.fetchone())
    
    cur.execute(f"""
        INSERT INTO clients(id, first_name_id, last_name_id, email_id, phone_id) 
            VALUES('{client_id}', '{data[0]}', '{data[1]}', '{data[2]}', '{phone_id[0]}');
    """)

    conn.commit()

def change_client(conn, client_id):
    
    print("""
    \nЧтобы поменять параметр - введите новое значение'
    \nЧтобы оставить параметр неизменным - нажмите enter\n
    """)

    new_first_name = input("Имя:")
    new_last_name = input("Фамилия:")
    new_email = input("Email:")
    new_phone = input("Телефон:")


    if new_first_name != "":
        cur.execute(f"INSERT INTO first_names(first_name) VALUES('{new_first_name}') RETURNING id")
        new_first_name_id = list(cur.fetchone())[0]     
        cur.execute(f"UPDATE clients SET first_name_id={new_first_name_id} WHERE id={client_id}")
    
    conn.commit()

    if new_last_name != "":
        cur.execute(f"INSERT INTO last_names(last_name) VALUES('{new_last_name}') RETURNING id")
        new_last_name_id = list(cur.fetchone())[0]     
        cur.execute(f"UPDATE clients SET first_name_id={new_last_name_id} WHERE id={client_id}")

    conn.commit()

    if new_email != "":
        cur.execute(f"INSERT INTO emails(email) VALUES('{new_email}') RETURNING id")
        new_email_id = list(cur.fetchone())[0]
        cur.execute(f"UPDATE clients SET first_name_id={new_email_id} WHERE id={client_id}")
    
    conn.commit()

    if new_phone != "":
        cur.execute(f"INSERT INTO phones(phone) VALUES('{new_phone}') RETURNING id")
        new_phone_id = list(cur.fetchone())[0]     
        cur.execute(f"UPDATE clients SET first_name_id={new_phone_id} WHERE id={client_id}")

    conn.commit()

def delete_phone(conn, client_id):
    
    cur.execute(f"UPDATE phones SET phone='NULL' WHERE id={client_id}")
    conn.commit()

def delete_client(conn, client_id):
    
    cur.execute(f"DELETE FROM clients WHERE id='{client_id}'")
    conn.commit()

def find_client(conn):

    print("""
    \nЧтобы использовать параметр при поиске - введите значение'
    \nЧтобы игнорировать параметр при поиске - нажмите enter\n
    """)

    first_name = input("Имя:")
    last_name = input("Фамилия:")
    email = input("Email:")
    phone = input("Телефон:")

    id_list = []

    if first_name != "":
        cur.execute(f"SELECT id FROM first_names WHERE first_name='{first_name}'")
        first_name_id = cur.fetchone()[0]
        cur.execute(f"SELECT id FROM clients WHERE first_name_id='{first_name_id}'")
        id_list.append(cur.fetchall())

    if last_name != "":
        cur.execute(f"SELECT id FROM last_names WHERE last_name='{last_name}'")
        last_name_id = cur.fetchone()[0]
        cur.execute(f"SELECT id FROM clients WHERE last_name_id='{last_name_id}'")
        id_list.append(cur.fetchall())
    
    if email != "":
        cur.execute(f"SELECT id FROM emails WHERE email='{email}'")
        email_id = cur.fetchone()[0]
        cur.execute(f"SELECT id FROM clients WHERE email_id='{email_id}'")
        id_list.append(cur.fetchall())

    if phone != "":
        cur.execute(f"SELECT id FROM phones WHERE email='{phone}'")
        phone_id = cur.fetchone()[0]
        cur.execute(f"SELECT id FROM clients WHERE phone_id='{phone_id}'")
        id_list.append(cur.fetchall())

    check = {}

    for group in id_list:
        for id in group:
            if id not in check.keys():
                check[id] = 1
            else:
                check[id] += 1

    find_list = []

    for id in check.keys():
        if check[id] == len(id_list):
            find_list.append(id[0])

    # print(find_list)
    result = []

    for id in find_list:
        cur.execute(f"""
        SELECT fn.first_name FROM first_names fn 
        where fn.id = (select c.first_name_id from clients c where c.id = '{id}')
        """)
        find_first_name = cur.fetchall()[0][0]

        cur.execute(f"""
        SELECT ln.last_name FROM last_names ln 
        where ln.id = (select c.last_name_id from clients c where c.id = '{id}')
        """)
        find_last_name = cur.fetchall()[0][0]

        cur.execute(f"""
        SELECT e.email FROM emails e
        where e.id = (select c.email_id from clients c where c.id = '{id}')
        """)
        find_email = cur.fetchall()[0][0]

        cur.execute(f"""
        SELECT p.phone FROM phones p 
        where p.id = (select c.phone_id from clients c where c.id = '{id}')
        """)
        find_phone = cur.fetchall()[0][0]

        res = [find_first_name, find_last_name, find_email, find_phone]
        result.append(res)
    
    conn.commit()
    print(f"Найдено {len(result)} человека:")
    pprint(result)

if __name__ == '__main__':
    
    conn = psycopg2.connect(database='netology_hw_1', user='matthew', password='management')
    cur = conn.cursor()
    # delete_db(conn)
    # create_db(conn)
    programm()
    conn.commit()
    conn.close()
