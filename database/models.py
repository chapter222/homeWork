from database.db import connect

class DBTableCreator:
    def __init__(self):
        self.connection, self.cursor = connect('.../todos.db')

    def creator_todos_table(self):
        sql = """
            DROP TABLE IF EXISTS todos;
            CREATE TABLE IF NOT EXISTS todos(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE  
);
"""
        self.cursor.executescript(sql)
        self.connection.commit()
        print('Таблица todos создана')

creator = DBTableCreator()
creator.creator_todos_table()