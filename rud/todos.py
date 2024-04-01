from database.db import connect

class TodosService:
    connection, cursor = connect('todos.db')

    def __check_todos_exists(self, **kwargs):
        sql = "SELECT id FROM todos WHERE username = ?;"
        self.cursor.execute(sql, (kwargs['username'],))
        user_id = self.cursor.fetchone()
        if user_id:
            return True
        return False

    def create(self, **kwargs):
        if self.__check_todos_exists(username=kwargs['username']):
            print('Такой пользователь уже существует: ')
            return
        sql = "INSERT INTO todos(username) VALUES (?)"
        self.cursor.execute(sql, (kwargs['username'],))
        self.connection.commit()


    def read(self, **kwargs):
        sql = "SELECT * FROM todos;"
        users = self.cursor.execute(sql).fetchall()
        return users

    def update(self, **kwargs):
        sql = "UPDATE todos SET username = ? WHERE username = ?"
        self.cursor.execute(sql, (kwargs['new_username'], kwargs['username']))
        self.connection.commit()


    def delete(self, **kwargs):
        sql = "DELETE FROM todos WHERE username = ?"
        self.cursor.execute(sql, (kwargs['username'],))
        self.connection.commit()
        print(f'Удалили пользователя с именем {kwargs["username"]}')
