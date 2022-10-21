import psycopg2

def create_db(conn):
    
    with cur:

        cur.execute("CREATE TABLE first_names (id SERIAL PRIMARY KEY, first_name VARCHAR(40) NOT null);")
        cur.execute("CREATE TABLE last_names (id SERIAL PRIMARY KEY, last_name VARCHAR(40) NOT null);")
        cur.execute("CREATE TABLE emails (id SERIAL PRIMARY KEY, email VARCHAR(40) NOT null);")
        cur.execute("CREATE TABLE phones (id SERIAL PRIMARY KEY, phone);")
        cur.execute("CREATE TABLE clients (id SERIAL PRIMARY KEY, first_name_id integer references first_names(id), last_name_id integer references last_names(id), email_id integer references emails(id), phone_id integer references phones(id));")

def delete_db(conn):

    with cur:

        cur.execute("DROP TABLE IF EXISTS first_names")
        cur.execute("DROP TABLE IF EXISTS last_names")
        cur.execute("DROP TABLE IF EXISTS emails")
        cur.execute("DROP TABLE IF EXISTS phones")
        cur.execute("DROP TABLE IF EXISTS clients")


if __name__ == '__main__':
    
    conn = psycopg2.connect(database='netology_hw_1', user='matthew', password='management')
    cur = conn.cursor()
    delete_db(conn)
    # create_db(conn)
    conn.commit()
    conn.close()

