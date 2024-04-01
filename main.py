from rud.todos import TodosService


todos_service = TodosService
"""
1) command
    1) todos
        create
            username
        read
            one
                id > username
            all
                list[username]
        update
            id > username
        delete
            one > id
            all 
    2) users
        create
        read
        update
        delete
"""
while True:

    # todos
    command = input('1.todos\ncommand: ')
    if command == 'todos':
        crud_commands = "\n".join(['1. create', '2. read', '3. update', '4. delete'])
        crud_command = input(f'{crud_commands}\nВыберите цифру: ')
        if crud_command == "1":
            print('create')
            username = input('username: ')
            todos_service.create(username=username)
        elif crud_command == '2':
            print('read')
            users = todos_service.read()
            for user_id, username in users:
                print(f'''==========
ID: {user_id}
USERNAME: {username}
==========
''')
        elif crud_command == '3':
            users = [username for _, username in todos_service.read()]
            users_names = "\n".join([f'{idx}. {username}' for idx, username in enumerate(users, start=1)])
            name_for_update = input(f'{users_names}\nНапиши имя для обновления: ')
            new_name = input('новое имя: ')
            todos_service.update(username=name_for_update, new_username=new_name)
        elif crud_command == '4':
            print('delete')
            users = [username for _, username in todos_service.read()]
            users_names = "\n".join([f'{idx}. {username}' for idx, username in enumerate(users, start=1)])
            name_for_delete = input(f'{users_names}\nНапиши имя для удаления: ')
            todos_service.delete(username=name_for_delete)
    elif command == 'todos':
        pass
