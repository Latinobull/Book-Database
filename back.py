import psycopg2


def connect():
    conn = psycopg2.connect(
        "dbname='books' user='postgres' password='djdx1997' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)"
    )
    conn.commit()
    conn.close()


connect()