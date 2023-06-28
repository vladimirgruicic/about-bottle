import sqlite3
import os

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    # Other methods for interacting with the database
    @staticmethod
    def create_table_users():
        db_path = os.path.join(os.getcwd(), 'db', 'aboutbottle.db')
        print(db_path)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            email TEXT NOT NULL
                          )'''
        )
        conn.commit()
        conn.close()
    
    @staticmethod
    def create_table_contacts():
        db_path = os.path.join(os.getcwd(), 'db', 'aboutbottle.db')
        print(db_path)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS contacts (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            contact TEXT NOT NULL
                          )'''
        )
        conn.commit()
        conn.close()
    
    @staticmethod
    def create_table_about():
        db_path = os.path.join(os.getcwd(), 'db', 'aboutbottle.db')
        print(db_path)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS about (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            about TEXT NOT NULL
                          )'''
        )
        conn.commit()
        conn.close()
    
    @staticmethod
    def create_table_zlatan():
        db_path = os.path.join(os.getcwd(), 'db', 'aboutbottle.db')
        print(db_path)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS zlatan (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            god_mode TEXT NOT NULL
                          )'''
        )
        conn.commit()
        conn.close()
    
    @staticmethod
    def insert_user(username, email):
        conn = sqlite3.connect('db/aboutbottle.db')
        cursor = conn.cursor()

        cursor.execute(
            '''
            INSERT INTO users 
            (
            username,
            email
            )
            VALUES (?, ?)
            ''',
            (username, email)
        )
        user_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return user_id

    @staticmethod
    def get_all_users():
        conn = sqlite3.connect('db/aboutbottle.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id, username, email FROM users')
        rows = cursor.fetchall()

        users = []
        for row in rows:
            user = User(row[0], row[1], row[2])
            users.append(user)

        conn.close()
        
        user_list = print(users)

        return user_list