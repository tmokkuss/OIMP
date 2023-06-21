from main import *


if __name__ == '__main__':
    command = input("\t\t\t\tДобрый день\n"
                    "\t\t\tЧто Вы хотите сделать?\n"
                    "Чтобы использовать команды скопируйте ниже одну из них и вставьте\n"
                    "---------------------------------------------------------------------------------\n"
                    "| Добавить нового пользователя \t Создать новый чат                              |\n"
                    "|                                                                              \t|\n"
                    "| Отправить сообщение в чат \t Получить список чатов конкретного пользователя |\n"
                    "|                                                                              \t|\n"
                    "| Получить список сообщений в конкретном чате                                  \t|\n"
                    "---------------------------------------------------------------------------------\n"
                    "Command: ")

    if command == "Добавить нового пользователя" or command == "Добавить нового пользователя ":
        print("<-----Добавление нового пользователя----->")
        username = input("Введите Ваш username: ")
        user_id = get_id(username)
        created_at = get_created_time()
        read_data("Users.txt")
        request = User(user_id=user_id, username=username, user_created_time=created_at).add_new_user

    elif command == "Создать новый чат" or command == "Создать новый чат ":
        print("<-----Создание нового чата----->")
        created_at = get_created_time()
        chat_users = how_users()
        chat_name = get_name()
        chat_id = get_id(chat_name)
        request = Chat(chat_id=chat_id, chat_name=chat_name, chat_users=chat_users,
                       chat_created_time=created_at).add_new_chat

    elif command == "Получить список чатов конкретного пользователя" or command == "Получить список чатов конкретного пользователя ":
        print("<-----Получение списка чатов пользователя----->")
        content = read_data("Chats.txt")
        get_users_chats(content=content)

    elif command == "Отправить сообщение в чат" or command == "Отправить сообщение в чат ":
        print("<-----Отправка сообщения в чат----->")