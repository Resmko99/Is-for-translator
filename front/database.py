import psycopg2


def connect():
    connection = psycopg2.connect(
        database="stud_group",
        user="stud_group_usr",
        password="N3vpU66W9u2jM0Tk",
        host="5.183.188.132",
    )
    return connection


def close_db_connect(connection, cursor):
    cursor.close()
    connection.close()