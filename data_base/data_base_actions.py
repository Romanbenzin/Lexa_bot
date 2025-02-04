from psycopg2 import Error
from data_base.data_base_connect import connect_to_db, close_connection

def get_all_uses_name():
    """Функция для получения списка пользователей."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для получения данных
            cursor.execute("SELECT user_name FROM users")
            users = cursor.fetchall()
            return users
        except Error as e:
            print(f"Ошибка при получении пользователей: {e}")
            return []
        finally:
            close_connection(connection)

def get_all_uses_name_without_yana():
    """Функция для получения списка пользователей."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для получения данных
            cursor.execute("SELECT user_name FROM users WHERE sucker = True")
            users = cursor.fetchall()
            return users
        except Error as e:
            print(f"Ошибка при получении пользователей: {e}")
            return []
        finally:
            close_connection(connection)

def add_user(user_name, sucker=True):
    """Функция для добавления пользователя."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для добавления пользователя
            cursor.execute(
                "INSERT INTO users (user_name, sucker) VALUES (%s, %s);",
                (f"@{user_name}", sucker)
            )
            connection.commit()
            return f"Пользователь @{user_name} успешно добавлен."
        except Error as e:
            return f"Ошибка при добавлении пользователя: {e}"
        finally:
            close_connection(connection)
    else:
        return "Ошибка подключения к базе данных."


def delete_user(user_name):
    """Функция для удаления пользователя."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для удаления пользователя
            cursor.execute("DELETE FROM users WHERE user_name = %s;", (f"@{user_name}",))
            connection.commit()

            # Проверяем, был ли пользователь удален
            if cursor.rowcount > 0:
                return f"Пользователь @{user_name} успешно удален."
            else:
                return f"Пользователь @{user_name} не найден в базе данных."
        except Error as e:
            return f"Ошибка при удалении пользователя: {e}"
        finally:
            close_connection(connection)
    else:
        return "Ошибка подключения к базе данных."
