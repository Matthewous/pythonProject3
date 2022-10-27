import psycopg2
from pprint import pprint

def delete_db(conn):

    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS clients")
        conn.commit()
    
def create_db(conn):

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE clients 
                (id INTEGER NOT NULL,   
                first_name VARCHAR(40) NOT null, 
                last_name VARCHAR(40) NOT null, 
                email VARCHAR(40) NOT null, 
                phone VARCHAR(40))
            ;
            """)
        conn.commit()

def add_client(conn, first_name, last_name, email, phone=None, id=None):
    
    with conn.cursor() as cur:
        
        if id is None:
            cur.execute("SELECT max(id) FROM clients")
            id = list(cur.fetchone())[0]
            if id is None:
                id = 1
            else: id += 1

        cur.execute("INSERT INTO clients(id, first_name, last_name, email, phone) VALUES(%s,%s,%s,%s,%s)", (id, first_name,last_name, email, phone))
        conn.commit()

def add_phone(conn, client_id, phone):

    with conn.cursor() as cur:
        
        cur.execute("SELECT first_name, last_name, email, phone FROM clients WHERE id=%s",(client_id,))
        data = list(cur.fetchone())
        if data[3] is None:
            cur.execute("INSERT INTO clients(phone) VALUES(%s) WHERE id = %s", (phone, client_id))
        else:
            add_client(conn, data[0], data[1], data[2], phone, client_id)
    
    conn.commit()

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phone=None):
    
    upd_list = [first_name, last_name, email, phone]

    with conn.cursor() as cur:
        
        if first_name is not None:
            cur.execute("UPDATE clients SET first_name=%s WHERE id=%s",(first_name,client_id))
        if last_name is not None:
            cur.execute("UPDATE clients SET last_name=%s WHERE id=%s",(last_name,client_id))
        if email is not None:
            cur.execute("UPDATE clients SET email=%s WHERE id=%s",(email, client_id))
        if phone is not None:
            cur.execute("UPDATE clients SET phone=%s WHERE id=%s",(phone,client_id))
    conn.commit()

def delete_phone(conn, client_id, phone):
    
    with conn.cursor() as cur:
        
        cur.execute("UPDATE clients SET phone=NULL WHERE id=%s AND phone=%s",(client_id, phone))

    conn.commit()

def delete_client(conn, client_id):
    
    with conn.cursor() as cur:
        cur.execute("DELETE FROM clients WHERE id=%s", (client_id,))
    conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    
    id_list = []

    with conn.cursor() as cur:

        if first_name is not None:
            cur.execute("SELECT id FROM clients WHERE first_name=%s",(first_name,))
            id_list.append(cur.fetchall())
        if last_name is not None:
            cur.execute("SELECT id FROM clients WHERE last_name=%s",(last_name,))
            id_list.append(cur.fetchall())
        if email is not None:
            cur.execute("SELECT id FROM clients WHERE email=%s",(email,))
            id_list.append(cur.fetchall())
        if phone is not None:
            cur.execute("SELECT id FROM clients WHERE phone=%s",(phone,))
            id_list.append(cur.fetchall())
 
        new_id_list = []

        for group in id_list:
            new_group = list(set(group))
            new_id_list.append(new_group)
        
        check = {}
        
        for group in new_id_list:
            for par in group:
                id = par[0]
                if id not in check.keys():
                    check[id] = 1
                else:
                    check[id] += 1

        find_list = []
        a = len(id_list)

        for key in check.keys():
            if check[key] == len(new_id_list):
                find_list.append(key)

        
        result = []
        num = 0

        for ids in find_list:
            cur.execute("SELECT first_name, last_name, email, phone FROM clients WHERE id=%s",(find_list[num],))
            res = (cur.fetchall())
            num += 1
    
        pprint(res) 

    conn.commit()

if __name__ == '__main__':
    
    with psycopg2.connect(database='netology_hw_1', user='matthew', password='management') as conn:

        delete_db(conn)
        create_db(conn)
        add_client(conn, "Иван", "Иванов", "mail@mail.ru", "3555")
        add_phone(conn, 1, "333")
        change_client(conn, 1, "Роман")
        find_client(conn, "Роман")
        delete_phone(conn, 1, "333")
        delete_client(conn, 1)
        conn.commit()
