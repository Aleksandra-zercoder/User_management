class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'  # Обычный пользователь

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Администратор

    def add_user(self, user_list: list, user: User):
        if not any(u.get_user_id() == user.get_user_id() for u in user_list):
            user_list.append(user)
            print(f"User {user.get_name()} (ID: {user.get_user_id()}) added successfully.")
        else:
            print(f"User {user.get_name()} (ID: {user.get_user_id()}) already exists.")

    def remove_user(self, user_list: list, user_id: int):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"User {user.get_name()} (ID: {user_id}) removed successfully.")
                return
        print(f"User with ID: {user_id} not found.")

    def grant_admin_rights(self, user_list: list, user_id: int):
        for user in user_list:
            if user.get_user_id() == user_id and user.get_access_level() == 'user':
                new_admin = Admin(user.get_user_id(), user.get_name())
                user_list.remove(user)
                user_list.append(new_admin)
                print(f"User {new_admin.get_name()} (ID: {new_admin.get_user_id()}) is now an Admin.")
                return
        print(f"User with ID: {user_id} not found or already an Admin.")

    def __str__(self):
        return f"Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"



