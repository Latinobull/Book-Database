import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")


def connect():
    conn = psycopg2.connect(
        f"dbname='books' user={USER} password='{PASSWORD}' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id SERIAL PRIMARY KEY, title text, author text, year integer, isbn integer)"
    )
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = psycopg2.connect(
        f"dbname='books' user='{USER}' password='{PASSWORD}' host='localhost' port='5432'"
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
        f"dbname='books' user='{USER}' password='{PASSWORD}' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title=None, author=None, year=None, isbn=None):
    conditions = []
    args = []
    if title:
        conditions.append("title = %s")
        args.append(title)
    if author:
        conditions.append("author = %s")
        args.append(author)
    if year:
        conditions.append("year = %s")
        args.append(year)
    if isbn:
        conditions.append("isbn = %s")
        args.append(isbn)
    if conditions:
        sql = f"SELECT * FROM book WHERE {' OR '.join(conditions)}"
        conn = psycopg2.connect(
            f"dbname='books' user='{USER}' password='{PASSWORD}' host='localhost' port='5432'"
        )
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        conn.close()
    return rows


def delete(id):
    conn = psycopg2.connect(
        f"dbname='books' user='{USER}' password='{PASSWORD}' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = %s", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = psycopg2.connect(
        f"dbname='books' user='{USER}' password='{PASSWORD}' host='localhost' port='5432'"
    )
    cur = conn.cursor()
    cur.execute(
        "UPDATE book SET title = %s, author = %s, year = %s, isbn = %s WHERE id = %s ",
        (title, author, year, isbn, id),
    )
    conn.commit()
    conn.close()


connect()
# insert("Green Eggs and Ham", "Dr.Seuss", 2003, 11233440)
# insert("Cat in the Hat", "Dr.Seuss", 2001, 11234790)
# delete(1)
# update(2, "updateTest", "Mr.test", 2021, 1123945)
print(view())
