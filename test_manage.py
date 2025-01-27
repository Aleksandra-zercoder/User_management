from User_manage import User, Admin  # Импортируем классы из основного файла

user_list = []
admin = Admin(1, "Alice")

while True:
    action = input("Введите команду (add, remove, list, grant_admin, exit): ").strip().lower()

    if action == "add":
        user_id = int(input("Введите ID пользователя: "))
        name = input("Введите имя пользователя: ")
        new_user = User(user_id, name)
        admin.add_user(user_list, new_user)

    elif action == "remove":
        user_id = int(input("Введите ID пользователя для удаления: "))
        admin.remove_user(user_list, user_id)

    elif action == "list":
        print("\nТекущий список пользователей:")
        for user in user_list:
            print(user)

    elif action == "grant_admin":
        user_id = int(input("Введите ID пользователя, которому дать права администратора: "))
        admin.grant_admin_rights(user_list, user_id)


    elif action == "exit":
        print("Выход из программы.")
        break

    else:
        print("Неизвестная команда, попробуйте снова.")
