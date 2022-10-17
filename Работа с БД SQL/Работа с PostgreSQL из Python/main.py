from venv import create
import psycopg2

psycopg2.connect(database='netology_hw', user='matthew', password='management')
with psycopg2.conn.cursor() as cur:

    # Функция, создающая структуру БД (таблицы)
    cur.execute("create table test(id serial primary key);")
    psycopg2.connect.commit()
    psycopg2.connect.close()



# Функция, позволяющая добавить нового клиента
# Функция, позволяющая добавить телефон для существующего клиента
# Функция, позволяющая изменить данные о клиенте
# Функция, позволяющая удалить телефон для существующего клиента
# Функция, позволяющая удалить существующего клиента
# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)

psycopg2.connection.close()
