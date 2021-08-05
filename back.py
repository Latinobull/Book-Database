import psycopg2


def connect():
    conn = psycopg2.connect(
        "dbname='books' user='postgres' password='djdx1997' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id SERIAL PRIMARY KEY, title text, author text, year integer, isbn integer)"
    )
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = psycopg2.connect(
        "dbname='books' user='postgres' password='djdx1997' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO book (title,author,year,isbn) VALUES (%s,%s,%s,%s)",
        (
            title,
            author,
            year,
            isbn,
        ),
    )
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname='books' user='postgres' password='djdx1997' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


connect()
insert("Test", "Mr.Test", 2021, 234729175)
print(view())