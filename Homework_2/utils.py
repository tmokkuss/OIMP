from datetime import datetime

ENTER = '\n'


def write_data(file_name, content):
    content = str(content) + ENTER
    with open(file_name, 'a') as file:
        file.write(content)


def get_id(username):
    username = username
    user_id = id(username)
    return user_id


def get_created_time():
    created_at = datetime.now().strftime("%H:%M:%S %d.%m.%Y")
    return created_at


def get_name():
    name = input("Введите название своего чата: ")
    return name


def read_data(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content


def get_users_chats(content):
    user_id = input("Введите ID пользователя: ")
    users_chats = []
    d = {}
    with open("Chats.txt") as file:
        content = file.read()
        content = content.removeprefix("{").removesuffix("}")
        content = content.split(",")
        for i in content:
            if user_id in i:
                chat_id = content[0].removeprefix("'chat_id': ")
                users_chats.append(chat_id)
        if len(users_chats) == 0:
            print(f"У пользователя с ID: {user_id} нет актуальных чатов")
        else:
            print(users_chats)
            return users_chats


def check_users_in_data(file_name, user_id):
    with open(file_name, 'r') as file:
        content = file.read()
    if user_id in content:
        return True
    else:
        return False


def how_users():
    users = []
    users_count = input("Введите cколько людей Вы хотите добавить в чат: ")
    for i in range(int(users_count)):
        user_id = input("Введите ID пользователя: ")
        check = check_users_in_data("Users.txt", user_id)
        if check == True:
            users.append(user_id)
            print(f"Пользователь с ID: {user_id} добавлен в чат")
        else:
            print("Введите действительный ID")
            users_count =+ 1
    return users


def send_message(user_id, ):
    check = check_users_in_data("Chats.txt", user_id)