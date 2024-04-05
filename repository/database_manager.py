import sqlite3
import random


class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.table_name_link_storage = "link_storage"
        self.table_users = "users"

    def create_table(self):
        with sqlite3.connect(self.db_file) as db:
            db.execute(
                f"""CREATE TABLE IF NOT EXISTS {self.table_name_link_storage}
                                (id INTEGER PRIMARY KEY, link TEXT, user_id INTEGER)"""
            )

            db.commit()

    def insert_link(self, link, user_id):
        with sqlite3.connect(self.db_file) as db:
            db.execute(
                f"INSERT INTO {self.table_name_link_storage} (link, user_id) VALUES (?, ?)",
                (link, user_id),
            )
            db.commit()

    def check_link_exists(self, text, user_id):
        with sqlite3.connect(self.db_file) as db:
            cursor = db.execute(
                f"SELECT * FROM {self.table_name_link_storage} WHERE user_id=? AND link=?",
                (user_id, text),
            )
            row = cursor.fetchone()
            return bool(row)

    def get_all_articles(self, user_id):
        with sqlite3.connect(self.db_file) as db:
            cursor = db.execute(
                f"SELECT * FROM {self.table_name_link_storage} WHERE user_id=?",
                (user_id,),
            )
            all_articles = cursor.fetchall()
            return all_articles

    def get_random_article(self, user_id):
        with sqlite3.connect(self.db_file) as db:
            cursor = db.execute(
                f"SELECT * FROM {self.table_name_link_storage} WHERE user_id=?",
                (user_id,),
            )
            all_articles = cursor.fetchall()
            if all_articles:
                random_article = random.choice(all_articles)
                db.execute("DELETE FROM link_storage WHERE id=?", (random_article[0],))
                db.commit()
                return random_article[1]  # Возвращаем ссылку на случайную статью
            else:
                return None  # Если база данных пуста, возвращаем None
