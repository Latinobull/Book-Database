import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            f"dbname='books' user={USER} password='{PASSWORD}' host='localhost' port='5432'"
        )
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id SERIAL PRIMARY KEY, title text, author text, year integer, isbn integer)"
        )
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute(
            "INSERT INTO book (title,author,year,isbn) VALUES (%s,%s,%s,%s)",
            (
                title,
                author,
                year,
                isbn,
            ),
        )
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title=None, author=None, year=None, isbn=None):
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
            self.cur.execute(sql, args)
            rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id = %s", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute(
            "UPDATE book SET title = %s, author = %s, year = %s, isbn = %s WHERE id = %s ",
            (title, author, year, isbn, id),
        )
        self.conn.commit()
